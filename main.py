from atproto import Client
import time
from ntscraper import Nitter
import random
scraper = Nitter() 

twitter_user = input("Introduce tu @ de Twitter: ")
bsky_user = input("Introduce tu usuario de Bluesky (BSKY): ")
password = input("Introduce tu contraseña de Bluesky: ")

replicatedTweets = set()


print(f"Twitter: {twitter_user}, BSKY: {bsky_user}, Contraseña: {'*' * len(password)}")
client = Client()
client.login(bsky_user, password)

while True:
    tweets = scraper.get_tweets(twitter_user, mode='user', number=1)
    for tw in tweets['tweets']:
        if tw['text'] not in replicatedTweets:
            replicatedTweets.add(tw['text'])
            print('Tweet recogido: ' + tw['text'])
            client.send_post(tw['text'])
            print('Replicando tweet: ' + tw['text'])
    time.sleep(random.randint(60, 120))

