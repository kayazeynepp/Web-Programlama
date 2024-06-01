from django import forms
from .models import Books, Comments

class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['title', 'summary', 'kind']  # fields değişkenine author eklendi
        labels = {'kind': 'Kind'}
        widgets = {
            'kind': forms.Select(choices=Books.KIND_CHOICES)
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['comment']
