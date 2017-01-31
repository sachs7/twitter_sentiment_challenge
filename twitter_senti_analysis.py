import tweepy
from textblob import TextBlob
import csv
import pygal


def set_up():
    consumer_key = 'CONSUMER_KEY_HERE'

    consumer_secret = 'CONSUMER_SECRET_HERE'

    access_token = 'ACCESS_TOKEN_HERE'
    access_token_secret = 'ACCESS_TOKEN_SECRET_HERE'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    return tweepy.API(auth)


def analyse_tweets(search_item):
    positive_count, negative_count, neutral_count = (0, 0, 0)

    public_tweets = set_up().search(search_item, count=100)

    with open('twitter_sentiment.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["Sl.No", "Author", "Tweets", "Tweet_Type"])

        for i, tweets in enumerate(public_tweets):

            analysis = TextBlob(tweets.text)

            author = tweets.user.screen_name

            tweet = tweets.text

            if analysis.sentiment.polarity > 0:
                positive_count += 1
                f.write(str(i) + "," + author + ',' + tweet + ',' + 'Positive')
                f.write('\n')
            elif analysis.sentiment.polarity == 0:
                neutral_count += 1
                f.write(str(i) + "," + author + ',' + tweet + ',' + 'Neutral')
                f.write('\n')
            else:
                negative_count += 1
                f.write(str(i) + "," + author + ',' + tweet + ',' + 'Negative')
                f.write('\n')

    return positive_count, negative_count, neutral_count


if __name__ == '__main__':
    search_term = 'Trump'
    p_count, neg_count, neu_count = analyse_tweets(search_term)
    # print(p_count, neg_count, neu_count)
    p = pygal.Pie(inner_radius=0.4)
    p.title = 'Tweets based on search term: ' + str(search_term) + ' (in %)'
    p.add('Positive Tweets', p_count)
    p.add('Neutral Tweets', neu_count)
    p.add('Negative Tweets', neg_count)
    p.render()
    p.render_to_file('tweets.svg')
