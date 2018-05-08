import requests
import sqlite3
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

def seperate_sentences(text):
    pass

##flips through whole book and grabs all text into a list
def get_all_text(url):
    create_database()
    soup = get_soup(url)
    page_text = get_body(soup)
    book_list = []
    
    if len(page_text) is not 2:
        page_text = page_text.replace("\n", ". ")
        book_list.extend(tokenize_sentences(page_text))

    i = 1
    book_name = soup.title.string.replace("Ulukau: ", "")
    for sentence in book_list:
        insert_data(sentence, i, url, book_name)
        i = i + 1
            
    return book_list


def create_database():
    db = sqlite3.connect('data/sentences.db')
    cursor = db.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS sentences(id INTEGER PRIMARY KEY, id_in_book INTEGER,
                    sentence TEXT, source_url TEXT, book_name TEXT)''')
    db.commit()
    db.close()

def insert_data(sentence, number, source_url, book_name):
    db = sqlite3.connect('data/sentences.db')
    cursor = db.cursor()
    cursor.execute('''INSERT INTO sentences(sentence, id_in_book, source_url, book_name)
                                    VALUES(?,?,?,?)''', (sentence, number, source_url, book_name))
    db.commit()
    db.close()
    
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
