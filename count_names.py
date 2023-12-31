from get_articles import obtain_article_info
from get_links_updated import get_links
# import export_as_json
import time
from collections import Counter
import manage_database
import datetime
from urllib import request

def count_names(current_xml):
    links_arr = []
    politician_names_arr = []
    total_found_names = []

    filename = "./xml_src_output/out_"+str(current_xml)+".txt"
    f = open(filename, "r")
    links=f.read()
    links_arr = links.splitlines()

    total_len = len(links_arr)

    # link_arr_all = get_links(current_xml)
    # link_arr_all = link_arr_all.append(get_links(31))

    a = open("./clean_up_data/get_all_politician_names/politician_names.txt", "r")
    politician_names=a.read()
    politician_names_arr = politician_names.splitlines()


    # for x in link_arr_all:
    #     if x.startswith("https://www.straitstimes.com/singapore"):
    #         links_arr.append(x)

    print("Found "+str(len(links_arr))+" articles"+"\n")



    need_log_in = True
    # LIMIT_COUNT = 3000
    count = 1
    # ended_halfway = (True, "https://www.straitstimes.com/singapore/transport/small-car-coe-lowest-since-early-2012")
    #
    # if ended_halfway[0]:
    #     links_arr = links_arr[links_arr.index(ended_halfway[1]):]


    for link in links_arr:
        # if count == LIMIT_COUNT:
        #     break
        #
        found_names = []

        # print(link)
        print("Attempting to fetch article " + str(count)+"/"+str(total_len)+" [XML "+str(current_xml)+"]")
        article_data = obtain_article_info(link, need_log_in=True if count == 1 and need_log_in else False)

        if article_data =="no internet":
            print("FATAL ERROR: NO INTERNET")
            manage_database.insert_internet_error(link)
            exit()


        article_title = article_data[0]
        article_author = article_data[1]
        article_date = article_data[2]
        article_text = article_data[3]

        for name in politician_names_arr:
            if name in article_text and name not in found_names:
                found_names.append(name)
                manage_database.insert_name_instance(name, article_date, article_title, article_author, link, current_xml)
                # export_as_json.check_if_alr_exist(name, article_date)

        # print("Article published on: "+str(article_date))
        print("Fetched successfully. Names found: "+str(found_names)+"\n")


        for x in found_names:
            total_found_names.append(x)

        count += 1

    # file_name = str(datetime.datetime.now()) +".txt"
    # with open(file_name, "w") as text_file:
    #     text_file.write(out+"\n")

    print(Counter(total_found_names))


for x in range(10):
    x+=1
    count_names(x)



#cheng li hui, Usha Chandradas, Leon Perera
