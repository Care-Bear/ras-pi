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
    browser.maximize_window()
    browser.find_element_by_tag_name("body").send_keys(Keys.F11)
    browser.find_element_by_id("menu_documentation").click()
    time.sleep(5)

local = "file:///some/local/directory"

def rotate_pages(browser):
    while True:
        try:
            if config["links"]:
                for page in config["links"]:
                    print page
                    browser.get(page)
                    time.sleep(sleep_time)
            if config["local"]:
                for page in config["local"]:
                    print local + page
                    browser.get(local + page)
                    time.sleep(sleep_time)
            if config["auth_links"]:
                for page in config["auth_links"]:
                    url = page["url"]
                    print url
                    browser.get(url)

                    username_element_type = page.get("username_element_type")
                    username_element_name = page.get("username_element_name")
                    username = page.get("username")
                    username_xpath = '//*[@{0}="{1}"]'.format(
                      username_element_type,
                      username_element_name
                    )

                    password_element_type = page.get("password_element_type")
                    password_element_name = page.get("password_element_name")
                    password = page.get("password")
                    password_xpath = '//*[@{0}="{1}"]'.format(
                      password_element_type,
                      password_element_name
                    )

                    try:
                        if browser.find_element_by_xpath(username_xpath):
                            browser.find_element_by_xpath(username_xpath).send_keys(username)
                            browser.find_element_by_xpath(password_xpath).send_keys(password)
                            browser.find_element_by_xpath(password_xpath).send_keys(Keys.ENTER)
                    except Exception:
                        pass

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

if __name__ == '__main__':
    get_browser()
    rotate_pages(browser)
