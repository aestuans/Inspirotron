import random
from sentence import break_text_to_sentences, break_sentence_to_words

BEGIN_CHAR = "^"
END_CHAR = "$"

class Markov(object):

    def __init__(self):
        super(Markov, self).__init__()
        self.chain = {}
        self.table = []
        self.allsentences = []

    def build_table(self, text):
        sentences = break_text_to_sentences(text)
        self.allsentences+=sentences

        for sentence in sentences:
            self.table.append(break_sentence_to_words(sentence))

    def build_chain(self):
        chain = {}

        for _sentence in self.table:
            sentence = [BEGIN_CHAR, BEGIN_CHAR] + _sentence + [END_CHAR]

            for i in range(len(sentence)-2):

                curState = tuple(sentence[i:i+2])
                nexState = tuple(sentence[i+1:i+3])

                if curState not in chain:
                    chain[curState] = {}

                if nexState not in chain[curState]:
                    chain[curState][nexState] = 0

                chain[curState][nexState] += 1

        self.chain = chain

    def make_sentence(self):
        sentence = []
        curState = tuple([BEGIN_CHAR, BEGIN_CHAR])

        while True:
            sumWeight = sum(self.chain[curState].values())
            choice, weight = zip(*self.chain[curState].items())

            weightedList = []
            for i in range(len(choice)):
                for _ in range(weight[i]):
                    weightedList.append(choice[i])

            rand = random.randint(0,sumWeight-1)
            curState = weightedList[rand]
            if list(curState)[-1] is END_CHAR:
                break
            sentence += [list(curState)[-1]]

        return sentence    