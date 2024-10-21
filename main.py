import asyncio
from playwright.async_api import async_playwright
from TwitterCredentialsManager import get_credentials
from TwitterPostManager import login, tweet
from atproto import Client
import time
from ntscraper import Nitter
import random


client = Client()
credentials = get_credentials()
client.login(credentials['bsky_user'], credentials['bsky_password'])


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()
        posts_replicados = []
        scrapper = Nitter()
        await login(page, credentials)
        last_tweet = getLastTweet(scrapper)
        last_bpost = get_latest_post()
        while(True):
            '''
            #Este codigo subnormal de mierda coge el tuit que le da la puta gana
            my_tweet = getLastTweet(scrapper)
            print('Ultimo tweet: ', my_tweet['text'])
            if my_tweet['text'] != last_tweet['text'] and my_tweet['text'] not in posts_replicados:
                client.send_post(my_tweet['text'])
                print('Replicando tweet')
                posts_replicados.append(my_tweet['text'])
            '''
                

            bpost = get_latest_post()
            print('Ultimo bpost: ', bpost)
            if bpost != last_bpost and bpost not in posts_replicados:
                await tweet(page, bpost)
                print('Replicando bpost')
                posts_replicados.append(bpost)

            time.sleep(random.randint(60, 120))

    
def getLastTweet(scraper):
    return scraper.get_tweets(credentials['twitter_user'], mode='user', number=1)['tweets'][0]


def get_latest_post():
    return client.get_author_feed(actor=credentials["bsky_user"], limit=1).feed[0].post.record.text
    
    
    

asyncio.run(main())
