import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])


import time
chromedriver_dir ='C://Users//Suin//Downloads//chromedriver.exe'
driver = webdriver.Chrome(chromedriver_dir, options = options)

url = 'https://www.naver.com/'
driver.get(url)
time.sleep(0.5)

fav_class = driver.find_element_by_class_name('NM_FAVORITE_LIST')
li = fav_class.find_elements_by_tag_name('li')
li[8].click()
time.sleep(0.5)

webtoon = driver.find_element_by_class_name('Ntxt_webtoon')
webtoon.click()
time.sleep(0.5)

webtoon_end = driver.find_element_by_class_name('Ntxt_menu_end')
webtoon_end.click()
time.sleep(0.5)

titles=[]
latestdays=[]
stories=[]
isitstore=[]

######################
for i in range(200):

    img_list = driver.find_element_by_class_name('img_list')
    li = img_list.find_elements_by_tag_name('li')
    thumb = li[i].find_element_by_class_name('thumb')
    try:
        em = li[i].find_element_by_class_name('ico_store')
        isitstore.append('유료')
        print('유료')
    except:
        isitstore.append('무료')
        print('무료')

    thumb.click()
    time.sleep(0.5)

    details = driver.find_element_by_class_name('detail')
    title = details.find_elements_by_tag_name('h2')
    print(title[0].text)
    titles.append(title[0].text)

    story= details.find_elements_by_tag_name('p')
    print(story[0].text)
    stories.append(story[0].text)

    viewlist = driver.find_element_by_class_name('viewList')
    latestday = viewlist.find_element_by_class_name('num')
    print(latestday.text)
    latestdays.append(latestday.text)

    driver.back()
    time.sleep(0.5)


cols = []
total_data = pd.DataFrame(columns = cols)
total_data['title'] = titles
total_data['story'] = stories
total_data['latestday'] = latestdays
total_data['isitstore'] = isitstore
total_data.to_csv('네이버웹툰.csv', encoding='utf-8-sig')
