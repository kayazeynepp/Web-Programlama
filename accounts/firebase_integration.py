import firebase_admin
from firebase_admin import credentials, auth
import os

current_directory = os.getcwd()
file_path = os.path.join(current_directory, "fjson.json")
# Initialize Firebase Admin SDK
cred = credentials.Certificate(file_path)
# Firebase Admin SDK'nın kullanılabilmesi için gerekli kimlik doğrulama bilgileri
app = firebase_admin.initialize_app(cred, name='proje_adi')
# Yeni kullanıcı oluşturma fonksiyonu
def add_user(email, password):
    user = auth.create_user(
        email=email,
        password=password
    )
    print("Yeni kullanıcı oluşturuldu:", user.uid)

