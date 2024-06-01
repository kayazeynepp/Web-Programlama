from firebase_admin import firestore
from datetime import datetime

db = firestore.client()

def save_comment(request, book_id, comment):
    try:
            doc_ref = db.collection('books').document(book_id)
            book_data = doc_ref.get().to_dict()
            user_id = request.user.id
            username = request.user.username
            comments_ref = db.collection('comments')
            comments_ref.add({
                'book_id': book_id,
                'comment': comment,
                'user_id': user_id,
                'user_username': username,
                'created_at': datetime.now()  # Add the timestamp
            })
            return True
    
    except Exception as e:
        return False
