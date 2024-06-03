import tensorflow as tf
from flask import Flask, request, jsonify
# functions from other files
from processing_model import preprocessing_predict
from processing_model import predict_text
from song_recommend import getRecommendation

app = Flask(__name__)

#routes
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    print(data)
    text = data['text']
    prediction = int(predict_text(text))
    print(f'printing prediction value: {prediction}')
    return jsonify({'prediction': prediction})

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    print(data)
    prediction = data['prediction']
    recommendation = getRecommendation(prediction)
    print(f'printing recommendation value: {recommendation}')
    return jsonify({'recommendation': recommendation})

if __name__ == '__main__':
    app.run(debug=True, port=5000)