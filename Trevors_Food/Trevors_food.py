# importing the libraries
from bs4 import BeautifulSoup
import requests


########### Step 1 ############

# Get User Input then set a URL to work with!
users_ingredients = input("Input List of Ingriedients (seperate each item with a space): ")

url="https://realfood.tesco.com/search.html?search="+users_ingredients



# Make a GET request to fetch the raw HTML content
html_content = requests.get(url, headers={'x-forwarded-for':'1.1.1.3'}).text


# Parse the html content
soup = BeautifulSoup(html_content, "html5lib")


# Search for the first
link = soup.find('a',attrs={'class':'ddl-search-results__item-link' })
new_link = link.get('href')


# Gonna use this to head to the second page!
recipe_link = 'https://realfood.tesco.com'+new_link


########### STEP 2 ###########


# Another Request for the second Page
recipe_page_req = requests.get(recipe_link, headers={'x-forwarded-for':'1.1.1.3'}).text


# Parse
recipe_soup = BeautifulSoup(recipe_page_req,"html5lib")

# Search For the Recipe on the page
recipe = recipe_soup.find('div',attrs={'class': 'recipe-detail__cms'})

# Search For the Heading of the food YEEEEEEEEEEEEEEE
print(recipe_soup.find('h1', attrs={'class':'recipe-detail__headline'}).text)


# Aidans code to make the text look prettier XD
print("")
x = recipe.findChildren('ol')

for i in x:
    print(i.text)
