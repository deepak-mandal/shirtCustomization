# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 07:34:05 2021

@author: dkmii
"""

#importing libraries
import bs4    #BeautifulSoup
import requests
import shutil
import os
#url=input("enter your URL: ")
url = "https://www.bombayshirts.com/collections/all/products/crema-stretch-satin"
response = requests.get(url)    #response after sending the url requests
print(type(response))
print(response.text)

bs = bs4.BeautifulSoup(response.text, "html.parser")




list_imgs = bs.find_all("img")
print(list_imgs)

no_of_imgs = len(list_imgs)
print("number of img tags ", no_of_imgs)



try:
    os.mkdir(os.path.join(os.getcwd(), "img"))
except:
    pass
os.chdir(os.path.join(os.getcwd(), "img"))


j = 1
for imgTag in list_imgs:
    #print(imgTag)
    try:
        imgLink = imgTag.get("src")
        print(imgLink)
    
        #for image extention
        ext = imgLink[imgLink.rindex('.'): ]
        if ext.startswith(".png"):
            ext=".png"
        elif ext.startswith(".jpeg"):
            ext = ".jpeg"
        elif ext.startswith(".jpg"):
            ext=".jpg"
        elif ext.startswith(".svg"):
            ext=".svg"
        
        #print(ext)
        filen = str(j)+ext
        res = requests.get(imgLink, stream = True)
        
        with open(filen, "wb") as file:
            shutil.copyfileobj(res.raw, file)
    except Exception as e:
        print(e)
            
    j+=1

print(j)