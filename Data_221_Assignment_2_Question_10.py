def find_lines_containing(filename, keyword):
    lines_with_keyword_list = []

    with open(filename, "r") as file:
        text_from_file = file.readlines()

    for i in range(len(text_from_file)):
        line = text_from_file[i]

        if keyword.lower() in line.lower():
            lines_with_keyword_list.append((i + 1, line))

    return lines_with_keyword_list

found_lines = find_lines_containing("csv_and_txt_files/sample-file.txt", "lorem")
print("Matching lines found: ", len(found_lines))

for line in found_lines:
    print(f"Line number {line[0]}: {line[1]}")