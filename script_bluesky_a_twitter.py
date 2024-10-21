import asyncio
from playwright.async_api import async_playwright
from TwitterPost.TwitterCredentialsManager import get_credentials
from TwitterPost.TwitterPostManager import login, tweet


async def main():
    credentials = get_credentials()
    async with async_playwright() as p:
        browser = p.chromium.launch(headless=True)
        login(credentials, browser)
