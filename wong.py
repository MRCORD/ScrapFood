import requests
from bs4 import BeautifulSoup
from scrapy import Selector
import re

url = "https://www.wong.pe/frutas-y-verduras"
req = requests.get(url).content
sel = Selector(text = req)

lista = []
def extrae(x):
    data= sel.xpath(x)
    for i in data:
        append




'//a[@class="product-item__name"]/text()'

"""
<div class="product-item__info">
		
		<a href="https://www.wong.pe/acelga-don-miguel-bolsa-300-g-4162/p" class="product-item__name" title="Acelga Don Miguel Bolsa 300 g">Acelga Don Miguel Bolsa 300 g</a>
		
		<div class="product-item__brand">Don Miguel</div>
		<div class="product-item__description" style="display: none"></div>
		
		<label class="product-item__compare product-compare">
			<input type="checkbox" name="prod-compare-checkbox" class="product-compare__input">
			<div class="font-icn check"></div>
			<span class="product-compare__text">Comparar</span>
		</label>
	</div>
    """