from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from collections import Counter

SERVICE_PATH = "C:\Program Files (x86)\chromedriver.exe"
service = Service(SERVICE_PATH)
options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(service=service, options=options)

count = 0

while True:
    if count == 0:
        url = input('Please provide a url:  ')
        count += 1
    try:
        driver.get(url)
        words = {}
        word_list = driver.find_element(By.XPATH, "/html/body").get_attribute("textContent").split()
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