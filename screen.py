#!/usr/bin/python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchWindowException
import time
import json
import os
import sys


SCRIPT = os.path.abspath(__file__)
SCRIPT_DIR = os.path.dirname(SCRIPT)
JSON_FILE = os.path.join(SCRIPT_DIR, 'screen.json')

browser = webdriver.Firefox()
config = json.load(open(JSON_FILE))

def get_browser():
    browser.get("http://www.seleniumhq.org/")
    browser.find_element_by_tag_name("body").send_keys(Keys.F11)
    browser.find_element_by_id("menu_documentation").click()
    time.sleep(5)


get_browser()

local = "file:///some/local/directory"

while True:
   try:
      for page in config["links"]:
            print page
            browser.get(page)
            time.sleep(15)

      for page in config["local"]:
            print local + page
            browser.get(local + page)
            time.sleep(15)
   except BaseException as err:
        print err
        try:
            browser.close()
        except NoSuchWindowException:
            pass
        browser = webdriver.Firefox()
        get_browser()
