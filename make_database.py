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
    working = True
    book_list = []

    while nworking is True:
        
        ##updates the index by 1, the gets soup
        url = url.replace("D0." + str(i), "D0." + str(i+1))
        soup = get_soup(url)

        ##if on the correct index
        if "D0." + str(i + 1) in url:
            print("Getting: " + url + "\n\n")
            page_text = get_body(soup)
            print("Length: " + str(len(page_text)))

             ##checks if the string is empty, this is what it does when there's no text.
            if len(page_text) is 2:
                working = False
                
            ##add the goods
            book_list.extend(tokenize_sentences(page_text))
            print("apended")
            
        i = i + 1
        print("D0." + str(i))
        print(url + "\n\n")
            
    return book_list



##test
url = input("URL: ")

text = get_all_text(url)
print(text)

for e in text:
    print(e + "\n")
