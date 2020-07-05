from flask import Flask, request
#from flask_restful import Resource, Api
from flask_restplus import Api, Resource
from flask import json
from TweetClassifier import Word_Sentiment_Tweets
from flask import jsonify

app = Flask(__name__)
#api = Api(app)
api = Api(app=app, version='0.1', title='Books Api', description='', validate=True)

@app.route("/")
def index(): 
    return "Hello World!"

@app.route("/getAnalysis", methods = ['GET','POST'])
def getAnalysis():
        req_data = request.get_json()
        word = req_data['word']
        print(word)
        Analword = Word_Sentiment_Tweets(word)
        data = []
        St = []
        data, St, rp , rn = Analword.get_Sentiment()


        return {"data" : data,
        "Sentiment" : St,
        "resp": rp,
           "resn": rn}
           

      



if __name__ == "__main__":
    app.run()
    

