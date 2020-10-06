# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 14:24:33 2020

@author: John
"""
import requests
import json

NUMBER_OF_ARTICLES = 50
response = requests.get("https://en.wikipedia.org/w/api.php?action=query&list=random&rnnamespace=0&rnlimit="+str(NUMBER_OF_ARTICLES)+"&format=json").json()
random = response["query"]["random"]
#print(random[0]["title"])

file = open("articles.txt", "a")

for x in range(NUMBER_OF_ARTICLES):
    with open("articles.txt", "a", encoding="utf-8") as file:
        file.write(random[x]["title"])
        file.write("\n")
    