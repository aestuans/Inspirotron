import re

def break_text_to_sentences(text):
    endWordPattern = re.compile(r"(\w+)[\.\?!](\s+)")
    endWords = re.finditer(endWordPattern,text)
    endIndex = [w.end() for w in endWords]
    endIndex.insert(0,0)
    endIndex.append(None)
    sentences = [text[endIndex[i]:endIndex[i+1]].strip() for i in range(len(endIndex)-1)]
    return sentences

def break_sentence_to_words(sentence):
    return re.split(" ", sentence)