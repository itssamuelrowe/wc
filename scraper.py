# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 21:02:51 2020

@author: Dell
"""

import time
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium import webdriver
import json

DRIVER_PATH='/usr/lib/chromium-browser/chromedriver'
options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

def scrap_flipkart(search_text):
    driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
    driver.get('https://www.flipkart.com')
    time.sleep(5)

    driver.find_element_by_class_name('_2AkmmA._29YdH8').click()
    time.sleep(5)   
    user_input = driver.find_element_by_class_name('LM6RPg')
    user_input.click()

    # initiate a new input variable here to take the apps response instead of Redmi note 5 
    user_input.send_keys(search_text) # follow as per the app response (refer above line)
    time.sleep(5)    
    driver.find_element_by_class_name('vh79eN').click()
    time.sleep(5)
    driver.find_element_by_class_name('_3wU53n').click()
    time.sleep(5)
    i=driver.switch_to.window(driver.window_handles[1])
    new=driver.current_url    
    driver.get(new)

    def strip_read_more(text):
      if text.endswith("READ MORE"):
        return text[0:len(text) - 9]
      return text

    result = []
    driver.find_element_by_class_name("swINJg._3nrCtb").click()
    time.sleep(5)
    page_url=driver.current_url
    for k in range(1, 3):
        new_page_url = (str(page_url) + "&page=" + str(k))    
        driver.get(new_page_url)        
        [item.click() for item in driver.find_elements_by_class_name("_1EPkIx")]
        time.sleep(1)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(1)
        soup = BeautifulSoup(driver.page_source, 'lxml')
        for items in soup:
            review_titles = soup.find_all("p",{"class" : "_2xg6Ul"})# rev title
            review_contents = soup.find_all("div",{"class" : "qwjRop"})#rev
            customer_names = soup.find_all("p",{"class" : "_3LYOAd _3sxSiS"})#customer name
            ratings_list = soup.find_all("div",{"class" : "hGSR34 E_uFuv"})#ratings
            dates = soup.find_all("p",{"class" : "_3LYOAd"})

            filtered_dates = []
            for date in dates:
                print(date.text)
                if date.text.find(",") >= 0:
                    filtered_dates.append(date)

            for review_title, review_content, customer_name, ratings, date in zip(review_titles, review_contents, customer_names, ratings_list, filtered_dates):
              result.append({
                "review_title": review_title.text,
                "review_content": strip_read_more(review_content.text),
                "customer_name": customer_name.text,
                "ratings": ratings.text,
                "date": date.text,
              })

    return result
    #output_file = open("output.json", "a")
    #output = json.dumps(result, indent=4, sort_keys=True)
    #output_file.write(output)