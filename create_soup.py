from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome(r"E:\\abc\\chromedriver.exe")
driver.get("http://python.org")
html_doc = driver.page_source

soup = BeautifulSoup(html_doc, "lxml")
print(soup.prettify())

driver.quit()