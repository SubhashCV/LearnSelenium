from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

class DemoRadioButtons():
    def demo_radio_butons(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.maximize_window()
        time.sleep(4)
        driver.get("https://www.sugarcrm.com/au/request-demo/")
        print(driver.find_element(By.ID,"doi0").is_selected())
        time.sleep(3)
        driver.find_element(By.ID,"doi0").click()
        print(driver.find_element(By.ID,"doi0").is_selected())
        time.sleep(4)
        print(driver.find_element_by_id("doi1").is_selected())
        time.sleep(4)
        driver.find_element_by_id("doi1").click()
        print(driver.find_element_by_id("doi1").is_selected())
        time.sleep(4)
        # doi1

demo = DemoRadioButtons()
demo.demo_radio_butons()
        