from django.contrib import messages
import logging
from accounts.models import User, CustomUser
from firebase_admin import firestore, auth

logger = logging.getLogger(__name__)
db = firestore.client()


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

    return user_id