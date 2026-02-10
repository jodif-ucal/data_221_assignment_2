import requests
from bs4 import BeautifulSoup
import csv

header = {'User-Agent': 'Windows/0.0 (joseph.odihi@ucalgary.ca)'}
html = requests.get("https://en.wikipedia.org/wiki/Machine_learning", headers=header).text
soup = BeautifulSoup(html, "html.parser")
table_dict = {}

#Using index 0 as we want the first table on the page
first_table = soup.find("div", id="mw-content-text").find_all("table")[0]
table_header = first_table.find("th").text
table_rows = first_table.find_all("td")

longest_row_length = 0
column_titles = [table_header]
table_list = []

for row in table_rows:
    row_name = row.find("div", class_="sidebar-list-title")
    #For some reason one of the row_names return None, so we're skipping over in here
    if row_name is None:
        continue

    #The table header will be the first column name
    dict_row = {column_titles[0]: row_name.text}
    #The values list contain the text of the links in the dropdowns on the row
    values = [value.text for value in row.find_all("li")]

    for count in range(len(values)):
        #Some values have newline characters in them. Just removing them here before saving to
        #the dictionary by column
        dict_row[f"col{count + 1}"] = values[count].replace("\n", " ")

    table_list.append(dict_row)

    #Finding the row with the most amount of items
    if len(dict_row) > longest_row_length:
        longest_row_length = len(dict_row)

#The longest row length found earlier is being used to create the correct amount of columns for
# the csv file
for count in range(longest_row_length - 1):
    column_titles.append(f"col{count + 1}")

#When using csvDictWriter with a csv file, windows interprets the encoding for new lines used by it
#as two new lines. the argument newline circumvents this issue.
with open("csv_and_txt_files/wiki_table.csv", "w", newline="") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=column_titles)
    writer.writeheader()

    #Writing the dictionaries in table_list into the csv file
    for row in table_list:
        writer.writerow(row)