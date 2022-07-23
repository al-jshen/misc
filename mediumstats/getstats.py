import time
from selenium import webdriver
import re
from datetime import date

def runstuff():

    driver = webdriver.Chrome()
    driver.get("https://medium.com/m/signin")

    time.sleep(2)

    driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/div[2]/div[3]/a/div').click()

    time.sleep(1)

    driver.find_element_by_xpath('//*[@id="username_or_email"]').send_keys('wetalk_physics')
    driver.find_element_by_xpath('//*[@id="password"]').send_keys('Cana1Chase2Daniella3Jeff4Tahmeed5')
    driver.find_element_by_xpath('//*[@id="allow"]').click()

    time.sleep(3)

    driver.get('https://medium.com/me/stats/post/30171f6f6225')
    time.sleep(1)

    views = driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div[1]/div[5]/div[1]/div/h2').text

    driver.get('https://medium.com/post/30171f6f6225')
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)

    try:
        responses = driver.find_element_by_class_name('pw-responses-count').text
    except:
        responses = 0

    try:
        claps = driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div[5]/div/div[1]/div/div[4]/div/div[1]/div[1]/span[1]/div/div[2]/div/p/button')
        inner = claps.get_attribute('innerHTML')
        claps = re.match('^\d+', inner).group(0)
        if claps is None:
            claps = 0
    except:
        claps = 0

    driver.close()

    today = date.today().strftime("%B %d, %Y")

    update = f'{today}: {views} views, {responses} responses, {claps} claps\n'
    print(update)

    with open("stats.txt", "r") as f:
        if today not in f.read():
            needtoupdate = True
        else:
            needtoupdate = False

    if needtoupdate:
        with open("stats.txt", "a") as f:
            f.write(update)


if __name__ == "__main__":
    while True:
        if time.localtime().tm_hour == 21 and time.localtime().tm_min < 5:
            runstuff()
            time.sleep(120)
        elif time.localtime().tm_hour == 20:
            print(f"sleeping for 2 mins, last check was at {time.strftime('%B %d, %H:%M:%S', time.localtime())}")
            time.sleep(120)
        else:
            print(f"sleeping for an hour, last check was at {time.strftime('%B %d, %H:%M:%S', time.localtime())}")
            time.sleep(3600)
