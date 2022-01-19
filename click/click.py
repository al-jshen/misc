from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://humanbenchmark.com/tests/reactiontime/")

time.sleep(0.5)

driver.find_element_by_class_name("view-splash").click()

not_clicked = True
while not_clicked:
    try:
        driver.find_element_by_class_name("view-go").click()
        not_clicked = False
    except:
        time.sleep(0.005)
