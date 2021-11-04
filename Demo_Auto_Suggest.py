from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class DemoAutoSuggets():
    def demo_AutoSuggest(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.yatra.com/")
        depart = driver.find_element(By.XPATH,"//input[@id='BE_flight_origin_city']")
        depart.click()
        time.sleep(3)
        depart.send_keys("New Delhi")
        time.sleep(3)
        depart.send_keys(Keys.ENTER)
        time.sleep(3)


        going_to = driver.find_element_by_xpath("//input[@id='BE_flight_arrival_city']")
        going_to.send_keys("New")
        time.sleep(4)
        search_results = driver.find_elements(By.XPATH,"//div[@class='viewport']//div[1]/li")
        print(len(search_results))
        for results in search_results:
            print(results.text)
            if "New York (JFK)" in results.text:
                results.click()
                time.sleep(4)
                break

Demo = DemoAutoSuggets()
Demo.demo_AutoSuggest()
        