#Use this to save output using python name.py > output.txt
#set PYTHONIOENCODING=utf-8
#set PYTHONLEGACYWINDOWSSTDIO=utf-8

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from tqdm import tqdm
import time
#options = Options()     
#options.headless = True

driver = webdriver.Chrome(r"E:\\abc\\chromedriver.exe")
driver.maximize_window()

driver.get("https://www.amazon.in/gp/bestsellers/?ref_=nav_cs_bestsellers")

time.sleep(20)
# print(driver.page_source)
soup = BeautifulSoup(driver.page_source, 'html.parser')

sections = soup.find_all('div', class_='a-section a-spacing-large')

#products = soup.find_all('div', class_='zg-carousel-general-faceout')

# sections: a-section a-spacing-large
# Gather title (find_all('h2', class_='a-carousel-heading a-inline-block'))  
# --> Gather products (find_all('div', class_='zg-carousel-general-faceout'))

# div class for title extraction: p13n-sc-truncate-desktop-type2  p13n-sc-truncated
# i class for rating extraction: a-icon a-icon-star-small a-star-small-3-5 aok-align-top
#   --> span class: a-icon-alt (contains ratings)
#   --> span class: a-size-small (contains number of reviews)
# div class for price extraction (a-row)

for i in sections:
    print(i)
    print('\n\n\n')
    """
    title = i.find('div', class_ = 'p13n-sc-truncate-desktop-type2  p13n-sc-truncated')
    rating = i.find('i', class_ = 'a-icon a-icon-star-small a-star-small-3-5 aok-align-top')
    price = i.find('div', class_ = 'a-row')
    print(title.text)
    print(rating.text)
    print(price.text)
    """
"""
for i in tqdm(sections):
    gather_title = i.find('h2', class_='a-carousel-heading a-inline-block')
    print('\n'+ gather_title.text)
    print('\n')
    product_list_in_section = i.find_all('div', class_='zg-carousel-general-faceout')
    for j in product_list_in_section:
        print(j.text)
    print('\n\n\n')
    time.sleep(5)
"""

#product 1: zg-carousel-general-faceout
#product 2: zg-carousel-general-faceout

driver.quit()