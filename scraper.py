import requests
from bs4 import BeautifulSoup
import json

URL = 'https://dev-test.hudsonstaging.co.uk/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

all_items = soup.find_all('div', class_=['product-tile', 'product-til'])
items = []

for product in all_items:
    name = product.find('p', class_='product-name').text
    image = product.img['src']
    details = product.find('div', class_='details')
    details_array = details.find_all('p')
    quantity = int(details_array[0].text.replace('Quantity: ', ''))
    raw_price = details_array[1].text.replace('Price: $', '')

    def fix_price(price):
        try:
            return int(price)
        except ValueError:
            return float(price)

    price = fix_price(raw_price)
    
    record = {"product":name,"metadata":{"image_url":image, "quantity":quantity, "price":price}}
    items.append(record)

with open('results.json', 'w', encoding='utf-8') as write_file:
    output = json.dumps(items, indent=2, separators=(',', ': '))
    write_file.write(output)
    
