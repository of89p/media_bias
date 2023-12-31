from get_articles import obtain_article_info
from get_links_updated import get_links
# import export_as_json
import time
from collections import Counter
import manage_database
import datetime
from urllib import request


links_arr = []
politician_names_arr = []
total_found_names = []
current_xml = 33

# f = open("links_20_17.txt", "r")
# links=f.read()
# link_arr_all = links.splitlines()

link_arr_all = get_links(current_xml)
# link_arr_all = link_arr_all.append(get_links(31))

a = open("./clean_up_data/get_all_politician_names/politician_names.txt", "r")
politician_names=a.read()
politician_names_arr = politician_names.splitlines()

for x in link_arr_all:
    if x.startswith("https://www.straitstimes.com/singapore"):
        links_arr.append(x)

print("Found "+str(len(links_arr))+" articles"+"\n")

# def internet_on():
#     try:
#         request.urlopen('http://216.58.192.142', timeout=1)
#         return True
#     except request.URLError as err:
#         return False

need_log_in = False
LIMIT_COUNT = 3000
count = 0
ended_halfway = False

def resume_from_interuption():
    pass

if ended_halfway:
    resume_from_interuption()

for link in links_arr:
    if count == LIMIT_COUNT:
        break

    found_names = []

    # print(link)
    print("Attempting to fetch article " + str(count))
    article_data = obtain_article_info(link, need_log_in=True if count == 0 and need_log_in else False)

    if article_data =="no internet":
        print("FATAL ERROR: NO INTERNET")
        exit()


    article_title = article_data[0]
    article_author = article_data[1]
    article_date = article_data[2]
    article_text = article_data[3]

    for name in politician_names_arr:
        if name in article_text and name not in found_names:
            found_names.append(name)
            # manage_database.insert_name_instance(name, article_date, article_title, article_author, link, current_xml)
            # export_as_json.check_if_alr_exist(name, article_date)

    # print("Article published on: "+str(article_date))
    print("Fetched successfully. Names found: "+str(found_names)+"\n")


    for x in found_names:
        total_found_names.append(x)

    count += 1
    # time.sleep(5)

# file_name = str(datetime.datetime.now()) +".txt"
# with open(file_name, "w") as text_file:
#     text_file.write(out+"\n")

print(Counter(total_found_names))


#cheng li hui, Usha Chandradas, Leon Perera
