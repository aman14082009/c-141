from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import requests
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("./chromedriver.exe")
browser.get(START_URL)


time.sleep(10)
headers = ["name", "distance", "mass", "radius"]

star_data = []
def scrap():
    time.sleep(2)
    soup = BeautifulSoup(browser.page_source, "html.parser")
    for th_tag in soup.find_all("th", attrs = {"class", "headerSort"}):
        tr_tags = th_tag.find_all("tr")
        temp_list = []
        for index, tr_tag in enumerate(tr_tag):
            if index == 0:
                temp_list.append(tr_tag.find_all("a")[0].contents[0])
            else:
                try:
                    temp_list.append(tr_tag.contents[0])
                except:
                       temp_list.append("")
        star_data.append(temp_list)
scrap()
    

