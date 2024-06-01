from django.contrib.auth.decorators import login_required
from .forms import BookForm
from firebase_admin import firestore
from django.shortcuts import render, redirect
from personal_assignments.ai import get_sentiment
from django.contrib import messages
from personal_assignments.third_party import third_party_usage
from personal_assignments.cookie import getTheme
from personal_assignments.business_layer import save_comment
from personal_assignments.data_layer import get_comments, get_my_books, edit_my_book, delete_my_book, create_my_book

db = firestore.client()

@login_required
def create_comment(request, book_id):
    if request.method == 'POST':
        comment = request.POST.get("comment")
        if not comment:
            messages.error(request, "Yorum boş olamaz.")
            return redirect('book_detail', book_id=book_id)
        save_comment(request, book_id, comment)
        return redirect('book_detail', book_id=book_id)
    else:
        messages.error(request, "Geçersiz istek türü.")
        return redirect('home')

def book_detail(request, book_id):
    theme = getTheme(request)
    try:
        book_data, query = get_comments(book_id)
        comments = []
        notr , positive, negative = 0, 0, 0
        for doc in query:
            #yorumun duygu analizi
            sentiment = get_sentiment(doc.to_dict()["comment"])
            dictionary = doc.to_dict()
            dictionary["sentiment"] = sentiment
            comments.append(dictionary)
            if sentiment == "negative":
                negative += 1
            elif sentiment == "positive":
                positive += 1
            else:
                notr += 1
        uri=third_party_usage(positive, negative, notr)
        return render(request, 
                      'books/book_detail.html', 
                      {'book': book_data, 
                       'comments':comments, 
                       'image': uri, 
                       'theme':theme}
                       )
    except Exception as e:
        messages.error(request, f"Bir hata oluştu: {e}")
        return redirect('home')

@login_required
def my_books(request):
    theme = getTheme(request)
    author_id = str(request.user.firebase_id)
    user_books = get_my_books(author_id)
    return render(request, 
                  'my_books.html', 
                  {'books': user_books, 'theme':theme})

@login_required
def edit_book(request, book_id):
    theme = getTheme(request)
    if request.method == 'POST':
        title = request.POST.get('title')
        summary = request.POST.get('summary')
        kind = request.POST.get('kind')
        edit_my_book(book_id, title, summary, kind)
        return redirect('my_books')
    else:
        doc_ref = db.collection('books').document(book_id)
        book_data = doc_ref.get().to_dict()
        return render(request, 'edit_book.html', 
                      {'book': book_data, 
                       'theme':theme})

@login_required
def delete_book(request, book_id):
    theme = getTheme(request)
    if request.method == 'POST':
        delete_my_book(book_id)
        return redirect('my_books')
    else:
        doc_ref = db.collection('books').document(book_id)
        book_data = doc_ref.get().to_dict()
        return render(request, 'delete_book.html', 
                      {'book': book_data, 
                       'theme':theme})

@login_required
def create_book(request):
    theme = getTheme(request)
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
           create_my_book(request, form)
           return redirect('home')
    else:
        form = BookForm()
    return render(request, 'books/create_book.html', 
                  {'form': form, 
                   'theme':theme})
