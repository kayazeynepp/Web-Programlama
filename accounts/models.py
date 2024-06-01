from django.contrib.auth.models import AbstractUser
from django.db import models
from firebase_admin import firestore, auth
from datetime import datetime

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('author', 'Author'),
        ('reader', 'Reader'),
    ]
    role = models.CharField(
        max_length=6, 
        choices=ROLE_CHOICES, 
        default='reader'
        )
    firebase_id = models.CharField(
        max_length=6, 
        default='000000' 
        )
    email = models.CharField(max_length=255)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        blank=True
    )
    def __str__(self):
        return self.username


class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    role = models.CharField(max_length=50)
    firebase_id = models.CharField(max_length=50,default='0')

    def save(self, *args, **kwargs):
        user = auth.create_user(
            email=self.email,
            password=self.password,
            display_name=self.username,
        )
        firebase_uid = user.uid
        db = firestore.client()
        doc_ref = db.collection('kullanicilar').document()
        doc_ref.set({
            'username': self.username,
            'password': self.password,
            'email': self.email,
            'role': self.role,
            'uid': firebase_uid,
            'datetime': datetime.now(),
            'firebase_id': self.firebase_id,
        })
