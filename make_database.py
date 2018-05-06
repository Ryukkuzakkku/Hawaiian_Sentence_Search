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
    soup = get_soup(url)
    page_text = get_body(soup)
    book_list = []
    
    if len(page_text) is not 2:
        book_list.extend(tokenize_sentences(page_text))
            
    return book_list


'''
TODO
*Add add_to_database (Takes sentence and adds it to database, organizing it by number, url, book name and sentence itself)
(Go through list, get all links. On every link, look at the links on page, and find one ending in D0&TOC=0)

*Add get_all_data (traverses all books from the search and adds it in the database)
'''

##test
url = input("URL: ")

text = get_all_text(url)
print(text)

for e in text:
    print(e + "\n")
