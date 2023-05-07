from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# import time

# Headless Chrome
options = Options()
options.headless = True

driver = webdriver.Chrome(r"E:\\abc\\chromedriver.exe", options=options)
driver.get("http://python.org")
html_doc = driver.page_source

# time.sleep(5)
print(html_doc)
driver.quit()