from django.db import models
from django.conf import settings

class Books(models.Model):
    KIND_CHOICES = [
        ('psikoloji', 'Psikoloji'),
        ('polisiye', 'Polisiye'),
        ('roman', 'Roman'),
        ('biyografi', 'Biyografi'),
        ('gezi', 'Gezi'),
        ('ani', 'Anı'),
        ('akademi', 'Akademi'),
        ('yemek', 'Yemek'),
        ('tarih', 'Tarih'),
    ]
    kind = models.CharField(
        max_length=20, 
        choices=KIND_CHOICES, 
        default='roman'
        )
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateTimeField(auto_now_add=True)
    summary = models.TextField()

    def __str__(self):
        return self.title


class Comments(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE
        )  
    # Django'nun kendi kullanıcı modelini kullanarak web security nin sağlanması amaçlandı
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"
