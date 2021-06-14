from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup 

myurl = "" # Insert url for chosen site

uClient = uReq(myurl) # Grabs and downloads website through connection 
page_contents = uClient.read() # Stores data from website
uClient.close() # Closes connection with website

# Parses the contents stored from the page
page_soup = soup(page_contents, "html.parser") # Second argument needs to be correct format 
# page_soup.h1.span # Shows the h1 tags with span attribute on the website 
# Inspect element to view each tag and parse accordingly 

# Can loop through every class container based on classes 
all_item_containers = page_soup.findAll("div", {"class":"item-container"}) # Finds every div tag, first argument in findAll, with the class, second-first argument, of item-container, second-second argument 
container = all_item_containers[0] 
container.div.div.a.alt 