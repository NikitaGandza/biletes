from bs4 import BeautifulSoup
import requests

url = 'https://www.bilesuparadize.lv/lv/search'

page = requests.get(url)

print(page.status_code)