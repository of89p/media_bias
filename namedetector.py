import string
import time
import lxml.html
import lxml.html.clean
from collections import Counter

from get_articles import obtain_article_info


# f = open("filt.txt", "r")
#
# words_all_text=f.read()


links_arr = []

f = open("links_34_32.txt", "r")
links=f.read()
link_arr_all = links.splitlines()

for x in link_arr_all:
    if x.startswith("https://www.straitstimes.com/singapore/politics/"):
        links_arr.append(x)

need_log_in = True
LIMIT_COUNT = 2
count = 0

total_arr = []

for link in links_arr:
    if count == LIMIT_COUNT:
        break


    words_all_text = obtain_article_info(link, need_log_in=True if count == 0 and need_log_in else False)[3]


    doc = lxml.html.fromstring(words_all_text)
    cleaner = lxml.html.clean.Cleaner(style=True)
    doc = cleaner.clean_html(doc)
    words_all_text = doc.text_content()



    words_all_text=words_all_text.replace('-', '  ')
    words_all_text=words_all_text.replace('“', '  ')
    words_all_text=words_all_text.replace('”', '  ')
    words_all_text=words_all_text.replace('’s', '  ')
    words_all_text = words_all_text.replace("'s", "")
    words_all_text=words_all_text.replace('’', '  ')
    words_all_text = words_all_text.replace('.', '  ')
    words_all_text = ''.join([i for i in words_all_text if not i.isdigit()])


    words = words_all_text.split()



    dictionary = open("./clean_up_data/improve_dictionary/out3.txt", "r")

    dics_arr = dictionary.read().split()

    dic_arr = []

    for x in dics_arr:
        x = x.lower()
        dic_arr.append(x)

    in_dic_words = []
    new_name = ''
    names = []
    repeat = False

    for ix, x in enumerate(words):
        x = x.translate(str.maketrans('', '', string.punctuation))
        x =x.lower()

        if x in dic_arr:
            in_dic_words.append([ix, x])


    for iy, y in enumerate(in_dic_words):
        if iy==len(in_dic_words)-1:
            break

        diff_with_prev_element = in_dic_words[iy + 1][0] - in_dic_words[iy][0]

        if diff_with_prev_element == 1 and not repeat:
            new_name = in_dic_words[iy][1] + " " + in_dic_words[iy + 1][1]

            repeat = True
        elif diff_with_prev_element == 1 and repeat:
            new_name = new_name + " " + in_dic_words[iy + 1][1]

        elif diff_with_prev_element > 1 and repeat:
            repeat = False
            names.append(new_name)
            new_name = ''

    final_names = []

    # Check for repeated names
    for x in names:
        if x not in final_names:
            final_names.append(x)
            total_arr.append(x)

    print(final_names)


    count += 1
    print("CURRENT COUNT: "+str(count))
    time.sleep(5)


total_count = Counter(total_arr)
print(total_count)


