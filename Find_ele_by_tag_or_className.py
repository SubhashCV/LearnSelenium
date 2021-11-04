import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class find_ele_tag_OR_className():
    def tagO(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element_by_tag_name("input").send_keys("7386612486")
        time.sleep(5)
    def tag1(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element_by_class_name("email-login-box").send_keys("7997664349")
        time.sleep(5)


res = find_ele_tag_OR_className()
res.tagO()
res.tag1()