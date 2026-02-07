import requests
from bs4 import BeautifulSoup

#Wikipedia requires bots to use headers when accessing the website, which is here
header = {'User-Agent': 'Windows/0.0 (joseph.odihi@ucalgary.ca)'}

#Scraoe the html page and parse it
html = requests.get("https://en.wikipedia.org/wiki/Data_science", headers=header).text
soup = BeautifulSoup(html, "html.parser")

#Find the title of the page and print it
print(f"Title of page: {soup.find("title").text}\n")

#Find the div with the mw-content-text id, then find the second <p> tag in the div, which contains
#the first paragraph
print(f"First paragraph of page:\n{soup.find("div", id="mw-content-text").find_all("p")[1].text}")
