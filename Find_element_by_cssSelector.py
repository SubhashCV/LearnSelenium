import time
from selenium import  webdriver
from webdriver_manager.chrome import ChromeDriverManager

class DemoCss_Selector():
    def selectoe(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element_by_css_selector("#login-input").send_keys("venkat")
        time.sleep(4)

fend = DemoCss_Selector()
fend.selectoe()
