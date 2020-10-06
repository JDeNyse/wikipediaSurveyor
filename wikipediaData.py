# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 22:13:26 2020

@author: John
"""

import requests

NUMBER_OF_ARTICLES = 50

file = open("articles.txt", "r", encoding="utf-8")
outputFile = open("properties.txt", "a", encoding="utf-8")
for x in range(NUMBER_OF_ARTICLES):   
    articleName = file.readline()
    articleName = articleName.rstrip('\n')
    articleName = articleName.replace("%2C",",")
    
    response = requests.get("https://www.wikidata.org/w/api.php?action=wbgetentities&sites=enwiki&titles="+articleName+"&props=descriptions&languages=en&format=json").json()
    
    wikidataQ = response["entities"].keys()
    wikidataQ = str(wikidataQ).replace("dict_keys(['", "")
    wikidataQ = wikidataQ.rstrip("'])")
    print(str(wikidataQ))
    
    #wikidataQ = "Q213812"    
    
    wikidataResponse = requests.get("https://www.wikidata.org/w/api.php?action=query&titles="+wikidataQ+"&generator=links&gplnamespace=0&gpllimit=100&prop=pageterms&wbptterms=label&format=json").json()
    otherWikidataResponse = requests.get("https://www.wikidata.org/w/api.php?action=wbgetclaims&format=json&props=value&entity="+wikidataQ).json()
    female = False
    male = False
    living = True
    person = False
    sport = False
    if len(wikidataResponse) == 1:
        outputFile.write("TODO \n")   
    else:
        for x in wikidataResponse["query"]["pages"]:
            #print(wikidataResponse["query"]["pages"][x])
            if wikidataResponse["query"]["pages"][x]["title"] == "Q5":
                person = True
                if wikidataResponse["query"]["pages"][x]["title"] == "Q6581072":
                    female = True
                elif wikidataResponse["query"]["pages"][x]["title"] == "Q6581097":
                    male = True            
            for y in otherWikidataResponse["claims"]:      
                print(y)
                if y == "P570":
                    living = False
                if y == "P641":
                    sport = True
                    
        if(person):
            if(living):
                outputFile.write("BLP")
            else:
                outputFile.write("BDP")
            if(male):
                outputFile.write(", M")
            elif(female):
                outputFile.write(", F")
            if(sport):
                outputFile.write(", S")
            outputFile.write("\n")
        else:
            outputFile.write("TODO \n")    
            
file.close()
outputFile.close()          
         
