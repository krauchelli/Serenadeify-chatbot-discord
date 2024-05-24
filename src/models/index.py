from processing_model import preprocessing_predict
from processing_model import predict_text
import tensorflow as tf
from flask import Flask, request, jsonify

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


if __name__ == '__main__':
    app.run(debug=True, port=5000)