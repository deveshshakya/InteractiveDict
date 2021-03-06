import json
from difflib import get_close_matches

data = json.load(open("data.json"))  # loading dictionary file first


def finder(word):
    """Finds meaning of input word."""

    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys(), cutoff=0.8)) > 0:
        ans = input("Did you mean {} instead? Enter Y if Yes, or N! ".format(get_close_matches(word, data.keys(), cutoff=0.8)[0]))
        if ans == 'Y' or ans == 'y':
            return data[get_close_matches(word, data.keys())[0]]
        elif ans == 'N' or ans == 'n':
            return "The word doesn't found, Please double check it."
        else:
            return "Don't understand."
    else:
        return "The word doesn't found, Please double check it."


print("Total words available " + str(len(data.keys())) + ".")

while True:
    word = input("\nEnter a word (q for quit): ")
    if word == 'q' or word == 'Q':
        exit()
    output = finder(word.lower())
    if type(output) == list:
        for meaning in output:
            print(meaning)
    else:
        print(output)
