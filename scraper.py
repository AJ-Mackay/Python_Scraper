### To Do ###
# Get Data from Website
# Format data
# Save as JSON
import requests
from bs4 import BeautifulSoup

URL = 'https://dev-test.hudsonstaging.co.uk/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
print(soup)
print('-----')

all_items = soup.find_all('div', class_=['product-tile', 'product-til'])

for products in all_items:
    name = products.find('p', class_='product-name').text
    image = products.img['src']
    details = products.find('div', class_='details')
    details_array = details.find_all('p')
    quantity = details_array[0].text.replace('Quantity: ', '')
    price = details_array[1].text.replace('Price: $', '')
    print('Product Name:', name)
    print('Image Source:', image)
    print('Quantity:', quantity)
    print('Price:', price)
    print('-----')
