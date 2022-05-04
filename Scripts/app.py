from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--user-data-dir=C:\\Users\\kylie\\Documents\\CS599-Project\\Scripts\\UserData")
options.page_load_strategy = 'normal'
driver = webdriver.Chrome(options=options, executable_path=r"C:\Users\kylie\Documents\School\CS-599\Project\chromedriver\chromedriver.exe")
driver.get("https://botometer.osome.iu.edu/")



searchField = driver.find_element_by_xpath('//*[@id="inputSN"]')

with open('sample.txt', 'r') as sample_file:

    for line in sample_file:
        string = line.replace('[', '').replace(']', '').replace("'", '').replace(' ', '')
        array = string.split(',')

    for username in array:
        searchField.clear()
        searchField.send_keys(str(username))
        searchField.submit()