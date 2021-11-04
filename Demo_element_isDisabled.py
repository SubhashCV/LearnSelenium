from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

class DemoElementState():
    def demo_enable_disable(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://training.openspan.com/login")
        demo_state = driver.find_element_by_xpath("//input[@id='login_button']").is_enabled()
        print(demo_state)
        driver.get("https://secure.yatra.com/social/common/yatra/register")
        demo_state2 = driver.find_element()
        time.sleep(3)

demostate = DemoElementState()
demostate.demo_enable_disable()
