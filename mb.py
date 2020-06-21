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
      
        

class Analysis(Resource):
     def __init__(self):
        self.tc = Word_Sentiment_Tweets("trump")
     def get(self, word):
        return self.tc.get_Sentiment()
        #return "Hello World!"


api.add_resource(Analysis,'/word')


if __name__ == "__main__":
    app.run()
    

