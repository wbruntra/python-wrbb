from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
base = "http://localhost:9393"
driver.get(base)
h1 = driver.find_element_by_css_selector("h1")
print h1.text

driver.get(base+'/new')
a = driver.find_element_by_name('author')
a.send_keys("William Bruntrager")
t = driver.find_element_by_name('title')
t.send_keys("The Little Prince")
driver.find_element_by_name('author')
b = driver.find_element_by_name('body')
body = "Once when I was six years old I saw a magnificent picture in a book, called True Stories from Nature, about the primeval forest. It was a picture of a boa constrictor in the act of swallowing an animal"
b.send_keys(body)
