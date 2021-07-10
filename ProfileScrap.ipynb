# WebScrappinga=int(input("Enter the number of Sec you want to run program "))
a=int(a/4)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import requests
import csv
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="chromedriver")
subj_url="https://www.roposo.com/discover/video"
c_xpath = '//a[@class="title"]'
id_links = []

csv_file = open('Scraped_profile.csv', 'w+')
writer = csv.writer(csv_file)


#Opening Link
driver.get(subj_url)

#Waiting for getting it load
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,c_xpath)))

i=0
for i in range(0,a):
   
    driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN) 
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,c_xpath)))
    time.sleep(2)
#Some Delay
time.sleep(1)

#Searching links
courses = driver.find_elements_by_xpath(c_xpath)

#Getting all Href and adding links into List/Array
for course in courses:
    
    link=course.get_attribute('href')

    if(link in id_links):
        
        print('Already Exists ==>',link)
    
    else:
        id_links.append(link)
        writer.writerow([link])       
        print(link)

driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN) 


csv_file.close()
driver.close()
print("\n ========================= END OF PROGRAM ========================= ")
