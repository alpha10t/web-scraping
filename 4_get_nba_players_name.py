from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
"""
soup = BeautifulSoup(html, 'html.parser')

for player in soup.find_all('div', class_='RosterRow_playerName__G28lg'):
    first_name = player.find('p', class_='RosterRow_playerFirstName__NYm50').text
    last_name = player.find('p').text
    print(first_name, last_name)
"""

driver = webdriver.Chrome(r"E:\\abc\\chromedriver.exe", options=options)
driver.get("https://www.nba.com/players")
#PlayerList_playerTable__Jno0k
html_doc = driver.page_source

soup = BeautifulSoup(html_doc, 'html.parser')
#div = soup.find('div', class_= 'PlayerList_playerTable__Jno0k')
"""
for a in div.find_all('a'):
    #first_name = find('p', class_='RosterRow_playerFirstName__NYm50').text
    #last_name = find('p').text
    href = a(['href'])
    #print(first_name, last_name)
    print(href)

    """


for a in soup.find_all('div', class_='RosterRow_playerName__G28lg'):
    first_name = a.find('p', class_='RosterRow_playerFirstName__NYm50').text
    last_name = a.find('p').text
    print(first_name, last_name)

driver.quit()