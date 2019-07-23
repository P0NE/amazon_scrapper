import csv
import asyncio
import requests
import os
import yagmail
import keyring
from dotenv import load_dotenv
from bs4 import BeautifulSoup

load_dotenv()
yagmail.register(os.getenv('EMAIL_ADDRESS'),
                 os.getenv('EMAIL_PASSWORD'))


@asyncio.coroutine
def check_price(check):

    page = requests.get(check['url'], headers={
                        "User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'})
    soup = BeautifulSoup(page.content, 'html.parser')
    price = soup.find(id="price_inside_buybox").get_text()

    if price < check['price']:
        yagmail.SMTP(os.getenv('EMAIL_ADDRESS')).send(
            check['mail'], 'Price LOWER !!!!', 'The price for {0} is lower than wanted !!!!'.format(check['url']))


@asyncio.coroutine
def main():
    yield from asyncio.wait([check_price(scrapp) for scrapp in scrapping_dict])


with open('check.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    key = ['mail', 'url', 'price']
    scrapping_dict = []
    for row in reader:
        scrapping_dict.append(dict(zip(key, row)))
csvFile.close()


print(scrapping_dict)
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
