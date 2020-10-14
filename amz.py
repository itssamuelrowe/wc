import time
from bs4 import BeautifulSoup
from selenium import webdriver
import json

DRIVER_PATH='/usr/lib/chromium-browser/chromedriver'
driver = webdriver.Chrome(DRIVER_PATH)

response=('https://www.amazon.in')
driver.get(response)

user="redmi note 5"
driver.execute_script(f'var element = document.getElementById("twotabsearchtextbox"); element.value = "{user}";')

user_input = driver.find_element_by_class_name('nav-search-submit.nav-sprite')
user_input.click()
driver.find_element_by_class_name('a-size-medium.a-color-base.a-text-normal').click()
time.sleep(5)
driver.switch_to.window(driver.window_handles[1])
new=driver.current_url        
driver.get(new)

driver.find_element_by_id("acrCustomerReviewText").click()


#driver.find_element_by_class_name('a-link-emphasis.a-text-bold').click()
time.sleep(5)
base_url = driver.current_url

result = []
for k in range (1,3):
    new_page_url = str(base_url) + "&pageNumber=" + str(k)
    driver.get(new_page_url)
    time.sleep(5)
    
    review_titles = driver.find_elements_by_xpath('//a[@data-hook="review-title"]/span')
    review_contents = driver.find_elements_by_xpath('//div[@data-hook="review-collapsed"]/span')
    customer_names = driver.find_elements_by_xpath('//span[@class="a-profile-name"]')
    ratings_list = driver.find_elements_by_xpath('//span[@class="a-icon-alt"]')
    dates = driver.find_elements_by_xpath('//span[@data-hook="review-date"]')

    for review_title, review_content, customer_name, ratings, date in zip(review_titles, review_contents, customer_names, ratings_list, dates):
        print(ratings.text)
        result.append({
            "review_title": review_title.text,
            "review_content": review_content.text,
            "customer_name": customer_name.text,
            "ratings": ratings.text,
            "date": date.text,
        })

output = json.dumps(result, indent=4, sort_keys=True)
print(output)