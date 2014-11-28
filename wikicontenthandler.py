#!/usr/bin/python3.3

#-*- coding: UTF-8 -*-

from bs4 import BeautifulSoup
import urllib.request

def packString(line):
    ret = ""
    
    for s in line.contents:
        if s.__class__.__name__ == "Tag":
            ret += s.text
        else:
            ret += s

        
    return ret

def getContentDidYouKnow():
    ret = ""
    
    html = getWikiSource()

    entries = html.find('div', id="mf-SaviezVous").findAll('li')

    for line in entries:
        ret += "- " + packString(line) + "\n"
        
    return ret
    
def getWikiSource():
  
    reponse = urllib.request.urlopen("http://fr.wikipedia.org")
    pageSource = reponse.read()
    
    return BeautifulSoup(pageSource.decode("utf8"))
    
    
    
def getContentLightOn():
    ret = ""
    
    html = getWikiSource()
    
    entries = html.find('div', id="mf-lumieresur").findAll('p')
    
    for l in entries:
        ret += l.text
    
    return ret

def main():
    getContentLightOn()
    
if __name__ == "__main__":
    main()
    



        
