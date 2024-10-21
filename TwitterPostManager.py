import asyncio
from playwright.async_api import async_playwright
from TwitterCredentialsManager import get_credentials

async def login(page, credentials):

        await page.goto("https://twitter.com/login")

        await page.wait_for_selector("input[name='text']", timeout=10000)

        await page.fill("input[name='text']", credentials['twitter_user']) 
        await page.click("button[class='css-175oi2r r-sdzlij r-1phboty r-rs99b7 r-lrvibr r-ywje51 r-184id4b r-13qz1uu r-2yi16 r-1qi8awa r-3pj75a r-1loqt21 r-o7ynqc r-6416eg r-1ny4l3l']") 
        
        await page.wait_for_selector("input[name='password']", timeout=10000)
        
        await page.fill("input[name='password']", credentials['twitter_password'])  
        await page.click("button[class='css-175oi2r r-sdzlij r-1phboty r-rs99b7 r-lrvibr r-19yznuf r-64el8z r-1fkl15p r-1loqt21 r-o7ynqc r-6416eg r-1ny4l3l']") 
      

async def tweet(page, text):
    await page.click("div[class='public-DraftStyleDefault-block public-DraftStyleDefault-ltr']")
    await page.fill("div[class='public-DraftStyleDefault-block public-DraftStyleDefault-ltr']", text)
    await page.click("button[class='css-175oi2r r-sdzlij r-1phboty r-rs99b7 r-lrvibr r-1cwvpvk r-2yi16 r-1qi8awa r-3pj75a r-1loqt21 r-o7ynqc r-6416eg r-1ny4l3l']") 
    await page.click("button[class='css-175oi2r r-sdzlij r-1phboty r-rs99b7 r-lrvibr r-1cwvpvk r-2yi16 r-1qi8awa r-3pj75a r-1loqt21 r-o7ynqc r-6416eg r-1vtznih r-1ny4l3l']") 