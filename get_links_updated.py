import urllib.request
import re
import manage_database

def get_links(page_number):
    print("Accessing XML "+str(page_number))
    contents = urllib.request.urlopen("https://www.straitstimes.com/sitemap.xml?page="+str(page_number)).read()

    all_links = re.findall("<loc>(.*?)</loc>", str(contents))

    return all_links

    # print(all_links)
    # print(len(all_links))



def compile_links():
    for xml in range(34):
        found_links = []
        xml += 1

        filename = "./xml_src/xml_"+str(xml)+".xml"
        f = open(filename, "r")
        links=f.read()

        all_links = re.findall("<loc>(.*?)</loc>", str(links))

        for link in all_links:
            if link.startswith("https://www.straitstimes.com/singapore"):
                found_links.append(link)

        filename = "./xml_src_output/out_"+str(xml)+".txt"
        with open(filename, 'w') as f:
            for x in found_links:
                f.write(x+"\n")

        print("Finished writing for xml "+str(xml))
