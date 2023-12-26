import string
import time
from get_articles import obtain_article_info

f = open("links_34_32.txt", "r")
words_all_text=f.read()

arr = words_all_text.splitlines()



ignore_links = [
    "https://www.straitstimes.com/singapore",
    "https://www.straitstimes.com/singapore/jobs",
    "https://www.straitstimes.com/singapore/housing",
    "https://www.straitstimes.com/singapore/parenting-education",
    "https://www.straitstimes.com/singapore/politics",
    "https://www.straitstimes.com/singapore/health",
    "https://www.straitstimes.com/singapore/transport",
    "https://www.straitstimes.com/singapore/courts-crime",
    "https://www.straitstimes.com/singapore/consumer",
    "https://www.straitstimes.com/singapore/environment",
    "https://www.straitstimes.com/singapore/community",
    "https://www.straitstimes.com/singapore",
    "https://www.straitstimes.com/singapore/jobs",
    "https://www.straitstimes.com/singapore/housing",
    "https://www.straitstimes.com/singapore/parenting-education",
    "https://www.straitstimes.com/singapore/politics",
    "https://www.straitstimes.com/singapore/health",
    "https://www.straitstimes.com/singapore/transport",
    "https://www.straitstimes.com/singapore/courts-crime",
    "https://www.straitstimes.com/singapore/consumer",
    "https://www.straitstimes.com/singapore/environment",
    "https://www.straitstimes.com/singapore/community",
    "https://www.straitstimes.com/singapore",
    "https://www.straitstimes.com/singapore/jobs",
    "https://www.straitstimes.com/singapore/housing",
    "https://www.straitstimes.com/singapore/parenting-education",
    "https://www.straitstimes.com/singapore/politics",
    "https://www.straitstimes.com/singapore/health",
    "https://www.straitstimes.com/singapore/transport",
    "https://www.straitstimes.com/singapore/courts-crime",
    "https://www.straitstimes.com/singapore/consumer",
    "https://www.straitstimes.com/singapore/environment",
    "https://www.straitstimes.com/singapore/community",
    "https://www.straitstimes.com/singapore",
    "https://www.straitstimes.com/singapore/jobs",
    "https://www.straitstimes.com/singapore/housing",
    "https://www.straitstimes.com/singapore/parenting-education",
    "https://www.straitstimes.com/singapore/politics",
    "https://www.straitstimes.com/singapore/health",
    "https://www.straitstimes.com/singapore/transport",
    "https://www.straitstimes.com/singapore/courts-crime",
    "https://www.straitstimes.com/singapore/consumer",
    "https://www.straitstimes.com/singapore/environment",
    "https://www.straitstimes.com/singapore/community",
    "https://www.straitstimes.com/singapore/latest",
    "https://www.straitstimes.com/singapore#scroll-1",
    "https://www.straitstimes.com/singapore#scroll-2",
    "https://www.straitstimes.com/singapore#scroll-3",
    "https://www.straitstimes.com/singapore#scroll-4",
    "https://www.straitstimes.com/singapore#scroll-5",
    "https://www.straitstimes.com/singapore#scroll-6",
    "https://www.straitstimes.com/singapore#scroll-7",
    "https://www.straitstimes.com/singapore#scroll-8",
    "https://www.straitstimes.com/singapore#scroll-9",
    "https://www.straitstimes.com/singapore#scroll-10",
    "https://www.straitstimes.com/singapore#scroll-1",
    "https://www.straitstimes.com/singapore#scroll-2",
    "https://www.straitstimes.com/singapore/jobs",
    "https://www.straitstimes.com/singapore#main-content",
    "https://www.straitstimes.com/singapore#main-content",
    "https://www.straitstimes.com/singapore#"
]

filtered_arr = []

for x in arr:
    if x not in ignore_links and "https://www.straitstimes.com/singapore" in x:
        filtered_arr.append(x)


# print(filtered_arr)

total_arr = []
LIMIT = 5

i = 1
while i < LIMIT:
    print(filtered_arr[i])
    total_arr.append(obtain_article_info(filtered_arr[i]))
    time.sleep(5)
    i += 1

print(total_arr)