# import modules and libraries
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--user-data-dir=C:\\Users\\kylie\\Documents\\CS599-Project\\Scripts\\UserData")
options.page_load_strategy = 'normal'
driver = webdriver.Chrome(options=options, executable_path=r"C:\Users\kylie\Documents\School\CS-599\Project\chromedriver\chromedriver.exe")

##### start automation of botometer #####
'''driver.get("https://botometer.osome.iu.edu/")
time.sleep(900) # make sure that we start at the 15 minute mark for the 180 searches per 15 minutes

# declare important variables
count = 0 # used to count how many usernames are searched
results_1 = {}
# website fields to interact with
searchField = driver.find_element_by_xpath('//*[@id="inputSN"]')

# open the sample file
with open('sample.txt', 'r') as sample_file:

    # go through the file and create an array to go through
    for line in sample_file:
        string = line.replace('[', '').replace(']', '').replace("'", '').replace(' ', '')
        array = string.split(',')
        array = array[array.index('the312conserva1') + 1:]

    # loop through the array and apply it to the website
    for username in array:
        # interact with buttons/fields
        searchField.clear()
        searchField.send_keys(str(username))
        searchField.submit()

        # sleep to let each username load
        time.sleep(10)

        # collect the results and store them
        score = driver.find_element_by_class_name('user-bot-score')
        results_1[username] = score.text

        # increment the number of usernames searched
        count += 1

        # if we have searched 180 usernames
        if count == 180:
            # make count be 0 again
            count = 0

            f = open('botometer_2.txt', 'w')
            f.write(str(results_1))
            f.close()

            # sleep for 16 minutes
            time.sleep(960)'''

##### start automation of botsentinel #####
driver.get('https://botsentinel.com/')
#time.sleep(900) # make sure that we start at the 15 minute mark for the 180 searches per 15 minutes

# declare important variables
count = 0 # used to count how many usernames are searched
results_2 = {}

# website fields to interact with
analyzeButton = driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[4]/div/div[1]/div/div/a/span')
searchField = driver.find_element_by_id("twitterhandle")
submitButton = driver.find_element_by_id("submitAnalyze")
finishedButton = driver.find_element_by_xpath('//*[@id="finishedAnalyze"]')

# open the sample file
with open('sample.txt', 'r') as sample_file:

    # go through the file and create an array to go through
    for line in sample_file:
        string = line.replace('[', '').replace(']', '').replace("'", '').replace(' ', '')
        array = string.split(',')
        array = array[(array.index('LynnJav') + 1):(array.index('lizwisch'))]

    # loop through the array and apply it to the website
    for username in array:
        analyzeButton.click()
        time.sleep(1)
        searchField.click()
        searchField.clear()
        searchField.send_keys(str(username))
        submitButton.click()
        time.sleep(10)

        score = driver.find_element_by_xpath('//*[@id="responseScore"]')
        score = score.text
        results_2[username] = score

        # write to the file during this time
        f = open('botsentinel.txt', 'a')
        f.write(str(username) + ' ' + str(score) + '\n')
        f.close()

        finishedButton.click()
        time.sleep(1)
'''
        # increment the number of usernames searched
        count += 1

        # if we have searched 180 usernames
        if count == 180:
            # sleep for 16 minutes
            time.sleep(900)
            # make count be 0 again
            count = 0'''