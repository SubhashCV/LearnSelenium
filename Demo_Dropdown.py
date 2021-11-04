from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.select import Select

class DemoDropDown():
    def demo_dropDown(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.salesforce.com/in/form/signup/freetrial-sales/?d=topnav2-btn-ft")
        drpdn = driver.find_element_by_name("UserTitle")
        dd = Select(drpdn)
        time.sleep(3)

        dd.select_by_index(1)
        time.sleep(3)


        dd.select_by_visible_text("Marketing / PR Manager")
        time.sleep(3)


        dd.select_by_value("CxO_General_Manager_AP")
        time.sleep(3)


demo = DemoDropDown()
demo.demo_dropDown()