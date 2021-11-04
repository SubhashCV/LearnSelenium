from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class DemoCalnder():
    def demo_calender(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.yatra.com/")
        origin = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_date']")
        origin.click()
        time.sleep(4)
        driver.find_element(By.XPATH,"//td[@id='21/10/2021']").click()
        time.sleep(4)

        all_dates = driver.find_elements(By.XPATH," self.error_handler.check_response(response)")
        FOR


# //div[@id='monthWrapper']//tbody//td[@class!='inActiveTD weekend']
demo = DemoCalnder()
demo.demo_calender()