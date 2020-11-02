# Interactive English Dictionary
An interactive dictionary you can use to search definitions of English words.

## Getting started
* Download the repository
* Run the **app.py** file either directly or from command line
* The app will prompt you for a word, it could be any from the English language (e.g. *mountain*, *rain*, etc.)
* The app will show an appropriate message based on the word you entered and if that word was found in the dictionary or not
* If the word is found, you will see a definition of the word. There could be more than one definition
* If the word seems to be misspelled, the app will suggest you the closest matching word.
* Note that you will have 3 attempts before you accept the word suggested
* If the word is not found, you will get an appropriate message telling you the word was not found

## Built With
* Python 3.6
* **json** module to read the dictionary data stored in a json file
* **difflib** module to find a closes matching word