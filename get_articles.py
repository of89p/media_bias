from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import re

ST_PASSWORD = ''
from private.dev_settings import *

options = Options()

options = webdriver.ChromeOptions()
options.add_extension('./new_blocker.crx')
driver = webdriver.Chrome(options=options)

options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)

# driver.get_all_politician_names("https://www.straitstimes.com/singapore")

def log_in():
    time.sleep(7)
    # log in to ST acc
    try:
        driver.find_element(By.ID, 'sph_login').click()
        user = driver.find_element(By.ID, 'IDToken1')
        user.send_keys("terenceteoly@gmail.com")
        password = driver.find_element(By.ID, 'IDToken2')
        password.send_keys(ST_PASSWORD)
        driver.find_element(By.ID, 'btnLogin').click()
    except:
        error_text = "cannot log in"
        print("ERROR: " + error_text)

    # DISMISS TOO MANY ACC NOTIFICATION T0 ALLOW SITE TO DELETE OLD LOGIN COOKIES
    try:
        # dismiss too many acc notification
        time.sleep(10)
        driver.find_element(By.ID, 'btnMysphMsg').click()
        time.sleep(5)
    except:
        pass

# log_in()


#find all a href to articles
# article_links = []
# def get_all_links():
#     ignore_links = [
#     "https://www.straitstimes.com/singapore",
#     "https://www.straitstimes.com/singapore/jobs",
#     "https://www.straitstimes.com/singapore/housing",
#     "https://www.straitstimes.com/singapore/parenting-education",
#     "https://www.straitstimes.com/singapore/politics",
#     "https://www.straitstimes.com/singapore/health",
#     "https://www.straitstimes.com/singapore/transport",
#     "https://www.straitstimes.com/singapore/courts-crime",
#     "https://www.straitstimes.com/singapore/consumer",
#     "https://www.straitstimes.com/singapore/environment",
#     "https://www.straitstimes.com/singapore/community",
#     "https://www.straitstimes.com/singapore",
#     "https://www.straitstimes.com/singapore/jobs",
#     "https://www.straitstimes.com/singapore/housing",
#     "https://www.straitstimes.com/singapore/parenting-education",
#     "https://www.straitstimes.com/singapore/politics",
#     "https://www.straitstimes.com/singapore/health",
#     "https://www.straitstimes.com/singapore/transport",
#     "https://www.straitstimes.com/singapore/courts-crime",
#     "https://www.straitstimes.com/singapore/consumer",
#     "https://www.straitstimes.com/singapore/environment",
#     "https://www.straitstimes.com/singapore/community",
#     "https://www.straitstimes.com/singapore",
#     "https://www.straitstimes.com/singapore/jobs",
#     "https://www.straitstimes.com/singapore/housing",
#     "https://www.straitstimes.com/singapore/parenting-education",
#     "https://www.straitstimes.com/singapore/politics",
#     "https://www.straitstimes.com/singapore/health",
#     "https://www.straitstimes.com/singapore/transport",
#     "https://www.straitstimes.com/singapore/courts-crime",
#     "https://www.straitstimes.com/singapore/consumer",
#     "https://www.straitstimes.com/singapore/environment",
#     "https://www.straitstimes.com/singapore/community",
#     "https://www.straitstimes.com/singapore",
#     "https://www.straitstimes.com/singapore/jobs",
#     "https://www.straitstimes.com/singapore/housing",
#     "https://www.straitstimes.com/singapore/parenting-education",
#     "https://www.straitstimes.com/singapore/politics",
#     "https://www.straitstimes.com/singapore/health",
#     "https://www.straitstimes.com/singapore/transport",
#     "https://www.straitstimes.com/singapore/courts-crime",
#     "https://www.straitstimes.com/singapore/consumer",
#     "https://www.straitstimes.com/singapore/environment",
#     "https://www.straitstimes.com/singapore/community",
#     "https://www.straitstimes.com/singapore/latest",
#     "https://www.straitstimes.com/singapore#scroll-1",
#     "https://www.straitstimes.com/singapore#scroll-2",
#     "https://www.straitstimes.com/singapore#scroll-3",
#     "https://www.straitstimes.com/singapore#scroll-4",
#     "https://www.straitstimes.com/singapore#scroll-5",
#     "https://www.straitstimes.com/singapore#scroll-6",
#     "https://www.straitstimes.com/singapore#scroll-7",
#     "https://www.straitstimes.com/singapore#scroll-8",
#     "https://www.straitstimes.com/singapore#scroll-9",
#     "https://www.straitstimes.com/singapore#scroll-10",
#     "https://www.straitstimes.com/singapore#scroll-1",
#     "https://www.straitstimes.com/singapore#scroll-2",
#     "https://www.straitstimes.com/singapore/jobs",
#     "https://www.straitstimes.com/singapore#main-content",
#     "https://www.straitstimes.com/singapore#main-content",
#     "https://www.straitstimes.com/singapore#"
#     ]
#
#     for x in driver.find_elements(By.XPATH, "//a[@href]"):
#         link = x.get_attribute("href")
#         if link not in ignore_links and "https://www.straitstimes.com/singapore" in link:
#             article_links.append(link)
#
# get_all_links()






total_arr = []


def obtain_article_info(link, need_log_in):
    driver.get(link)
    if need_log_in:
        log_in()

    #GET TITLE
    try:
        article_title = driver.find_element(By.CLASS_NAME, 'headline')
        article_title=article_title.get_attribute("innerHTML").strip()
    except:
        error_text = "cannot get article title for"+link
        print("ERROR: "+error_text)
        article_title = "ERROR"

    #GET AUTHOR
    try:
        journalist_container = driver.find_element(By.CLASS_NAME, 'group-info').get_attribute("innerHTML")
        # x = journalist_container.split(">")
        #
        # author_name = x[1][:-3]
        # job_title = x[3][:-5]

        author_name = re.findall(">(.*?)</a>", str(journalist_container))[0]
    except:
        error_text = "cannot get author for"+link
        print("ERROR: "+error_text)
        author_name = "ERROR"

    #GET DATE PUBLISHED
    try:
        article_date = driver.find_element(By.CLASS_NAME, 'story-postdate')
        article_date = article_date.get_attribute("innerHTML")
    except:
        error_text = "cannot get published date for"+link
        print("ERROR: "+error_text)
        article_date = "ERROR"


    #GET BODY TEXT
    complete_body_text = ''
    try:
        p_tags = driver.find_elements(By.TAG_NAME, 'p')

        for x in p_tags:
            complete_body_text = complete_body_text + x.get_attribute("innerHTML")
    except:
        error_text = "cannot get published body text for"+link
        print("ERROR: "+error_text)
        complete_body_text = "ERROR"

    return_arr = [article_title, author_name, article_date, complete_body_text]
    return return_arr


