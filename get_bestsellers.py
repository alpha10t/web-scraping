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

driver.get("https://www.amazon.in/gp/bestsellers/?ref_=nav_cs_bestsellers")

# print(driver.page_source)
soup = BeautifulSoup(driver.page_source, 'html.parser')

sections = soup.find_all('div', class_='a-section a-spacing-large')

#products = soup.find_all('div', class_='zg-carousel-general-faceout')

# sections: a-section a-spacing-large
# Gather title (find_all('h2', class_='a-carousel-heading a-inline-block'))  
# --> Gather products (find_all('div', class_='zg-carousel-general-faceout'))

#for i in div_tags:
#    print(i.text)

for i in tqdm(sections):
    gather_title = i.find('h2', class_='a-carousel-heading a-inline-block')
    print('\n'+ gather_title.text)
    print('\n')
    product_list_in_section = i.find_all('div', class_='zg-carousel-general-faceout')
    for j in product_list_in_section:
        print(j.text)
    print('\n\n\n')
    time.sleep(5)

#product 1: zg-carousel-general-faceout
#product 2: zg-carousel-general-faceout

driver.quit()