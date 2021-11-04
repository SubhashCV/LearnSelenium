import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class Demo_Find_text():
    def findTXT(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        txt_1 = driver.find_element_by_xpath("//h1[contains(text(),'Book Flights, Hotels, Trains, Buses, Cruise and Ho')]").text
        print(txt_1)
        txt_2 = driver.find_element(By.TAG_NAME,"button").text
        print(txt_2)
        time.sleep(3)
        
webelements = Demo_Find_text()
webelements.findTXT()