#The starting process is similar as the earlier two questions
PUNCTUATION = "?!/#@$%,.;:'`-"
ALPHABET = "abcdefghijklmnopqrstuvwxyz"
NEWLINE_CHARACTER = '\n'
nearly_identical_pairs = []
formatted_lines = []


with open("csv_and_txt_files/sample-file.txt", "r") as file:
    # Key difference here --- we want to store sentences this time, not words
    # This is possible through the file.readlines() method
    lines_from_text_file = file.readlines()

for i in range(len(lines_from_text_file)):
    lines_from_text_file[i] = {
        "Original line": lines_from_text_file[i],
        "Line number": i
    }

'''
Quickly casting the original list into a tuple
This is so that no errors are raised when taking items out of the original list and using that
during the loop simultaneously
Runtime errors will occur otherwise
'''
for line in tuple(lines_from_text_file):
    if line["Original line"] == NEWLINE_CHARACTER:
        lines_from_text_file.remove(line)

for index in range(len(lines_from_text_file)):
    line = lines_from_text_file[index]
    edited_line = lines_from_text_file[index]["Original line"]

    for punctuation in PUNCTUATION:
        if punctuation in line["Original line"]:
            edited_line = edited_line.replace(punctuation, "")

    edited_line = edited_line.rstrip(NEWLINE_CHARACTER).lower().replace(" ", "")

    line["Edited line"] = edited_line
    formatted_lines.append(line)

for dictionary1 in formatted_lines:
    for dictionary2 in formatted_lines:
        if dictionary1 is dictionary2:
            continue

        if dictionary1["Edited line"] == dictionary2["Edited line"]:
            if (dictionary2, dictionary1) not in nearly_identical_pairs:
                nearly_identical_pairs.append((dictionary1, dictionary2))

for near_identical_pair in nearly_identical_pairs:
    print(
        f'''
        Line number {near_identical_pair[0]["Line number"]} -> {near_identical_pair[0]["Edited line"]}
        Original line: {near_identical_pair[0]["Original line"]}
        is paired with: 
        Line number {near_identical_pair[1]["Line number"]} -> {near_identical_pair[1]["Edited line"]}
        Original line: {near_identical_pair[1]["Original line"]}
        \n
        '''
    )