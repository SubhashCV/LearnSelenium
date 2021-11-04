from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

class getAttributeValue():
    def getAttrValvue(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.yatra.com/")
        attr = driver.find_element_by_xpath("//a[normalize-space()='Charter']").get_attribute("target")
        print(attr)
        attr2 = driver.find_element_by_xpath("//a[normalize-space()='Student Fare']").get_attribute("class")
        print(attr2)
        time.sleep(2)


aat_vale = getAttributeValue()
aat_vale.getAttrValvue()