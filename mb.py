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
      
@api.route("/books/")
class BooksList(Resource):
    def get(self):
        """
        returns a list of books
        """
        word = Word_Sentiment_Tweets("trump")
        data = []
        St = []
        data, St, rp , rn = word.get_Sentiment()
        return [{"data" : data,
        "Sentiment" : St,
        "resp": rp,
            "resn": rn}]

    def post(self):
        """
        Add a new book to the list
        """
        data = request.get_json()
        if not data:
            data = {"response": "ERROR"}
            return data, 404
        else:
            title = data.get('title')
            word = Word_Sentiment_Tweets("trump")
            rp , rn = word.get_Sentiment()
            return {"rp": rp,
            "rn": rn}

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
    

