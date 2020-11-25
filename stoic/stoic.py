from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")
DRIVER_PATH = "/home/luke/stoic/chromedriver"

driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
driver.get('https://stoic-quote-generator.web.app/')

element = driver.find_element_by_class_name("btn-primary")
element.click()


quote = driver.find_element_by_id("quoteDisplay")

print(quote.text)
driver.quit()