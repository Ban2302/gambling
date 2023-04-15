from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.ceneo.pl/Smartfony').text
soup = BeautifulSoup(html_text, 'lxml')
phones = soup.find_all('div', class_ = 'cat-prod-row js_category-list-item js_clickHashData js_man-track-event   ')
for phone in phones:
    phone_name = soup.find('span', class_ = 'font-bold')
    print (phone_name)