from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from  selenium.webdriver.common.by import By

class DemoCheckBox():
    def demo_checkbox(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.sugarcrm.com/au/request-demo/")
        driver.find_element_by_id("interest_market_c0").click()
        time.sleep(4)
        driver.find_element(By.ID,"interest_sell_c0").click()
        time.sleep(4)

    def demo_checkbox_2(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.sugarcrm.com/au/request-demo/")
        driver.find_element_by_id("interest_market_c0").click()
        var_1 = driver.find_element_by_id("interest_market_c0").is_selected()
        print(var_1)
        time.sleep(4)
        var_2 = driver.find_element(By.ID, "interest_sell_c0").is_selected()
        print(var_2)
        driver.find_element(By.ID,"interest_sell_c0").click()
        var_3 = driver.find_element(By.ID, "interest_sell_c0").is_selected()
        print(var_3)
        time.sleep(3)

demo = DemoCheckBox()
# demo.demo_checkbox()
demo.demo_checkbox_2()