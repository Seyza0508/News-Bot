from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from time import sleep


def getNews(topic):
    # creating the webdriver object instance
    driver = webdriver.Chrome()
    driver.get(f"http://www.google.com/search?q={topic}+News")
    # This will hold titles text
    titles = driver.find_elements(
        By.CSS_SELECTOR, "div.n0jPhd.ynAwRc.tNxQIb.nDgy9d")
    file = open("title.txt", "w")
    for title in titles:
        file.write(f"{title.text}\n")
    file.close()
    
    driver.close()
    
def main():
    # This will search news based on given args that we give it
    getNews('Tech')
    
main()