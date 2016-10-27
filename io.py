import json
import sys
from markov import Markov
from difflib import SequenceMatcher

def get_json_object(file, key):
    with open(file, 'r') as jfile:
        content = json.load(jfile)
        return content[key]
    return None

def load_quotes_to_model(file, model):
    quotes = get_json_object(file, "Quotes")
    for i in quotes:
        model.build_table(i["quote"])

def similar(a,b):
    return SequenceMatcher(None,a,b).ratio()

def add_gen_sentences(num):
    model = Markov()
    load_quotes_to_model("QUOTES.JSON", model)
    model.build_chain()

    genquotes = []
    with open("generated_quotes.json", 'r') as jfile:
        content = json.load(jfile)
        genquotes = content["quotes"]

    for _ in range(num):
        newQuote = " ".join(model.make_sentence())
        maxSimilarity = max(similar(newQuote,i) for i in model.allsentences)
        if maxSimilarity < 0.85:
            print(newQuote)
            print(maxSimilarity)
            genquotes.append(newQuote)

    jsonData = {"quotes": genquotes}
    with open("generated_quotes.json", 'w') as jfile:
        json.dump(jsonData,jfile)

def main():
    if len(sys.argv) > 1:
        add_gen_sentences(int(sys.argv[1]))
    else:
        add_gen_sentences(3)

if __name__ == '__main__':
    main()