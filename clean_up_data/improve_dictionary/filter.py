import string

f = open("sg_names.txt", "r")
words_all_text=f.read()

arr = words_all_text.splitlines()

filtered_arr = []

#get_all_politician_names all names into this format: [number, name]
for x in arr:
    if len(x) != 0 and x[0].isdigit():
        element_break = 0

        #find position where number ends and name starts
        for idy, y in enumerate(x):
            if not y.isdigit():
                element_break = idy
                break

        number = x[:element_break].strip()
        name = x[element_break:].strip()

        head, sep, tail = name.partition(" (")
        name = head

        #remove empty elements
        if name and number:
            filtered_arr.append([number, name])

# print(filtered_arr)

print("==================================")

king_arr = []
present_arr = []
still_in_same_grp = False
# cycles = 0

#format into arrays
for ix, x in enumerate(filtered_arr):

    # if cycles == 3:
    #     break

    # if last element
    if ix+1 == len(filtered_arr):
        print("last element")
    #for first element
    elif str(int(x[0]) + 1) == filtered_arr[ix+1][0]:
        present_arr.append(x)
        still_in_same_grp = True
    #for last element of group
    elif still_in_same_grp == True and str(int(x[0]) + 1) != filtered_arr[ix+1][0]:
        present_arr.append(x)
        still_in_same_grp = False
        king_arr.append(present_arr)
        present_arr = []
        # print(present_arr)
        # cycles += 1



#filter out non-names eg comapny names
reject_arr = []
accept_arr = []
for ix, x in enumerate(king_arr):
    total_lenth = 0
    for iy, y in enumerate(x):
        total_lenth = len(y[1]) + total_lenth
    avg_length = total_lenth/len(x)
    # print("Array no: "+str(ix)+"; avg length: "+str(avg_length))
    if avg_length > 21:
        reject_arr.append(x)
    else:
        accept_arr.append(x)

# with open("output_reject.txt", "w") as text_file:
#     for ix, x in enumerate(reject_arr):
#         text_file.write("Array no: "+str(ix)+"\n\n")
#         text_file.write(str(x))
#         text_file.write("\n\n\n\n\n\n\n\n\n\n====================================\n\n\n\n\n\n\n\n\n\n")
#
# with open("output_accept.txt.txt", "w") as text_file:
#     for ix, x in enumerate(accept_arr):
#         text_file.write("Array no: "+str(ix)+"\n\n")
#         text_file.write(str(x))
#         text_file.write("\n\n\n\n\n\n\n\n\n\n====================================\n\n\n\n\n\n\n\n\n\n")

# with open("output (original).txt", "w") as text_file:
#     text_file.write(str(present_arr))
#     text_file.write("\n\n\n\n\n\n\n\n\n\n====================================\n\n\n\n\n\n\n\n\n\n")


# print(king_arr[23])

# with open("output_reject.txt", "w") as text_file:
#     for ix, x in enumerate(king_arr):
#         text_file.write("Array no: "+str(ix)+"\n\n")
#         text_file.write(str(x))
#         text_file.write("\n\n\n\n\n\n\n\n\n\n====================================\n\n\n\n\n\n\n\n\n\n")

arr_soup = []
for ix, x in enumerate(accept_arr):
    for iy, y in enumerate(x):
        name_arr = y[1].split()
        for x in name_arr:
            arr_soup.append(x)

arr_soup = list(dict.fromkeys(arr_soup))


with open("duplicates.txt", "w") as text_file:
    text_file.write("This document contains "+str(len(arr_soup))+" unique words which make up Singaporeans' names.\n")
    for x in arr_soup:
        out = (x.translate(str.maketrans('', '', string.punctuation))).lower()
        text_file.write(out+"\n")