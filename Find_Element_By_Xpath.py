import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class FindElementByXpath():
    def locate_Xpath_demo(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")  
        # driver.find_element_by_xpath('//input[@id='login-input']').send_keys('hello')
        driver.find_element_by_xpath("//button[normalize-space()='sign in with facebook']").send_keys('venky')
        # // button[normalize - space() = 'sign in with facebook']
        time.sleep(4)


xpat = FindElementByXpath()
xpat.locate_Xpath_demo()
