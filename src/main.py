import requests
from bs4 import BeautifulSoup
url = "https://www.facebook.com"
html = requests.get(url).text

# Find all <a> tags
links = BeautifulSoup(html, "html.parser").find_all('a')

# Extract and print the href attributes
for link in links:
    href = link.get('href')
    if href:
        print(href)