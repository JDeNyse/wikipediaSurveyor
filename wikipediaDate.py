# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 12:32:25 2020

@author: John
"""

import requests

NUMBER_OF_ARTICLES = 50

file = open("articles.txt", "r", encoding="utf-8")
outputFile = open("dates.txt", "a", encoding="utf-8")
for x in range(NUMBER_OF_ARTICLES): 
    articleName = file.readline()
    articleName = articleName.rstrip('\n')
    articleName = articleName.replace("%2C",",")
    articleName = articleName.replace("&", "%26")
    response = requests.get("https://en.wikipedia.org/w/api.php?action=query&prop=revisions&rvlimit=1&rvprop=timestamp&rvdir=newer&format=json&titles="+articleName).json()
    
    
    #print(response["continue"]["rvcontinue"])
    jobj = list(response["query"]["pages"].values())
    jdict = jobj[0]
    jfinal = jdict["revisions"]
    date = str(jfinal[0])
    formattedDate = date[15:35]
    #print(jstr[15:25])    
       # print(response["query"]["pages"][x]["revisions"]["timestamp"])
    #date = response["continue"]["rvcontinue"]
    #formattedDate = date[:4] + "-" + date[4:6] + "-" + date[6:8]
    
    outputFile.write(formattedDate)
    outputFile.write("\n")

print("done")
file.close()
outputFile.close()