# twitter_sentiment_challenge
Twitter Sentiment Analysis Challenge for Learn Python for Data Science #2 by @Sirajology on Youtube

##Overview

This is the code for the Twitter Sentiment Analyzer challenge for 'Learn Python for Data Science #2' by @Sirajology on [YouTube](https://youtu.be/o_OZdbCzHUA). The code uses the [tweepy](http://www.tweepy.org/)  library to access the Twitter API, the [TextBlob](https://textblob.readthedocs.io/en/dev/) library to perform Sentiment Analysis on each Tweet and [Pygal] (http://pygal.org/en/stable/index.html) library to represent the results graphically. We'll be able to see how positive or negative each tweet is about whatever topic we choose. 

##Dependencies

* tweepy (http://www.tweepy.org/)
* textblob (https://textblob.readthedocs.io/en/dev/)
* pygal (http://pygal.org/)

Install missing dependencies using [pip](https://pip.pypa.io/en/stable/installing/)

##Usage

Once you have your dependencies installed via pip, run the script in terminal via

```
python twitter_senti_analysis.py
```

##Challenge

Instead of printing out each tweet, save each Tweet to a CSV file with an associated label. The label should be either 'Positive' or 'Negative'. You can define the sentiment polarity threshold yourself, whatever you think constitutes a tweet being positive/negative. Push your code repository to [github](https://help.github.com/articles/set-up-git/) then post it in the comments. I'll give the winner a shoutout a week from now!
