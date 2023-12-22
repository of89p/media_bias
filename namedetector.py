import string
from string import digits


f = open("test.txt", "r")

words_all_text=f.read()

# remove_digits = str.maketrans('', '', digits)
# words_all_text = words_all_text.translate(remove_digits)
# words_all_text=''.join([i for i in words_all_text if not i.isdigit()])

words_all_text=words_all_text.replace('-', ' ')
words_all_text=words_all_text.replace('“', ' ')
words_all_text=words_all_text.replace('”', ' ')
words_all_text=words_all_text.replace('’s', ' ')
words_all_text=words_all_text.replace('’', ' ')


words = words_all_text.split()

# print(words)


dictionary = open("words_alpha.txt", "r")

dic_arr = dictionary.read().split()

# print(dic_arr)

prev_no = -10000
word = ''
repeat = False

for ix, x in enumerate(words):

    x = x.translate(str.maketrans('', '', string.punctuation))
    x =x.lower()

    if x not in dic_arr:
        print(ix, x)
        if ix -1 == prev_no:

            word = word+" "+words[ix-1]+" "+x
            # print("x: "+x)
            print("word: "+word)
        prev_no = ix




