from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
import requests
import logging
from accounts.models import CustomUser
from firebase_admin import firestore

logger = logging.getLogger(__name__)
db = firestore.client()

def auth2(email, password):
    db = firestore.client()
    user_ref = db.collection('kullanicilar').where('email', '==', email).limit(1)
    snapshot = user_ref.get()
    if len(snapshot) == 0:
        return None
    user_data = snapshot[0].to_dict()
    if user_data.get('password') == password:
        return user_data
    else:
        return None

def try_login(email, password, request):
    try:
        firebase_api_key = 'AIzaSyB_ELWZV2qJphITNNmQ-guwxxZw9L7Jc5k'
        request_data = {
            "email": email,
            "password": password,
            "returnSecureToken": True
        }
        response = requests.post(
            f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={firebase_api_key}",
            json = request_data
        )
        user_data = response.json()
        if 'error' in user_data:
            messages.error(request, 'Invalid username or password.')
        else:
            user_data_full = auth2(email,password)
            if user_data_full:
                existing_user = CustomUser.objects.filter(email=email).exists()
                if not existing_user:
                    user = CustomUser(username=user_data_full.get('username'),
                                        email=email, 
                                        password=password,
                                        role=user_data_full.get('role'), 
                                        firebase_id = user_data_full.get('firebase_id')
                                        )
                    user.save()
                    login(request, user)
                    return True
                else:
                    userr = CustomUser.objects.get(email=email)
                    userr.firebase_id=user_data_full.get('firebase_id')
                    userr.save()
                    login(request, userr)
                    return True
            print(user_data_full.get('username'),user_data_full.get('role'))
            return redirect('home')
    except Exception as e:
            messages.error(request, 'An error occurred. Please try again later.')

"""
def save_user(form):
    try:
            firebase_id = getFirebaseID()
            user = form.save()
            user = User.objects.create(username=form.cleaned_data['username'],
                                       password=form.cleaned_data['password1'],
                                       email=form.cleaned_data['email'],
                                       role=form.cleaned_data['role'],
                                       firebase_id=firebase_id)
            return True
    except Exception as e:
         return False

def getFirebaseID():
    db = firestore.client()
    query = db.collection("kullanicilar").order_by('datetime', direction=firestore.Query.DESCENDING).limit(1).stream()
    user_id = 0
    for doc in query:
        user_data = doc.to_dict()
        user_id = user_data.get('firebase_id')
        user_id = user_id + 1
        break
    return user_id"""
