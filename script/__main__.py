import csv
import asyncio
import requests
from bs4 import BeautifulSoup


@asyncio.coroutine
def check_price(check):

    # header = {
    #     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
    # page = requests.get(check['url'], headers=header)
    # soup = BeautifulSoup(page.content, 'html.parser')
    print(check)


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
