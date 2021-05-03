from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path=r"C:\Users\nguyentan.khoi\PycharmProjects\SeleniumProject\Driver\geckodriver.exe")

driver.get("https://localhost:44303/ModelEMC/Upload")

driver.find_element_by_name("ExcelFile").send_keys(r"C:\Users\nguyentan.khoi\Downloads\Test.xls")
