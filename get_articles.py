from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

import time



options = Options()

options = webdriver.ChromeOptions()
options.add_extension('./new_blocker.crx')
driver = webdriver.Chrome(options=options)

options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)

driver.get("https://www.straitstimes.com/singapore")


def log_in():
    # log in to ST acc
    driver.find_element(By.ID, 'sph_login').click()
    user = driver.find_element(By.ID, 'IDToken1')
    user.send_keys("terenceteoly@gmail.com")
    password = driver.find_element(By.ID, 'IDToken2')
    password.send_keys("Test6546!")
    driver.find_element(By.ID, 'btnLogin').click()

    # dismiss too many acc notification
    time.sleep(10)
    driver.find_element(By.ID, 'btnMysphMsg').click()
    time.sleep(5)

# log_in()


#find all a href to articles
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

article_links = []

for x in driver.find_elements(By.XPATH, "//a[@href]"):
    link = x.get_attribute("href")
    if link not in ignore_links and "https://www.straitstimes.com/singapore" in link:
        print(link)
    article_links.append(link)




# links = driver.find_elements("xpath", "//a[@href]")
# print(links)

# driver.find_element_by_css_selector('.btn_close_342755_1703311765049').click()
# driver.find_element_by_xpath('//*[@id="btn_close_342755_1703312831760"]').click()

# ids = driver.find_element("xpath", '//*[@id]')
# print(ids)
# for ii in ids:
#     print("Hello")
#     #print ii.tag_name
#     print (ii.get_attribute('id'))

# heading1 = driver.find_elements(By.TAG_NAME, 'a')

#
# for x in heading1:
#     x.click()

# btn_close_342755_1703314456890
# btn_close_342755_1703314473363
# btn_close_342755_1703314502295

# //*[@id="btn_close_342755_1703314549017"]

# time.sleep(3)
#
# driver.execute_script("window.stop();")
# print("stop")

# try:
#     element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, "/html/body/div[11]/a"))
#     )
# finally:
#     driver.find_element(By.XPATH, "/html/body/div[12]/a").click()
#     driver.find_element(By.XPATH, "/html/body/div[11]/a").click()


# driver.find_element(By.XPATH, "/html/body/div[12]/a").click()
# driver.find_element(By.XPATH, "/html/body/div[11]/a").click()

# /html/body/div[11]/a
# /html/body/div[11]/a
# /html/body/div[12]/a
# /html/body/div[12]/a
# /html/body/div[12]/a
# /html/body/div[12]/a