from flask import Flask, request, jsonify
from helper import preprocessing, vectorizer, get_prediction

app = Flask(__name__)

data = dict()
reviews = []
positive = 0
negative = 0

@app.route('/api', methods=['GET'])
def api():
    data['reviews'] = reviews
    data['positive'] = positive
    data['negative'] = negative
    return data

@app.route('/send-comments',methods=['POST'])
def sendComment():
    comment = request.args.get('comment')
    preProcessedText = preprocessing(comment)
    vectorizedText = vectorizer(preProcessedText)
    prediction = get_prediction(vectorizedText)
   
    if prediction == 'negative':
        global negative
        negative += 1
    else:
        global positive
        positive += 1

    res={
        'prediction': prediction,
        'negative':negative,
        'positive':positive
    }
    reviews.insert(0, comment)
    return jsonify(res)


if __name__ == '__main__':
    app.run()
