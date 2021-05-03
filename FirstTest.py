from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path=r"C:\Users\nguyentan.khoi\PycharmProjects\SeleniumProject\Driver\geckodriver.exe")

driver.get("https://google.com.vn/")
driver.maximize_window()

driver.find_element_by_name("q").send_keys("Mitsubishi Electric Viet Nam")

driver.find_element_by_name("q").send_keys(Keys.ENTER)



