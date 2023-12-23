from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




options = Options()

options = webdriver.ChromeOptions()
options.add_extension('./new_blocker.crx')
driver = webdriver.Chrome(options=options)

options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)

driver.get("https://www.straitstimes.com/singapore/businessman-linked-to-money-laundering-accused-left-s-pore-abruptly-in-september")

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