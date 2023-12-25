from collections import Counter
import string

f = open("duplicates.txt", "r")

x=f.read()

king_arr = []

all_words = x.splitlines()

for y in all_words:
    king_arr.append(y)


total_count = Counter(king_arr)
# print(total_count)

lesser_than_arr = []

for key, value in list(total_count.items()):
    if value < 40:
        # total_count.pop(key)
        lesser_than_arr.append(key)

# print(lesser_than_arr)

f = open("common_el_words.txt", "r")
words_all_text=f.read()

arr_common_words = words_all_text.splitlines()
# print(arr_common_words)


list3 = set(lesser_than_arr)&set(arr_common_words) # we don't need to list3 to actually be a list

list4 = sorted(list3, key = lambda k : lesser_than_arr.index(k))
#
# print(list4)
# print("====================")



total_count = list(total_count)

final_list = []

for x in total_count:
    if x not in list4:
        final_list.append(x)

print(final_list)

# # print("====================")
# print(total_count)


with open("out3.txt", "w") as text_file:
    # text_file.write("This document contains "+str(len(arr_soup))+" unique words which make up Singaporeans' names.\n")
    for x in final_list:
        # out=x
        out = (x.translate(str.maketrans('', '', string.punctuation))).lower()
        text_file.write(out+"\n")