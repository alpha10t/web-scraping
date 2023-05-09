from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True

driver = webdriver.Chrome(r"E:\\abc\\chromedriver.exe", options=options)

driver.get("https://www.imdb.com/chart/top")

# print(driver.page_source)
soup = BeautifulSoup(driver.page_source, 'html.parser')
table = soup.find('table', class_ = 'chart full-width')

for td in table.find_all('td', class_ = 'titleColumn'):
    full_title = td.text.strip().replace('\n','').replace('      ','')
    print(full_title)

    rank = full_title.split('.')[0]
    print(rank)

    title = full_title.split('.')[1].split('(')[0].replace('. ','')
    print(title)

    year = full_title.split('(')[1][:-1]
    print(year)

    a = td.find('a')
    print('http://www.imdb.com' + a['href'], '\n')

driver.quit()