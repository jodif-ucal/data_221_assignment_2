def find_lines_containing(filename, keyword):
    lines_with_keyword_list = []

    with open(filename, "r") as file:
        #file.readlines() returns a list
        text_from_file = file.readlines()

    #Using index to iterate as we will need it to store the line number
    for i in range(len(text_from_file)):
        line = text_from_file[i]

        #Checking if the keyword is in the line, disregarding capitals with the .lower() method
        if keyword.lower() in line.lower():
            #i + 1 as the .txt file starts with 1, not 0
            lines_with_keyword_list.append((i + 1, line))

    return lines_with_keyword_list

found_lines = find_lines_containing("csv_and_txt_files/sample-file.txt", "lorem")
print("Matching lines found: ", len(found_lines)) #-> No matching lines

for i in range(3):
    #Just in case not enough matching lines were found, so that the program won't crash
    if i < len(found_lines):
        print(f"Line {i + 1}: {found_lines[i][1]}")