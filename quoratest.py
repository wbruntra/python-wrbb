 #!/usr/bin/python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from quora_qa import questions, answers


# driver.get("http://www.python.org")
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()

def register(driver,base,username,password):
    driver.get(base+'/register')
    u = driver.find_element_by_name('username')
    u.send_keys(username)
    p = driver.find_element_by_name('password')
    p.send_keys(password)
    p.submit()

def signin(driver,base,username,password):
    driver.get(base+'/signin')
    u = driver.find_element_by_name('username')
    u.send_keys(username)
    p = driver.find_element_by_name('password')
    p.send_keys(password)
    p.submit()

def ask_questions():
    driver = webdriver.Firefox()
    base = "http://localhost:9393"
    signin(driver,base,'george','stevens')
    for question in questions:
        driver.get(base+'/ask')
        t = driver.find_element_by_name('title')
        b = driver.find_element_by_name('body')
        t.send_keys(question[0])
        b.send_keys(question[1])
        b.submit()

base = "http://localhost:9393"
#register(driver,base,'george','stevens')
#signin('george','stevens')
ask_questions()
