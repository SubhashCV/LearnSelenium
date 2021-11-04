import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class byClass():
    def fun1(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element(By.ID, "login-input").send_keys("Test Engineer By ID")
        time.sleep(5)

    def fun_2(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element(By.CLASS_NAME,"email-login-box").send_keys("bu class name")
        time.sleep(5)

priwate = byClass()
# priwate.fun1()
priwate.fun_2()