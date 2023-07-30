from urllib import request
from bs4 import BeautifulSoup
from collections import Counter

count = 0

while True:
    if count == 0:
        url = input('Please provide a url:  ')
        count += 1
    try:
        html = request.urlopen(url=url).read()
        soup = BeautifulSoup(html, 'html.parser')
        words = {}
        raw_word_list = []
        word_list = []
        print(soup.body.string)
        for string in soup.body.strings:
            raw_word_list.append(string.split())
        for w in raw_word_list:
            if type(w) == list:
                for d in w:
                    word_list.append(d)
            else:
                word_list.append(w)
        n_words = Counter(word_list)
        for word, value in n_words.items():
            words[word.lower()] = value
        action = input('Please select an action\n(s-stop,  r-reset url or pass a word to count[start with "\\" or "/" to search for stop & reset])\t')
        if action.lower() == 'stop':
            break
        elif action.lower() == 'reset':
            count = 0
        else:
            if action.startswith("/") or action.startswith("\\"):
                action = action[1:]
            if action.lower() in words.keys():
                print(f"The word {action} occurred {words[action]} times")
            else:
                print(f"The word {action} was not used in this page")
    except:
        print("Error getting url. Please input a valid url or check your internet connection")
        count = 0