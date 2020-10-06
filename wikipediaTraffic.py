# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 15:43:06 2020

@author: John
"""

import requests
file = open("articles.txt", "r", encoding="utf-8")

NUMBER_OF_ARTICLES = 49

viewsCount = []
for x in range(NUMBER_OF_ARTICLES):
    print(x)
    articleName = file.readline()
    articleName = articleName.rstrip('\n')
    articleName = articleName.replace("%2C",",")
    #print(articleName)
    response = requests.get("https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/all-agents/"+articleName+"/daily/20200801/20200831").json()
    sum = 0  
    print(response["items"])
    for z in response["items"]:
        print(z["views"])
        sum += z["views"]
   # viewsCount.append(response["items"][0]["views"])
    viewsCount.append(sum)
    
file.close()    
file = open("views.txt", "a", encoding="utf-8")

for y in range(NUMBER_OF_ARTICLES):
    file.write(str(viewsCount[y]))
    file.write("\n")
    
print("done")
file.close()