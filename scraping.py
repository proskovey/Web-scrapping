from bs4 import BeautifulSoup
import requests

KEYWORDS = ['дизайн', 'фото', 'web', 'python']

def find_words(text: str, words):
    for i in words:
        if i in text.lower():
            return True
    return False    

def get_posts(words: list = False):
    resp = requests.get('https://habr.com/ru/all/').text
    soup = BeautifulSoup(resp, 'lxml')
    titles: list[BeautifulSoup] = soup.find_all(class_='tm-article-snippet__title-link')

    rtn = []
    for i in titles:
        href = 'https://habr.com' + i.get('href')
        titles = i.text
        rtn.append((href, titles))

    return list(filter(lambda x: find_words(x[1], words), rtn)) if words else rtn

print(get_posts(KEYWORDS))  