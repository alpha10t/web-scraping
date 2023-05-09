from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#options = Options()
#options.headless = True

driver = webdriver.Chrome(r"E:\\abc\\chromedriver.exe")

#driver.get("https://www.imdb.com/title/tt0068646")
driver.get("https://www.imdb.com/title/tt0111161/")

soup = BeautifulSoup(driver.page_source, 'html.parser')

link = soup.find('a', {'class': 'ipc-lockup-overlay'})['href']

url = "http://www.imdb.com" + link
print(url)

driver.get(url)


soup = BeautifulSoup(driver.page_source, 'html.parser')

img_tag = soup.find('img', class_='sc-7c0a9e7c-0 fEIEer')
img_url = img_tag['src']

print(img_url)


driver.quit()