#!/usr/bin/env python
# coding: utf-8

# importing required library
from selenium import webdriver

# opening a webpage
driver = webdriver.Chrome()  # PATH
# driver = webdriver.Chrome("/path/to/chromedriver")
driver.get("https://www.pluralsight.com/")

# closing the current window
driver.quit()

# Firefox
driver = webdriver.Firefox()
driver.get("https://www.pluralsight.com/")
driver.quit()

# opening a webpage with options
options = webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-errors")
options.add_argument("--incognito")
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

driver.get("https://google.com/")
