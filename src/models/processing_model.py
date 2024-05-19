import re
import string
import numpy as np
from nltk.corpus import stopwords
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model

def preprocessing_predict(text):
    stop_words = set(stopwords.words('english'))
    text = text.lower()
    remove_stopwords = [word for word in text.split() if word not in stop_words]
    text = ' '.join(remove_stopwords)
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = re.sub(r"\d", '', text)
    text = re.sub(r"\s+", " ", text)
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts([text])
    max_length = len(text.split())
    text = tokenizer.texts_to_sequences([text])
    text = pad_sequences(text, maxlen=79)
    text = np.array(text)
    return text

#load the model
def predict_text(text):
    # Preprocess the text
    preprocessed_text = preprocessing_predict(text)

    # Load the model
    model = load_model('C:/Users/kraun/OneDrive/Documents/archivenandatugas/SEMESTER 4/Temu Kembali Informasi/Tugas Akhir/Serenadeify-chatbot-discord/src/models/mood_predict.h5')
    # Make a prediction
    prediction = model.predict(preprocessed_text)

    y = np.argmax(prediction, axis=1)

    return f'The predicted mood is {y} for the full result of prediction {prediction}'

text = 'i am happy, i cant endure this overflowing joy'
result = predict_text(text)
print(result)
