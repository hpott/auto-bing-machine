#Written by hpott
import string, random, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox()
browser.get("https://www.bing.com/search?q=s")
while True:
    try:
        search = browser.find_element_by_id("sb_form_q")
        search.send_keys(Keys.CONTROL+"a")
        search.send_keys(Keys.DELETE)
        search.send_keys(random.choice(string.ascii_letters))
        time.sleep(3)
        suggested = browser.find_element_by_css_selector("#sa_5004 > div:nth-child(1)")
        suggested.click()
        time.sleep(3)
    except Exception:
        print("Error. Retrying sequence")
