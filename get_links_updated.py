import urllib.request
import re

def get_links(page_number):
    print("Accessing XML "+str(page_number))
    contents = urllib.request.urlopen("https://www.straitstimes.com/sitemap.xml?page="+str(page_number)).read()

    all_links = re.findall("<loc>(.*?)</loc>", str(contents))

    return all_links

    # print(all_links)
    # print(len(all_links))
