import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(r"E:\\abc\\chromedriver.exe")

driver.get('http://quotes.toscrape.com/')
i = 0
authors = driver.find_elements(By.CLASS_NAME , 'author')
quotes = driver.find_elements(By.CLASS_NAME, 'text')

for author in authors:
    i=i+1
    print(i, author.text) 
    print(quotes[i-1].text)
    print('\n')

#With BeautifulSoup

soup = BeautifulSoup(driver.page_source, 'html.parser')

quotes = soup.find_all('div', class_='quote')
"""
for quote in quotes:
    i = i+1
    print(i)
    quote_text = quote.find('span', class_='text')
    print(quote_text.text)
    quote_author = quote.find('small', class_='author')
    print(quote_author.text + '\n')

time.sleep(20)
"""
driver.quit()