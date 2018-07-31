list=[]
list2=[]
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
    #print(tb.polarity)
    list.append(tb.polarity)
    list2.append(tb.subjectivity)

bin_edges = [-1,-0.5, 0, 0.5, 1]
plt.hist(list, bins=bin_edges)
plt.xlabel("polarity")
plt.ylabel("tweets")
plt.show()

bin_edges = [-1,-0.5, 0, 0.5, 1]
plt.hist(list2, bins=bin_edges)
plt.xlabel("subjectivity")
plt.ylabel("tweets")
plt.show()
