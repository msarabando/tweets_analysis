'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt

#Get the JSON data
tweetFile = open("./tweets.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

# Continue your program below!

for tweets in tweetData:
    tb = TextBlob(tweets["text"])
    print(tb.polarity)
