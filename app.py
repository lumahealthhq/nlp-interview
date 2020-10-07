from flask import Flask, render_template, request

import joblib
import re
import string

from googletrans import Translator
translator = Translator()

app = Flask(__name__)

def text_prep(text):
    #clean text
    punct = set(string.punctuation)
    text = re.sub(r"n't", " not ", text)
    text = re.sub(r"\'s", " ", text)
    text = re.sub(r"\'ve", " have ", text)
    text = re.sub(r"\'re", " are ", text)
    text = re.sub(r"\'d", " would ", text)
    text = re.sub(r"\'ll", " will ", text)
    
    #remove non-letters and lower case
    text = re.sub('[^a-z\s]', '', text.lower())
    
    #remove punctuation        
    punc_removed = [char for char in text if char not in punct]
    punc_removed = ''.join(punc_removed)
    
    return [word for word in punc_removed.split()]

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    sentiment_classifier_model = open('./model/sentiment_classifier_model.pkl','rb')
    tfidf_v, clf = joblib.load(sentiment_classifier_model)

    if request.method == 'POST':
        message = request.form['message']

        if message.isdigit():
            return render_template('home.html', prediction='invalid')

        if translator.detect(message).lang != 'en':
            message = translator.translate(message).text

        data = [message]
        vect = tfidf_v.transform(data).toarray()
        my_prediction = clf.predict(vect)

    return render_template('home.html', prediction=my_prediction)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

