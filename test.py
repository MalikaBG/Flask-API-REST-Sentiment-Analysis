from TweetClassifier import Word_Sentiment_Tweets
from Tweet import Tweet
from Sentiment import Sentiment

class Tweet:
    def __init__(self, text, score):
        self.text = text
        self.score = score
        self.sentiment = self.getSentiment()
    def getSentiment(self):
        if self.score == "0":
            return Sentiment.NEGATIVE
        
        elif self.score == "1":
            return Sentiment.POSITIVE

word = Word_Sentiment_Tweets("trump")

tw, ls ,rp, rn = word.get_Sentiment()

print(rp)
print(rn)
print(tw)
print(ls)