from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

links = ['','/signin','/register']

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

class SecureUserTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.base = "http://localhost:9393"

    def test(self):
        base = self.base
        driver = self.driver
        username = 'george'
        password = 'stevens'
        # register(driver,base,username,password)
        # assert "Sign out" in driver.page_source
        # driver.get(base+'/signout')
        register(driver,base,username,password)
        assert "Name already taken" in driver.page_source
        signin(driver,base,username,'notit')
        assert "Bad password" in driver.page_source
        signin(driver,base,username,password)
        assert "Sign out" in driver.page_source
        driver.get(base+'/signout')
        signin(driver,base,'nonsense','hello')
        assert "No user by that name" in driver.page_source

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
