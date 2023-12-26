from get_articles import obtain_article_info
import time

links_arr = []
politician_names_arr = []

f = open("links.txt", "r")
links=f.read()
link_arr_all = links.splitlines()

a = open("./clean_up_data/get_all_politician_names/politician_names.txt", "r")
politician_names=a.read()
politician_names_arr = politician_names.splitlines()

for x in link_arr_all:
    if x.startswith("https://www.straitstimes.com/singapore/politics/"):
        links_arr.append(x)

need_log_in = False
LIMIT_COUNT = 10
count = 0

for link in links_arr:
    if count == LIMIT_COUNT:
        break

    found_names = []

    article_data = obtain_article_info(link, need_log_in=True if count == 0 and need_log_in else False)

    article_date = article_data[2]
    article_text = article_data[3]

    for name in politician_names_arr:
        if name in article_text:
            found_names.append(name)

    print("Article published on: "+str(article_date))
    print("Names found: "+str(found_names))

    count += 1
    time.sleep(3)


#cheng li hui, Usha Chandradas, Leon Perera
