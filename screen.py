#!/usr/bin/python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchWindowException
import time
import yaml
import os


SCRIPT = os.path.abspath(__file__)
SCRIPT_DIR = os.path.dirname(SCRIPT)
FILE = os.path.join(SCRIPT_DIR, 'config.yaml')

config = yaml.safe_load(open(FILE))
browser = webdriver.Firefox()

sleep_time = config["sleep_time"]

def get_browser():
    browser.get("http://www.seleniumhq.org/")
    browser.find_element_by_tag_name("body").send_keys(Keys.F11)
    browser.find_element_by_id("menu_documentation").click()
    time.sleep(5)

get_browser()

local = "file:///some/local/directory"


while True:
    try:
        if config["links"]:
            for page in config["links"]:
                print page
                browser.get(page)
                time.sleep(sleep_time)
        elif config["local"]:
            for page in config["local"]:
                print local + page
                browser.get(local + page)
                time.sleep(sleep_time)

        """
        This is a very un-elegant way to circumvent an issue with the for loops, as they
        would throw a NoneType is not defined error once it reaches the end of the
        list.
        """

    except TypeError:
        pass

    except BaseException as err:
        print err
        try:
            browser.close()
        except NoSuchWindowException:
            pass
        browser = webdriver.Firefox()
        get_browser()
