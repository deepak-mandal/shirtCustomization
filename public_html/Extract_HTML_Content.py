# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 15:03:52 2021

@author: dkmii
"""

#importing libraries
import bs4    #BeautifulSoup
import requests
import os
#url=input("enter your URL: ")
url = "https://www.bombayshirts.com/collections/all/products/crema-stretch-satin"
response = requests.get(url)    #response after sending the url requests
print(type(response))
print(response.text)
filename = "temp.html"
bs = bs4.BeautifulSoup(response.text, "html.parser")
formatted_text = bs.prettify()
print(formatted_text)
try:
    with open(filename, "w+", encoding="utf-8") as f:    #w: write; w+ : if not then create
        f.write(formatted_text)
except Exception as e:
    print(e)