#https://www.airbnb.co.in/s/Hyderabad--Telangana/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=2023-06-01&monthly_length=3&price_filter_input_type=0&price_filter_num_nights=3&channel=EXPLORE&query=Hyderabad%2C%20Telangana&date_picker_type=calendar&checkin=2023-06-01&checkout=2023-06-04&adults=2&source=structured_search_input_header&search_type=autocomplete_click&place_id=ChIJx9Lr6tqZyzsRwvu6koO3k64
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

i=0
page = 0

def click_next_page():
    element = driver.find_element(By.XPATH , '//*[@id="site-content"]/div[2]/main/div[2]/div/div[3]/div/div/nav/div/a[5]')
    #//*[@id="site-content"]/div[2]/main/div[2]/div/div[3]/div/div/nav/div/a[6]
    element.click()
    time.sleep(10)
    

def extract_hotel_info():
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    div_tags = soup.find_all('div', class_='g1qv1ctd cb4nyux dir dir-ltr')
    global i
    print("Current Page: ", page, "Last Page", last_page)
    # Extract the text of each div tag
    for div in div_tags:
        i = i+1
        print(i)
        print(div.text + '\n')

#options = Options()
#options.headless = True

driver = webdriver.Chrome(r"E:\\abc\\chromedriver.exe")

driver.get("https://www.airbnb.co.in/s/Hyderabad--Telangana/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=2023-06-01&monthly_length=3&price_filter_input_type=0&price_filter_num_nights=3&channel=EXPLORE&query=Hyderabad%2C%20Telangana&date_picker_type=calendar&checkin=2023-06-01&checkout=2023-06-04&adults=2&source=structured_search_input_header&search_type=autocomplete_click&place_id=ChIJx9Lr6tqZyzsRwvu6koO3k64")

time.sleep(10)
last_page_element = driver.find_element(By.XPATH , '//*[@id="site-content"]/div[2]/main/div[2]/div/div[3]/div/div/nav/div/a[4]')
last_page = int(last_page_element.text)

for page in range(last_page):
    print("Current Page: ", page)
    print('\n\n\n')
    extract_hotel_info()
    click_next_page()

#extract_hotel_info()
#last page number
#//*[@id="site-content"]/div[2]/main/div[2]/div/div[3]/div/div/nav/div/a[4]
#element = driver.find_element(By.XPATH , '//*[@id="site-content"]/div[2]/main/div[2]/div/div[3]/div/div/nav/div/a[4]')
driver.quit()