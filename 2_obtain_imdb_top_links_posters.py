from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#options = Options()
#options.headless = True
def invoke_now(link_to_open):
    driver = webdriver.Chrome(r"E:\\abc\\chromedriver.exe")
    driver.get(link_to_open)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    link = soup.find('a', {'class': 'ipc-lockup-overlay'})['href']

    url = "http://www.imdb.com" + link
    print(url)

    driver.get(url)

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    img_tag = soup.find('img', class_='sc-7c0a9e7c-0 fEIEer')
    img_url = img_tag['src']

    print(img_url+'\n')

    driver.quit()

driver = webdriver.Chrome(r"E:\\abc\\chromedriver.exe")

driver.get("https://www.imdb.com/chart/top")

# print(driver.page_source)
soup = BeautifulSoup(driver.page_source, 'html.parser')
table = soup.find('table', class_ = 'chart full-width')

for td in table.find_all('td', class_ = 'titleColumn'):
    full_title = td.text.strip().replace('\n','').replace('      ','')
    rank = full_title.split('.')[0]
    print(rank)
    title = full_title.split('.')[1].split('(')[0].replace('. ','')
    print(title)
    a = td.find('a')
    print('http://www.imdb.com' + a['href'], '\n')
    passthis = 'http://www.imdb.com' + a['href']
    invoke_now(passthis)

driver.quit()