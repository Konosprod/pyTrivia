#!/usr/bin/python

from BeautifulSoup import BeautifulSoup
import urllib2

def packString(line):
    ret = ""
    
    for s in line.contents:
        if s.__class__.__name__ == "Tag":
            ret += s.text
        else:
            ret += s

        
    return ret

def getContent():
    ret = ""
    
    #print("Getting Wikipedia's page...")

    reponse = urllib2.urlopen("http://fr.wikipedia.org")
    page_source = reponse.read()

    html = BeautifulSoup(str(page_source))

    entries = html.find('div', id="mf-SaviezVous").findAll('li')

    for line in entries:
        ret += "- " + packString(line) + "\n"
        
    return ret


        
