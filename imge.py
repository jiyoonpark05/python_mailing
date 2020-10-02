import dload
from bs4 import BeautifulSoup
from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')
driver.get("https://search.daum.net/search?w=img&nil_search=btn&DA=NTB&enc=utf8&q=%EC%95%84%EB%9D%BC%EC%8B%9C")

time.sleep(5)

req = driver.page_source
soup = BeautifulSoup(req,'html.parser')

i = 1

thumbnails = soup.select('#imgList > div > a > img')
for thumbnail in thumbnails:
    img = thumbnail['src']
    dload.save(img, f'img/{i}.jpg')
    i += 1
driver.quit()