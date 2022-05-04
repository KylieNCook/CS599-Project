from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

count = 0

options = Options()
options.add_argument("--user-data-dir=C:\\Users\\kylie\\Documents\\CS599-Project\\Scripts\\UserData")
options.page_load_strategy = 'normal'
driver = webdriver.Chrome(options=options, executable_path=r"C:\Users\kylie\Documents\School\CS-599\Project\chromedriver\chromedriver.exe")
driver.get('https://botsentinel.com/')

analyzeButton = driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[4]/div/div[1]/div/div/a/span')
searchField = driver.find_element_by_id("twitterhandle")
submitButton = driver.find_element_by_id("submitAnalyze")
results = driver.find_element_by_xpath('//*[@id="responseScore"]')
finishedButton = driver.find_element_by_xpath('//*[@id="finishedAnalyze"]')

analyzeButton.click()
time.sleep(1)
searchField.click()
searchField.clear()
searchField.send_keys('NAU')
submitButton.click()
time.sleep(1)
driver.get("https://botometer.osome.iu.edu/")


'''with open('sample.txt', 'r') as sample_file:

    for line in sample_file:
        string = line.replace('[', '').replace(']', '').replace("'", '').replace(' ', '')
        array = string.split(',')

    for username in array:
        searchField.clear()
        searchField.send_keys(str(username))
        searchField.submit()
        count += 1

        if count == 180:
            time.sleep(960)
            count = 0'''