from csv import reader
import csv
import json
from sklearn.pipeline import Pipeline
import pickle
from sklearn.externals import joblib
import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from Sentiment import Sentiment
from Tweet import Tweet


class Word_Sentiment_Tweets:
    def __init__(self, word):
        self.word=word

    
    def get_Sentiment(self ):


        tweets = []
        file_name = 'training.txt'



        f=open(file_name,"r", encoding="utf8")
        lines=f.readlines()

        for x in lines:
            tweets.append(Tweet(x.split('\t')[1],x.split('\t')[0]))
        f.close()
         
        train_xx = [x.text for x in tweets]
        train_yy = [x.sentiment for x in tweets]

        clf = joblib.load('clf087.pkl')

        
        vectorizer = CountVectorizer()

        train_xxx_vectors = vectorizer.fit_transform(train_xx)
        

        tests = []
        file_name = 'train.csv'

        with open(file_name, 'r') as f:
         # pass the file object to reader() to get the reader object
             csv_reader = reader(f)
      # Iterate over each row in the csv using reader object
             for row in csv_reader:
        # row variable is a list that represents a row in csv
        #print(row)
        #print(row[2])
                         tests.append(row[2])
        

        good = vectorizer.transform(tests)



        word = self.word
        ls = []
        Tw = []
       #read csv, and split on "," the line
        csv_file = csv.reader(open('train.csv', "r"), delimiter=",")


       #loop through csv list
        for row in csv_file:
      #if current rows 2nd value is equal to input, print that row
             if word in row[2]:
                    Sent = clf.predict(good[int(row[0])])
        #print(str(row[0]) + str(clf.predict(good[int(row[0])]))
                    print("Tweet: %(n)s \nSentiment: %(s)s" % {'n': row[2], 's': Sent})
                    ls.append(Sent[0])
                    Tw.append(row[2])
        
        respp =0
        resnn = 0
        pos = 0
        neg = 0
        for i in range(0,len(ls)):
           if ls[i] == 'NEGATIVE':
               neg+=1
           if ls[i] == 'POSITIVE':
               pos+=1
        if len(ls)>0 :
            respp = (pos / len(ls))*100
            resnn = (neg / len(ls))*100
            resp = round(respp, 2)
            resn = round(resnn, 2)

        #print(resp)
        #print(resn)
        return Tw, ls,resp, resn

