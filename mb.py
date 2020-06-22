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
           

      
@api.route("/analysis/")
class BooksList(Resource):
    def get(self):
        """
        returns a list of books
        """
        req_data = request.json(force = True)
        if not req_dataata:
            data1 = {"responsgjhge": "ERROR"}
            return data1, 404
        #else :
        word = req_data['word']
        Analword = Word_Sentiment_Tweets("violence")
        data = []
        St = []
        data, St, rp , rn = Analword.get_Sentiment()
        return "Hello"
        #return {"data" : data,
        #"Sentiment" : St,
        #"resp": rp,
        #"resn": rn}
            #return [{"resp": str(rp),
            #"resn": str(rn)}]

    def post(self):
        """
        Add a new book to the list
        """
        data = request.get_json()
        if not data:
            data = {"response": "ERROR"}
            return data, 404
        else:
            wordkey = data.get('data')
            if wordkey:
                get(wordkey)
@app.route("/wordd")
def indexx(): 
    word = Word_Sentiment_Tweets("trump")
    rp , rn = word.get_Sentiment()
    return "rn"

        

class Analysis(Resource):
     def __init__(self):
        self.tc = Word_Sentiment_Tweets("trump")
     def get(self, word):
        return self.tc.get_Sentiment()
        #return "Hello World!"


api.add_resource(Analysis,'/word')


if __name__ == "__main__":
    app.run()
    

