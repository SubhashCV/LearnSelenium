from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.common.by import By

class Demo_MultiSelect():
    def demo_MultiSelect(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html")
        dd = driver.find_element_by_id("multi-select")
        dd_multi = Select(dd)
        dd_multi.select_by_index(0)
        dd_multi.select_by_value("Florida")
        dd_multi.select_by_visible_text("New Jersey")
        time.sleep(3)
        dd_multi.select_by_index(3)
        dd_multi.select_by_value("Ohio")
        dd_multi.select_by_visible_text("Texas")
        time.sleep(3)
        dd_multi.deselect_by_index(0)
        dd_multi.deselect_by_value("Florida")
        dd_multi.deselect_by_visible_text("New Jersey")
        time.sleep(3)
        dd_multi.deselect_all()

Demo = Demo_MultiSelect()
Demo.demo_MultiSelect()