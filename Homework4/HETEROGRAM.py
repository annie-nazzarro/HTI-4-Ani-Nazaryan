sentence = input('Input your favorite quote ')
s = sentence.replace(' ', '')

split_sentence_list = [j for j in ''.join(sentence.split())]

if len(split_sentence_list) == len(set(split_sentence_list)) and s.isalpha():
    print('YES')
else:
    print('NO')

