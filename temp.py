# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import requests

url="https://www.newegg.com/global/in-en/samsung-galaxy-z-flip-3-5g-6-7-black/p/N82E16875168090?Description=samsung%20galaxy%20z%20flip%203%205g&cm_re=samsung_galaxy%20z%20flip%203%205g-_-75-168-090-_-Product&quicklink=true"

page=requests.get(url)

from bs4 import BeautifulSoup

soup= BeautifulSoup(page.content, "html.parser")

price = soup.find_all('div', attrs={"class":"price-current"})[0].get_text() 
