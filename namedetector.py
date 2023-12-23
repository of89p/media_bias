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

not_in_dic_words = []
new_name = ''
names = []
repeat = False

for ix, x in enumerate(words):
    x = x.translate(str.maketrans('', '', string.punctuation))
    x =x.lower()

    if x not in dic_arr:
        not_in_dic_words.append([ix, x])

print(not_in_dic_words)

for iy, y in enumerate(not_in_dic_words):
    if iy==len(not_in_dic_words)-1:
        break
    # print(not_in_dic_words[iy][0],not_in_dic_words[iy+1][0] )
    diff_with_prev_element =not_in_dic_words[iy+1][0] - not_in_dic_words[iy][0]

    if diff_with_prev_element == 1 and not repeat:
        new_name = not_in_dic_words[iy][1] + " " + not_in_dic_words[iy + 1][1]
        print(new_name)
        repeat = True
    elif diff_with_prev_element == 1 and repeat:
        new_name = new_name + " " + not_in_dic_words[iy + 1][1]

    elif diff_with_prev_element > 1 and repeat:
        repeat = False
        names.append(new_name)
        new_name = ''

final_names = []

# Check for repeated names
for x in names:
    if x not in final_names:
        final_names.append(x)

print(names)
print(final_names)





#removed: lee, tan, yang,
#added: singaporean





