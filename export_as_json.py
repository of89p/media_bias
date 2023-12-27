import json
import datetime


def first_add(name, article_date):
    f = open("./output/out1.txt")
    json_data=json.loads(f.read())
    print(json_data)

    data = json_data
    data[name] = str(article_date)
    json_data = json.dumps(data)

    file_name = "./output/out1.txt"
    with open(file_name, "a") as text_file:
        text_file.write(json_data+"\n")
    print("NOTE: Added as JSON to text file.")

    print(json_data)


first_add("new", "lol")

# def add_to_existing_json(name, article_date):
#
#
#
#
# def check_if_alr_exist(name, article_date):
#
#     f = open("./output/out1.txt")
#     json_arrays=f.read().splitlines()
#
#     for i, json_array in enumerate(json_arrays):
#         existing_data=json.loads(json_array)
#
#         if existing_data["name"] == name:
#             add_to_existing_json(name, article_date)
#             # print("yes")


        # if i == int(len(json_arrays)-1):
        #     # print("Not inside json data")
        #     first_add(name, article_date)
        #     break

# ======================
# data = {}
# data['Lee Hsien Loong'] = {}
# data['Lee Hsien Loong']['dates_mentioned'] = "22 Dec 2020, 5:00 am SGT"
# data["testing1234"] = {}
# data['testing1234']['dates_mentioned'] = "22 Dec 2020, 5:00 am SGT"
#
# json_data = json.dumps(data)
#
# print(json_data)