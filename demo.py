#Use this to save output using python name.py > output.txt
#set PYTHONIOENCODING=utf-8
#set PYTHONLEGACYWINDOWSSTDIO=utf-8

import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

i=0

def extract_hotel_info():
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    div_tags = soup.find_all('div', class_='g1qv1ctd cb4nyux dir dir-ltr')
    global i
    # Extract the text of each div tag
    for div in div_tags:
        i = i+1
        print(i)
        print(div.text + '\n')

driver = webdriver.Chrome(r"E:\\abc\\chromedriver.exe")

driver.get("https://www.airbnb.co.in/s/Hyderabad--Telangana/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=2023-06-01&monthly_length=3&price_filter_input_type=0&price_filter_num_nights=3&channel=EXPLORE&query=Hyderabad%2C%20Telangana&date_picker_type=calendar&checkin=2023-06-01&checkout=2023-06-04&adults=2&source=structured_search_input_header&search_type=autocomplete_click&place_id=ChIJx9Lr6tqZyzsRwvu6koO3k64")

time.sleep(10)
last_page_element = driver.find_element(By.XPATH , '//*[@id="site-content"]/div[2]/main/div[2]/div/div[3]/div/div/nav/div/a[4]')
last_page = int(last_page_element.text)

for page in range(last_page):
    print("Current Page: ", page)
    print('\n\n\n')
    time.sleep(10)
    extract_hotel_info()
    next_button = driver.find_element(By.XPATH, "//a[@aria-label='Next']")
    next_button.click()

driver.quit()