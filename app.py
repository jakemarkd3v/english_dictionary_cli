import json
from difflib import get_close_matches
data = json.load(open("data.json"))

def translate(word):
    word =  word.lower()
    if word in data:
        return data[word]
    else:
        return "The word doesn't exist. Did you mean" + " "+ get_close_matches(word, data.keys())[0] + "?"

word = input("Enter a word: ")

print (translate(word))
