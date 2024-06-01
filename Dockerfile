FROM python:3.11.5

WORKDIR /web

# requirements.txt dosyasını kopyala
COPY requirements.txt .

# Bağımlılıkları yükle
RUN pip install --no-cache-dir -r requirements.txt

# NLTK veri setlerini indir

# Proje dosyalarını kopyala
COPY . .

# Django uygulamasını başlatmak için komutu ayarla
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
