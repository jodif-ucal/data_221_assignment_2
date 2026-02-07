import requests
from bs4 import BeautifulSoup

header = {'User-Agent': 'Windows/0.0 (joseph.odihi@ucalgary.ca)'}
html = requests.get("https://en.wikipedia.org/wiki/Data_science", headers=header).text
soup = BeautifulSoup(html, "html.parser")

h2_headings = soup.find("div", id="mw-content-text").find_all("h2")

for i in range(len(h2_headings)):
    h2_headings[i] = h2_headings[i].text + "\n"

excluded_headers = ["See also\n", "References\n", "External links\n", "Notes\n", "[edit]\n"]

for h2_header in excluded_headers:
    if h2_header in h2_headings:
        h2_headings.remove(h2_header)

with open("csv_and_txt_files/headings.txt", "w") as file:
    file.writelines(h2_headings)