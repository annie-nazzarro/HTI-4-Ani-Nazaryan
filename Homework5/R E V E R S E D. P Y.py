rev_sentence = input("Input the quote you want to reverse ")


def recursive_reversed(sentence):
    if sentence == "" or sentence == 1:
        return sentence
    else:
        return recursive_reversed(sentence[1:]) + sentence[0]


print(recursive_reversed(rev_sentence))
