# access a webpage and obtain information

import requests

from bs4 import BeautifulSoup

#We can read the content of the server’s response. Consider the GitHub timeline again:
r = requests.get('https://www.ole.com.ar/')
r.text

soup=BeautifulSoup(r.text, 'html.parser')
#print(soup.prettify())

print(soup.title)

soup.find_all(class_="entry-title")

for story_heading in soup.find_all(class_="entry-title"):
	
	print(story_heading.get_text())







