import time
from  selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class hidde_ele():
    def ele_dsplayed(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")
        ele1 = driver.find_element_by_xpath("//div[@id='myDIV']").is_displayed()
        print(ele1)
        time.sleep(4)
        driver.find_element(By.XPATH,"//button[normalize-space()='Toggle Hide and Show']").click()
        ele2 = driver.find_element_by_xpath("//div[@id='myDIV']").is_displayed()
        print(ele2)
        time.sleep(2)

    def ele_dsplayed_yatra(self):
        driver =webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.yatra.com/hotels")
        driver.find_element(By.XPATH,"//label[normalize-space()='Traveller and Hotel']").click()
        driver.find_element_by_xpath("//div[@class='hotel_passengerBox dflex relative']//div[3]//div[1]//div[1]//span[2]").click()
        elem1 = driver.find_element(By.XPATH,"//select[@class='ageselect']").is_displayed()
        print(elem1)
        time.sleep(4)
        driver.find_element(By.XPATH,"//div[@class='hotel_passengerBox dflex relative']//div[3]//div[1]//div[1]//span[1]").click()
        elem2 = driver.find_element(By.XPATH,"//select[@class='ageselect']").is_displayed()
        print(elem2)
        time.sleep(2)
display = hidde_ele()
#display.ele_dsplayed()
display.ele_dsplayed_yatra()