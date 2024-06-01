import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

# Download NLTK resources if not already downloaded
nltk.download('punkt')
nltk.download('stopwords')
# Load Turkish stopwords
stop_words = set(stopwords.words('turkish'))

def load_words_from_file(filename):
    words = set()
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            word = line.strip().lower()  # Remove leading/trailing whitespaces and convert to lowercase
            words.add(word)
    return words

# Load positive and negative words from files
positive_words = load_words_from_file('pozitif.txt')
negative_words = load_words_from_file('negatif.txt')

def get_sentiment(text):
    tokenizer = RegexpTokenizer(r'\w+')
    words = tokenizer.tokenize(text.lower())  # Convert text to lowercase
    # Remove stopwords
    filtered_words = [word for word in words if word not in stop_words]
    positive_count = sum(1 for word in filtered_words if word in positive_words)
    negative_count = sum(1 for word in filtered_words if word in negative_words)
    if positive_count > negative_count:
        return 'positive'
    elif negative_count > positive_count:
        return 'negative'
    else:
        return 'neutral'
