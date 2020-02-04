from selenium import webdriver
import unittest
from selenium.webdriver.common.action_chains import ActionChains
import time


class Apples(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://hrtest.alycedev.com')

    ''' Test One:
    "Free Apples" -> 5 sec pause -> Jonathan grabs apple1 -> 5 sec pause -> Adrian grabs apple2 -> 5 sec pause  ->
    Julie grabs apple3 -> 5 sec pause -> Jonathan grabs apple5 -> 5 sec pause ->
    Adrian grabs apple4  '''

    def test_one(self):
        driver = self.driver

        # Click on "Free Apples"
        free_apples = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[1]/div/section[2]/a')
        ActionChains(driver).click(free_apples).perform()
        time.sleep(5.5)

        # Jonathan grabs Apple1
        jonathan_grab_apple = driver.find_element_by_xpath \
        ('/html/body/div[1]/div[2]/div[2]/div[1]/div/section[1]/ul/li[1]/div/span/button')
        # click on "Grab apple"
        ActionChains(driver).click(jonathan_grab_apple).perform()
        # check that Jonathan has grabbed the apple
        time.sleep(0.5)
        driver.find_element_by_xpath \
        ('/html/body/div[1]/div[2]/div[2]/div[1]/div/section[1]/ul/li[1]/div[2]/ul/li')
        # Wait 5 seconds
        time.sleep(5)

        # Adrian grabs Apple2
        adrian_grab_apple = driver.find_element_by_xpath \
        ('/html/body/div[1]/div[2]/div[2]/div[1]/div/section[1]/ul/li[2]/div/span/button')
        # click on "Grab apple"
        ActionChains(driver).click(adrian_grab_apple).perform()
        # check that Jonathan has grabbed the apple
        time.sleep(0.5)
        driver.find_element_by_xpath \
        ('/html/body/div[1]/div[2]/div[2]/div[1]/div/section[1]/ul/li[2]/div[2]/ul/li')
        time.sleep(5)

        # Julia grabs Apple3
        julia_grab_apple = driver.find_element_by_xpath \
        ('/html/body/div[1]/div[2]/div[2]/div[1]/div/section[1]/ul/li[3]/div/span/button')
        ActionChains(driver).click(julia_grab_apple).perform()
        time.sleep(0.5)
        driver.find_element_by_xpath \
        ('/html/body/div[1]/div[2]/div[2]/div[1]/div/section[1]/ul/li[3]/div[2]/ul/li')
        time.sleep(5)

        # Jonathan grabs Apple5
        jonathan_grab_apple = driver.find_element_by_xpath \
        ('/html/body/div[1]/div[2]/div[2]/div[1]/div/section[1]/ul/li[1]/div/span/button')
        # click on "Grab apple"
        ActionChains(driver).click(jonathan_grab_apple).perform()
        # check that Jonathan has grabbed the apple
        time.sleep(0.5)
        driver.find_element_by_xpath \
        ('/html/body/div[1]/div[2]/div[2]/div[1]/div/section[1]/ul/li[1]/div[2]/ul/li[2]')
        # Wait 5 seconds
        time.sleep(5)

        # Adrian grabs Apple4
        adrian_grab_apple = driver.find_element_by_xpath \
            ('/html/body/div[1]/div[2]/div[2]/div[1]/div/section[1]/ul/li[2]/div/span/button')
        # click on "Grab apple"
        ActionChains(driver).click(adrian_grab_apple).perform()
        # check that Jonathan has grabbed the apple
        time.sleep(0.5)
        driver.find_element_by_xpath \
            ('/html/body/div[1]/div[2]/div[2]/div[1]/div/section[1]/ul/li[2]/div[2]/ul/li[2]')


    ''' Test Two:
    "Free Apples" -> 5 sec pause -> Jonathan grabs apple1 -> 5 sec pause -> Jonathan grabs apple3 -> 5 sec pause  ->
    Jonathan grabs apple5 -> 5 sec pause -> Julie grabs apple2 -> 5 sec pause ->
    Julie grabs apple4 ->   '''

    def test_two(self):
        driver = self.driver

        # Click on "Free Apples"
        free_apples = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[1]/div/section[2]/a')
        ActionChains(driver).click(free_apples).perform()
        time.sleep(5.5)

        # Jonathan grabs Apple1
        jonathan_grab_apple = driver.find_element_by_xpath \
            ('/html/body/div[1]/div[2]/div[2]/div[1]/div/section[1]/ul/li[1]/div[1]/span/button')
        # click on "Grab apple"
        ActionChains(driver).click(jonathan_grab_apple).perform()
        # check that Jonathan has grabbed the apple
        time.sleep(0.5)
        driver.find_element_by_xpath \
            ('/html/body/div[1]/div[2]/div[2]/div[1]/div/section[1]/ul/li[1]/div[2]/ul/li')
        # Wait 5 seconds
        time.sleep(5)

        # Jonathan grabs Apple3
        jonathan_grab_apple = driver.find_element_by_xpath \
            ('/html/body/div[1]/div[2]/div[2]/div[1]/div/section[1]/ul/li[1]/div[1]/span/button')
        # click on "Grab apple"
        ActionChains(driver).click(jonathan_grab_apple).perform()
        time.sleep(0.5)
        # check that Jonathan has grabbed the apple
        driver.find_element_by_xpath \
            ('/html/body/div[1]/div[2]/div[2]/div[1]/div/section[1]/ul/li[1]/div[2]/ul/li[2]')
        # Wait 5 seconds
        time.sleep(5)

        # Jonathan grabs Apple5
        jonathan_grab_apple = driver.find_element_by_xpath \
            ('/html/body/div[1]/div[2]/div[2]/div[1]/div/section[1]/ul/li[1]/div[1]/span/button')
        # click on "Grab apple"
        ActionChains(driver).click(jonathan_grab_apple).perform()
        # check that Jonathan has grabbed the apple
        time.sleep(0.5)
        driver.find_element_by_xpath \
            ('/html/body/div[1]/div[2]/div[2]/div[1]/div/section[1]/ul/li[1]/div[2]/ul/li[3]')
        # Wait 5 seconds
        time.sleep(5)

        # Julia grabs Apple2
        julia_grab_apple = driver.find_element_by_xpath \
        ('/html/body/div[1]/div[2]/div[2]/div[1]/div/section[1]/ul/li[3]/div[1]/span/button')
        ActionChains(driver).click(julia_grab_apple).perform()
        time.sleep(0.5)
        driver.find_element_by_xpath \
        ('/html/body/div[1]/div[2]/div[2]/div[1]/div/section[1]/ul/li[3]/div[2]/ul/li')
        time.sleep(5)

        # Julia grabs Apple4
        julia_grab_apple = driver.find_element_by_xpath \
        ('/html/body/div[1]/div[2]/div[2]/div[1]/div/section[1]/ul/li[3]/div[1]/span/button')
        ActionChains(driver).click(julia_grab_apple).perform()
        time.sleep(0.5)
        driver.find_element_by_xpath \
        ('/html/body/div[1]/div[2]/div[2]/div[1]/div/section[1]/ul/li[3]/div[2]/ul/li[2]')

    '''Test Three:
    Check the pop-up message, if you click on "Grab apple" without a 5-second pause'''

    def test_three(self):
        driver = self.driver

        # Click on "Free Apples"
        free_apples = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[1]/div/section[2]/a')
        ActionChains(driver).click(free_apples).perform()
        time.sleep(5.5)

        # Jonathan grabs the Apple1
        jonathan_grab_apple = driver.find_element_by_xpath \
            ('/html/body/div[1]/div[2]/div[2]/div[1]/div/section[1]/ul/li[1]/div[1]/span/button')

        # click on "Grab apple"
        ActionChains(driver).click(jonathan_grab_apple).perform()
        # check that Jonathan has grabbed the apple
        time.sleep(0.5)
        driver.find_element_by_xpath \
            ('/html/body/div[1]/div[2]/div[2]/div[1]/div/section[1]/ul/li[1]/div[2]/ul/li')

        # Jonathan instantly grabs the Apple3
        jonathan_grab_apple = driver.find_element_by_xpath \
            ('/html/body/div[1]/div[2]/div[2]/div[1]/div/section[1]/ul/li[1]/div[1]/span/button')
        # click on "Grab apple"
        ActionChains(driver).click(jonathan_grab_apple).perform()
        # check that the pop-up message appears
        time.sleep(0.1)
        driver.find_element_by_xpath \
            ('/html/body/div[1]/div[2]/div[1]/div')

    '''Test Four:
        Check the pop-up message, if you're trying to take an apple from the empty basket'''
    def test_four(self):
        driver = self.driver

        # Click on "Free Apples"
        free_apples = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[1]/div/section[2]/a')
        ActionChains(driver).click(free_apples).perform()
        time.sleep(5.5)

        # Jonathan grabs Apple1
        jonathan_grab_apple = driver.find_element_by_xpath \
        ('/html/body/div[1]/div[2]/div[2]/div[1]/div/section[1]/ul/li[1]/div[1]/span/button')
        # click on "Grab apple"
        ActionChains(driver).click(jonathan_grab_apple).perform()
        # check that Jonathan has grabbed the apple
        time.sleep(0.5)
        driver.find_element_by_xpath \
            ('/html/body/div[1]/div[2]/div[2]/div[1]/div/section[1]/ul/li[1]/div[2]/ul/li')
        # Wait 5 seconds
        time.sleep(5)

        # Jonathan grabs Apple3
        jonathan_grab_apple = driver.find_element_by_xpath \
            ('/html/body/div[1]/div[2]/div[2]/div[1]/div/section[1]/ul/li[1]/div[1]/span/button')
        # click on "Grab apple"
        ActionChains(driver).click(jonathan_grab_apple).perform()
        time.sleep(0.5)
        # check that Jonathan has grabbed the apple
        driver.find_element_by_xpath \
            ('/html/body/div[1]/div[2]/div[2]/div[1]/div/section[1]/ul/li[1]/div[2]/ul/li[2]')
        # Wait 5 seconds
        time.sleep(5)

        # Jonathan grabs Apple5
        jonathan_grab_apple = driver.find_element_by_xpath \
            ('/html/body/div[1]/div[2]/div[2]/div[1]/div/section[1]/ul/li[1]/div[1]/span/button')
        # click on "Grab apple"
        ActionChains(driver).click(jonathan_grab_apple).perform()
        # check that Jonathan has grabbed the apple
        time.sleep(0.5)
        driver.find_element_by_xpath \
            ('/html/body/div[1]/div[2]/div[2]/div[1]/div/section[1]/ul/li[1]/div[2]/ul/li[3]')
        # Wait 5 seconds
        time.sleep(5)

        # Julia grabs Apple2
        julia_grab_apple = driver.find_element_by_xpath \
        ('/html/body/div[1]/div[2]/div[2]/div[1]/div/section[1]/ul/li[3]/div[1]/span/button')
        ActionChains(driver).click(julia_grab_apple).perform()
        time.sleep(0.5)
        driver.find_element_by_xpath \
        ('/html/body/div[1]/div[2]/div[2]/div[1]/div/section[1]/ul/li[3]/div[2]/ul/li')
        time.sleep(5)

        # Julia grabs Apple4
        julia_grab_apple = driver.find_element_by_xpath \
        ('/html/body/div[1]/div[2]/div[2]/div[1]/div/section[1]/ul/li[3]/div[1]/span/button')
        ActionChains(driver).click(julia_grab_apple).perform()
        time.sleep(0.5)
        driver.find_element_by_xpath \
        ('/html/body/div[1]/div[2]/div[2]/div[1]/div/section[1]/ul/li[3]/div[2]/ul/li[2]')
<<<<<<< HEAD
        time.sleep(5)
=======

>>>>>>> 9ef1a45c5a275c95b6059ba7da5b62c1aed2911b
        # Jonathan is trying to take an apple from the empty basket
        jonathan_grab_apple = driver.find_element_by_xpath \
            ('/html/body/div[1]/div[2]/div[2]/div[1]/div/section[1]/ul/li[1]/div[1]/span/button')
        # click on "Grab apple"
        ActionChains(driver).click(jonathan_grab_apple).perform()
        # check that the pop-up message appears
        time.sleep(0.1)
        driver.find_element_by_xpath \
            ('/html/body/div[1]/div[2]/div[1]/div/div')


if __name__ == '__main__':
    unittest.main()
