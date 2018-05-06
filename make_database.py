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

##flips through whole book and grabs all text into a list
def get_all_text(url):
    i = 0
    no_error = True
    book_list = []

    while no_error is True:
        
        url = url.replace("D0." + str(i), "D0." + str(i+1))
        soup = get_soup(url)

        
        if "D0." + str(i + 1) in url:
            print("Getting: " + url + "\n\n")
            page_text = get_body(soup)

            ##temporary until i find how to check for blank
            if i is 24:
                no_error = False
            
            book_list.extend(tokenize_sentences(page_text))
            print("apended")
            
        i = i + 1
        print("D0." + str(i))
        print(url + "\n\n")
            
    return book_list



##test
url = "http://www.ulukau.org/elib/cgi-bin/library?e=d-0ks4-000Sec--11haw-50-20-frameset-book--1-010escapewin&a=d&d=D0.1&toc=0"

text = get_all_text(url)
print(text)

for e in text:
    print(e + "\n")
