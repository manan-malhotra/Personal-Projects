import json
from difflib import get_close_matches
data=json.load(open("data.json"))

def translate(word):
    word=word.lower()
    if word in data:
        return "\n".join(data[word])
    elif len(get_close_matches(word,data.keys(),cutoff=0.85)) >0:
        yn= input(f"Did you mean {get_close_matches(word,data.keys())[0]} insted? \nPress Y for yes, N for no:")
        if yn.upper()=='Y':
            return "\n".join(data[get_close_matches(word,data.keys())[0]])
        elif yn.upper()=='N':
            return "Sorry.Could not find your word"
        else:
            return "Sorry. We couldn't understand your entry"
    else:
        return "The word doesn't exist. Please double check it."

word=input("Enter a word:")
print(translate(word))
