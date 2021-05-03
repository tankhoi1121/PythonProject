from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json

driver = webdriver.Firefox(executable_path=r"C:\Users\nguyentan.khoi\PycharmProjects\SeleniumProject\Driver\geckodriver.exe")
res = driver.get("https://chercher.tech/sample/api/product/read")


resultJSON = driver.find_element_by_id("json").text
dictX=  json.loads(str(resultJSON))
# print(dictX["records"])

print (len(dictX["records"]))

