import requests
from bs4 import BeautifulSoup
import csv

header = {'User-Agent': 'Windows/0.0 (joseph.odihi@ucalgary.ca)'}
html = requests.get("https://en.wikipedia.org/wiki/Machine_learning", headers=header).text
soup = BeautifulSoup(html, "html.parser")
table_dict = {}

first_table = soup.find("div", id="mw-content-text").find_all("table")[0]
table_header = first_table.find("th").text
table_rows = first_table.find_all("td")

longest_row_length = 0
column_titles = [table_header]
table_list = []

for row in table_rows:
    row_name = row.find("div", class_="sidebar-list-title")
    if row_name is None:
        continue

    dict_row = {column_titles[0]: row_name.text}
    values = [value.text for value in row.find_all("li")]

    for count in range(len(values)):
        dict_row[f"col{count + 1}"] = values[count].replace("\n", " ")

    table_list.append(dict_row)

    if len(dict_row) > longest_row_length:
        longest_row_length = len(dict_row)


for count in range(longest_row_length - 1):
    column_titles.append(f"col{count + 1}")

for di in table_list:
    print(di)

with open("csv_and_txt_files/wiki_table.csv", "w", newline="") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=column_titles)
    writer.writeheader()

    for row in table_list:
        writer.writerow(row)