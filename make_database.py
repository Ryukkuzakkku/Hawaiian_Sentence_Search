import requests
from bs4 import BeautifulSoup
import nltk

##grabbers

def get_soup(url):
    r = requests.get(url)
    return BeautifulSoup(r.content, 'html.parser')

def get_body(soup):
    elems = soup.findAll("p")
    return BeautifulSoup(str(elems), "html.parser").text

def tokenize_sentences(text):
    return nltk.sent_tokenize(text)
    
##crawlers



##test
soup = get_soup("http://www.ulukau.org/elib/cgi-bin/library?e=d-0ks4-000Sec--11haw-50-20-frameset-book--1-010escapewin&p=frameset&toc=0&d=D0.8")

text = get_body(soup)

for e in tokenize_sentences(text):
    print(e + "\n")
