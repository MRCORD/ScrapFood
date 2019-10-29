import requests
from bs4 import BeautifulSoup
from scrapy import Selector
import re

url = 'https://www.plazavea.com.pe/frutas-y-verduras/frutas/'
req = requests.get(url).content
sel = Selector(text = req)

#soup = BeautifulSoup(req, 'html.parser')


lista =[]
path = '//div[@class="Showcase__content"]/@title'


data = sel.xpath(path).getall()

for i in data:
    result = data
    lista.append(result)

