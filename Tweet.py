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