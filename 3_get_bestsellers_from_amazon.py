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
    print('\n\n')
    gather_title = i.find('h2', class_='a-carousel-heading a-inline-block')
    print(gather_title.text + '\n')
    title = i.find_all('div', class_ = 'p13n-sc-truncate-desktop-type2 p13n-sc-truncated')
    
    for j in title:
        print(j.text)
        rating = i.find('i', class_ = 'a-icon a-icon-star-small a-star-small-4-5 aok-align-top')
        print(rating.text)
        price = i.find('span', class_ = '_cDEzb_p13n-sc-price_3mJ9Z')
        print(price.text)
        print('\n')



driver.quit()