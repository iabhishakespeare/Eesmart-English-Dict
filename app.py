import json
from difflib import get_close_matches

data = json.load(open("data/data.json"))
acceptable_replies = ("Y", "YES", "N", "NO")
negative_response = "Sorry, the word '{}' does not exist in the dictionary."


def swap_to_title_case(word):
    """
        Converts a word from any case to title case. E.g. 'mumbai' will become 'Mumbai'
        :param word: A string which is will converted to Title case.
        :return: A string in Title case
    """
    return word.lower()[0].upper() + word.lower()[1:]


def check_key_exists(key):
    """
        Checks if a key exists in the dictionary stored in the global variable above named 'data'.
        :param key: A dictionary key with string data type.
        :return: A string in the appropriate case which is found as a key in the dictionary of 'data.json' file
    """
    if key.lower() in data:
        return key.lower()
    elif key.upper() in data:
        return key.upper()
    elif swap_to_title_case(key) in data:
        return swap_to_title_case(key)


def search_definition(word):
    """
        Accepts a word from the user as a parameter and returns the definition of that word if found. E.g. 'mountain',
        'tree', 'river'
        :param word: A string which will be used as a key for the dictionary
        :return: The definition of the word searched or else an appropriate message if the word is not found in the
        dictionary.
    """
    if check_key_exists(word):
        return data[check_key_exists(word)]

    if len(get_close_matches(word.lower(), data.keys())) > 0:
        suggested_word = get_close_matches(word.lower(), data.keys())[0]
        yes_or_no = input("Did you mean '{}'? Please type yes or no: ".format(suggested_word)).upper()
        num_of_attempts = 2
        while not(yes_or_no in acceptable_replies) and num_of_attempts > 0:
            yes_or_no = input("Did you mean '{}'? Please type yes or no: ".format(suggested_word)).upper()
            num_of_attempts -= 1
        if yes_or_no == "Y" or yes_or_no == "YES":
            return data[get_close_matches(word.lower(), data.keys())[0]]
        elif yes_or_no == "N" or yes_or_no == "NO":
            return negative_response.format(word)
        return "Sorry, you've exceeded the number of attempts. Please try again."

    return negative_response.format(word)


# Stores the search results. It could be a string or a list
search_result = search_definition(input("Type your word: "))

# Checks if the search result is a list. If yes, it prints each list item one by one which are definitions of the word
if type(search_result) == list:
    for item in search_result:
        print(">>> " + item)
else:
    print(search_result)
