import logging
from firebase_admin import firestore

logger = logging.getLogger(__name__)
db = firestore.client()

def get_books():
     books_ref = db.collection('books')
     books_docs = books_ref.get()
     books_data = [doc.to_dict() for doc in books_docs]
     return books_data

def get_comments(book_id):
    book_ref = db.collection('books').document(book_id)
    book_data = book_ref.get().to_dict()
    comments_ref = db.collection("comments")
    query = comments_ref.where("book_id", "==", book_id).get()    
    return book_data, query 

def get_my_books(author_id):
    user_books_ref = db.collection('books').where('author_id', '==', author_id)
    user_books = [doc.to_dict() for doc in user_books_ref.get()]
    return user_books

def edit_my_book(book_id, title, summary, kind):
    doc_ref = db.collection('books').document(book_id)
    doc_ref.update({
            'title': title,
            'summary': summary,
            'kind': kind
        })

def delete_my_book(book_id):
    db.collection('books').document(book_id).delete()    

def create_my_book(request, form):
    author_id = request.user.firebase_id
    author_name = request.user.username
    book = form.save(commit=False)
    book.author = author_id  # Set the logged-in user as the author
    book.save()
    doc_ref = db.collection('books').document()
    doc_ref.set({
        'title': book.title,
        'summary': book.summary,
        'kind': book.kind,
        'author_id': author_id,
        'author_name': author_name,
        "published_date": book.published_date
    })
    id_new = doc_ref.id
    doc_ref = db.collection('books').document(id_new)  # Belgeye ulaşmak için belge kimliğini belirtin
    doc_ref.update({'id': id_new})     

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
    return user_id
"""