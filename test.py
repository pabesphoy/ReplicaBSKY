from TwitterCredentialsManager import get_credentials
from atproto import Client
from ntscraper import Nitter

scrapper = Nitter(log_level=1, skip_instance_check=False)

for tweet in scrapper.get_tweets(get_credentials()['twitter_user'], mode='user', number=10)['tweets']:
    print(tweet['text'])

