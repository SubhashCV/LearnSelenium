import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class elemnts_list():
    def fun1(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.yatra.com/")
        list1 = driver.find_elements_by_tag_name("a")
        list2 = driver.find_elements_by_tag_name("input")
        print(len(list1))
        for i in list1:
            print(i.text)
        time.sleep(5)

publicElements = elemnts_list()
publicElements.fun1()
