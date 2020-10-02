from bs4 import BeautifulSoup
from selenium import webdriver
from openpyxl import Workbook

driver = webdriver.Chrome('./chromedriver')

url = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query=나훈아"

driver.get(url)
req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

wb = Workbook()
ws1 = wb.active
ws1.title = "practice_articles"
ws1.append(['title','link','company','thumbnail'])

articles = soup.select('#main_pack > div.news.mynews.section._prs_nws > ul> li')

for article in articles:
    root = article.select_one('dl > dt > a')

    title = article.select_one('dl > dt > a').text
    url = article.select_one('dl > dt > a')['href']
    company = article.select_one('dd.txt_inline > span._sp_each_source').text.split(' ')[0].replace('언론사','')
    thumbnail = article.select_one('div > a > img')['src']

    print([title,url,company,thumbnail])
    ws1.append([title,url,company,thumbnail])

driver.quit()
wb.save(filename='practice_articles.xlsx')
