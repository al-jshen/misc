from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://particle-clicker.web.cern.ch/particle-clicker/')
while True:
    driver.find_element_by_id('detector-events').click()

