import time
from selenium import webdriver
from  webdriver_manager.chrome import ChromeDriverManager

class DemoFindElementByID():
    def locate_by_id_demo(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element_by_id('login-input').send_keys('test@test.com')
        driver.find_element_by_name('login-input').send_keys('  Hello@hyee.com')
        time.sleep(2)

datapass = DemoFindElementByID()
datapass.locate_by_id_demo()
