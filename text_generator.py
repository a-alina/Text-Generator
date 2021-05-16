from nltk.tokenize import regexp_tokenize
from collections import Counter
from sys import exit
import random

f = open("corpus.txt", 'r', encoding='UTF-8')

f = f.read() # working file

# separating words by whitespaces
def text_processing(text_o):

    return(regexp_tokenize(text_o, r'\S+'))
# creating a bigram from  proceed list
def bigram(l):

    bigram_list = [[l[i], l[i + 1]] for i in range(len(l) - 1)]

    return bigram_list  # nested list

def list_processing(lst):
    # this list contains heads as keys and list of all possible tails from the original text
    dict_lst = {}

    for bigram in lst:
        dict_lst.setdefault(bigram[0], []).append(bigram[1])

    # nested dictionary with heads as keys and tails as keys for the second dictionary
    # with counter as value
    final = {}

    for object in dict_lst.items():
        final[object[0]] = Counter(object[1])
    return final

def markov(dict):

    chain_list = [[] for i in range(10)]

    # list of keys for the first element
    punct = ['.', '!', '?']
    first_list = [i for i in dict.keys() if i[0].isupper() and i[-1] not in punct]

    # for every sentance
    for sentance in range(10):
        head = random.choice(first_list)
        chain_list[sentance].append(head)
        length = random.randint(5, 10)
        while True:
                tail = dict[head].most_common(1)[0][0]
                chain_list[sentance].append(tail)
                dict[head].pop(tail)
                head = tail

                if len(chain_list[sentance]) > 4 and tail[-1] in punct:
                    break

                elif len(chain_list[sentance]) == length - 1:
                    tail = random.choice([i[0] for i in dict[head].items() if i[0][-1] in punct])
                    chain_list[sentance].append(tail)
                    break

                else:
                    pass

    return [' '.join(chain_list[i]) for i in range(10)]

print(*markov(list_processing(bigram(text_processing(f)))), sep='\n')
