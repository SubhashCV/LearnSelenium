import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class browseRR():
    def metods_OR_properties(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        # driver.maximize_window()
        driver.get("https://training.rcvacademy.com/")
        print(driver.current_url)
        print(driver.title)
        driver.maximize_window()
        time.sleep(3)
        driver.fullscreen_window()
        time.sleep(2)
        driver.refresh()
        time.sleep(5)
        driver.find_element_by_link_text("ALL COURSES").click()
        time.sleep(3)
        driver.back()
        time.sleep(2)
        driver.forward()
        time.sleep(3)
        driver.minimize_window()
        time.sleep(5)
        driver.quit()

pro = browseRR()
pro.metods_OR_properties()