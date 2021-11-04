import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class fin_ele_by_LinkText_OR_PartialLinkText():
    def elemet(self):

        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.yatra.com/")
        # driver.find_element_by_link_text("Yatra for Business").click()
        driver.find_element_by_partial_link_text("My Accou").click()
        time.sleep(10)


txt1 = fin_ele_by_LinkText_OR_PartialLinkText()
txt1.elemet()