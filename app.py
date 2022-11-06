import json
from difflib import get_close_matches
data = json.load(open("data.json"))

def translate(w):
    word =  w.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(w, data.keys()))> 0:
        yn = input("Did you mean %s ?  Enter Y if yes, or N if no: \n" % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return " The word doesn't exist. Please check it. "
        else:
            return " I didn't understand your entry."

    else:
        return "The word doesn't exist. Did you mean"

w = input("Enter a word: ")

output = translate(w)

if type(output) == list:
    for i in output:
        print (i)

else:
    print(output)



