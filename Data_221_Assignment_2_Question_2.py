#Just over half of this script is going to be the same as question 1
#The starting process isn't going to change
PUNCTUATION = "?!/#@$%,.;:'`-"
ALPHABET = "abcdefghijklmnopqrstuvwxyz"
modified_tokens_from_text_file = []
tuples_of_bigrams = []
dicts_of_bigrams = []

with open("csv_and_txt_files/sample-file.txt", "r") as file:
    raw_tokens_from_text_file = file.read().split()

for word in raw_tokens_from_text_file:
    current_word = word.lower()
    first_character_of_word = current_word[0]
    last_character_of_word = current_word[-1]
    alphabetic_counter = 0

    if first_character_of_word in PUNCTUATION:
        current_word.replace(first_character_of_word, "", 1)

    if last_character_of_word in PUNCTUATION:
        current_word.replace(last_character_of_word, "", 1)

    for character in current_word:
        if character in ALPHABET:
            alphabetic_counter += 1

        if alphabetic_counter >= 2:
            modified_tokens_from_text_file.append(current_word)
            break

#This is where the differences come in
for index in range(len(modified_tokens_from_text_file)):
    #This check needs to be made on the index; otherwise, this piece of code will try to use an index out of range,
    #Which would cause a runtime error
    if index != len(modified_tokens_from_text_file) - 1:
        #Tuples cannot be changed (they are immutable), making them suitable to store bigrams together
        tuple_of_bigrams = (
            modified_tokens_from_text_file[index], modified_tokens_from_text_file[index + 1]
        )

        tuples_of_bigrams.append(tuple_of_bigrams)

for bigram_tuple in tuples_of_bigrams:
    #Tuples are immutable, therefore we can use them as keys
    bigram_dict = {bigram_tuple: tuples_of_bigrams.count(bigram_tuple)}

    #Again, this prevents duplicate dictionaries of the same bigram appearing
    if bigram_dict not in dicts_of_bigrams:
        dicts_of_bigrams.append(bigram_dict)

#The lambda function here does the same thing as before
dicts_of_bigrams.sort(key=lambda bigram: list(bigram.values())[0], reverse=True)

for index in range(10):
    bigram_item = list(dicts_of_bigrams[index].items())
    '''
    The bigrams themselves are inside a tuple, which is the first item of the tuple from items, 
    which is in a list. Therefore, that requires triple indexing.
    Not the same case with getting the frequency of the bigram though, as that's just the second
    item in the list
    '''
    print(f"{bigram_item[0][0][0]} {bigram_item[0][0][1]} -> {bigram_item[0][1]}")