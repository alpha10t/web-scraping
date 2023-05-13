#Use this to save output using python name.py > output.txt
#set PYTHONIOENCODING=utf-8
#set PYTHONLEGACYWINDOWSSTDIO=utf-8

import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(r"E:\\abc\\chromedriver.exe")

driver.get("https://www.brainyquotes.com/quotes/arthur_ashe_371527/")

time.sleep(10)
last_page_element = driver.find_element(By.XPATH , '//*[@id="site-content"]/div[2]/main/div[2]/div/div[3]/div/div/nav/div/a[4]')
last_page = int(last_page_element.text)

for page in range(last_page):
    print("Current Page: ", page)
    print('\n\n\n')
    time.sleep(10)
    next_button = driver.find_element(By.XPATH, "//a[@aria-label='Next']")
    next_button.click()

driver.quit()


"""
from selenium import webdriver
import time
#import urllib.request


def download_image(file_name):
    #Add file extension to filename
    file_name += '.png'
    print(file_name)
    with open(file_name,'wb') as file:
        a = browser.find_element_by_class_name('quoteContent')
        file.write(a.screenshot_as_png)
    print('File Saved', file_name)


website = "https://www.brainyquotes.com/quotes/arthur_ashe_371527/"

#Get number of images to be downloaded from user
number_of_images_to_download = int(input("How many images you wanna download? "))
print(number_of_images_to_download)
browser = webdriver.Firefox()
browser.maximize_window()
browser.get(website)
#string_name = "Image" + str(1)
#download_image(string_name)


for x in range(number_of_images_to_download):
    time.sleep(30)
    string_name = "Image" + str(x)
    print("Saving File:",)
    download_image(string_name)
    #Click next quote
    browser.find_element_by_css_selector('.bq-fa-sh-sm-r').click()



print("Starting to close now...")
"""