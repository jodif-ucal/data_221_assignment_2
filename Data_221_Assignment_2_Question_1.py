#Variables in capitals are meant to be constant---their values will not change
PUNCTUATION = "?!/#@$%,.;:'`-"
ALPHABET = "abcdefghijklmnopqrstuvwxyz"
modified_tokens_from_text_file = []
dicts_of_modified_tokens_from_text_file = []

#Put all the tokens into the raw_tokens_from_text_file list
#str.split() uses the whitespace character in between words as a separator, and returns a list with all the tokens separated
#Only two lines long as we don't need the file for the rest of the program
with open("csv_and_txt_files/sample-file.txt", "r") as file:
    raw_tokens_from_text_file = file.read().split()

for word in raw_tokens_from_text_file:
    current_word = word.lower()
    first_character_of_word = current_word[0]
    last_character_of_word = current_word[-1]
    alphabetic_counter = 0 #resets after every new word; it can be used for each token this way

    #Removing the first and/or last character of each token if it contains
    #str.replace() will find the instance of a character and replace it with the second argument given
    #The third argument specifies that we only want to do this once
    if first_character_of_word in PUNCTUATION:
        current_word.replace(first_character_of_word, "", 1)

    if last_character_of_word in PUNCTUATION:
        current_word.replace(last_character_of_word, "", 1)

    #checking if the token has more than 2 characters within it
    for character in current_word:
        if character in ALPHABET:
            alphabetic_counter += 1

        if alphabetic_counter >= 2:
            modified_tokens_from_text_file.append(current_word)
            #for efficiency purposes, we break the loop here, we already did what we needed to do
            break

for modified_token in modified_tokens_from_text_file:
    dict_of_modified_token = {modified_token: modified_tokens_from_text_file.count(modified_token)}

    #If a dictionary like this one is already in the dicts list, this if statement will be false
    #This essentially prevents duplicates
    if dict_of_modified_token not in dicts_of_modified_tokens_from_text_file:
        dicts_of_modified_tokens_from_text_file.append(dict_of_modified_token)

'''
The optional parameter 'key' in the method list.sort() allows us to define how we want to sort the list.
Here, I'm using a lambda function, which is a one-time use function that can be written within a line of code
'token' is essentially the parameter I operate on; 'key' will pass in each dictionary in the list as an argument
token.values() returns a dict_values showing all the values present in the dictionary.
In order to access the items inside through code, we turn it into a list.
This way, all the dictionaries inside the dicts list will be sorted by their values: how many times the word appear in the original txt file
The optional parameter 'reverse' sorts all the dicts in descending order .
'''
dicts_of_modified_tokens_from_text_file.sort(key=lambda token : list(token.values())[0], reverse=True)

for index in range(10):
    #dict.items() does the same as dict.values(), just that it gets the key-value pair instead
    modified_token = list(dicts_of_modified_tokens_from_text_file[index].items())
    #Double indexing is used here as converting the dict_items object to a list stores each key-value pair as an item in the list
    #We're only concerned about one key-value pair of course, so that's the first and only item in the modified_token list
    print(f"{modified_token[0][0]} -> {modified_token[0][1]}")