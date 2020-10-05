from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


PATH ='C:\Program Files (x86)\EdgeDriver\msedgedriver.exe'
driver = webdriver.Edge(PATH)
# users_input = input("Input The song you want to Download")
driver.get("https://www.mp3juices.cc")

search = driver.find_element_by_name("query")
search.send_keys("yeet")
search_button = driver.find_element_by_id("button")
time.sleep(2)
search_button.click()



first_result = driver.find_element_by_css_selector("")

first_result.click
print(first_result)

