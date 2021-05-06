from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
import json
import time
import requests
from requests.structures import CaseInsensitiveDict
import urllib3

class Comestic:
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path=r"C:\Users\nguyentan.khoi\PycharmProjects\SeleniumProject\Driver\geckodriver.exe")

    # ------------------------------------------------------------ Brand ----------------------------------------------------
    def login(self):

        self.driver.find_element_by_id("btnlogin").click()
        self.driver.find_element_by_id("username").send_keys("ADMIN")
        self.driver.find_element_by_id("pwd").send_keys("1")
        self.driver.find_elements_by_id("button")[0].click()

    def checkingCreateNullData(self):
        self.driver.get("https://localhost:44394/brand")
        self.login()

        time.sleep(5)  # sleep 10s
        self.driver.find_element_by_id("tthm").click()
        self.driver.find_element_by_id("tdm").click()
        self.driver.quit()
        return True

    def checkingCreateNullData_1(self):
        self.driver.get("https://localhost:44394/api/Brand/searchBrand/100,1")
        allBrand = []
        resultJSON = self.driver.find_element_by_id("json").text
        listBrandReturn = json.loads(str(resultJSON))
        for i in range(0, len(listBrandReturn["data"])):
            brandIdCheck = listBrandReturn["data"][i].get("brandId")
            if (brandIdCheck == ""):
                allBrand.append(listBrandReturn["data"][i])
        self.driver.quit()
        if (allBrand != []):
            return False
        return True


    def checkDeleteWithBrandIdIsNull(self):
        self.driver.get("https://localhost:44394/brand")
        self.login()
        self.driver.find_element_by_xpath("/html/body/app-root/body/div/app-brand-data/table/tbody/tr[1]/td[5]/button[3]").click()
        self.driver.switch_to.alert.accept()
        time.sleep(40)
        self.driver.quit()

    def checkDeleteBrandFollowId(self, id):
        urlLogin = "http://localhost:44394/api/Personal_Information/Login"
        headers = CaseInsensitiveDict()
        headers["Content-Type"] ="application/json"
        auth = {
          "account": "mitsu",
          "password": "asus.123"
        }

        contentAfterlogin = requests.post(urlLogin, data=json.dumps(auth, indent=10), headers=headers)
        myToken = json.loads(contentAfterlogin.text)

        # objCompare = json.loads(str(requests.get("http://localhost:44394/api/Brand/searchBrand/100,1?keyWord="+ str(id)).text))

        url = "http://localhost:44394/api/Brand/deleteBrand/" + str(id)
        headers[
            "Authorization"] = "Bearer "+ myToken["token"]

        resp = requests.delete(url, headers=headers)

        if (resp.status_code == 500):
            return resp.reason
        elif (resp.status_code == 200):
            if(resp.text == "Unable to delete: not found ID."):
                return "not found ID"

        return None

    def checkUpdateBrandFollowId(self, id, req):


        urlLogin = "http://localhost:44394/api/Personal_Information/Login"
        headers = CaseInsensitiveDict()
        headers["Content-Type"] = "application/json"
        auth = {
            "account": "ADMIN",
            "password": "1"
        }

        contentAfterlogin = requests.post(urlLogin, data=json.dumps(auth, indent=10), headers=headers)
        myToken = json.loads(contentAfterlogin.text)

        headers[
            "Authorization"] = "Bearer " + myToken["token"]

        url = "http://localhost:44394/api/Brand/updateBrandPut/"+str(id)
        resPut = requests.put(url, data=json.dumps(req,indent=10), headers=headers)

        return resPut
    # ---------------------------------------------------------- Category --------------------------------------------------
    def checkingCreateCategoryNullData(self):
        self.driver.get("https://localhost:44394/category")
        self.login()


        self.driver.find_element_by_id("tdmm").click()
        self.driver.find_element_by_id("tdm").click()
        # self.driver.quit()
        return True

    def checkCreateCatgoryNullData_1(self):
        self.driver.get("https://localhost:44394/api/Category/searchCategory/100,1")
        allCategory = []
        resultJSON  =self.driver.find_element_by_id("json").text
        listCategoryReturn = json.loads(str(resultJSON))
        for i in range(0, len (listCategoryReturn["data"])):
            categoryIdCheck = listCategoryReturn["data"][i].get("categoryId")
            if(categoryIdCheck == ""):
                allCategory.append(listCategoryReturn["data"][i])
        self.driver.quit()
        if (allCategory != []):
            return False
        return True
    def checkDeleteCatgoryFollowId(self, id):
        urlLogin = "http://localhost:44394/api/Personal_Information/Login"
        headers = CaseInsensitiveDict()
        headers["Content-Type"] = "application/json"
        auth = {
            "account": "mitsu",
            "password": "asus.123"
        }
        contentAfterlogin = requests.post(urlLogin, data=json.dumps(auth, indent=10), headers=headers)
        myToken = json.loads(contentAfterlogin.text)
        url = "http://localhost:44394/api/Category/deleteCategory/" + str(id)
        headers[
            "Authorization"] = "Bearer " + myToken["token"]
        resp = requests.delete(url, headers=headers)

        if (resp.status_code == 500):
            return resp.reason
        elif (resp.status_code == 200):
            if (resp.text == "Unable to delete: not found ID."):
                return "not found ID"

        return None

    def checkUpdateCategoryFollowId(self, id, req):
        urlLogin = "http://localhost:44394/api/Personal_Information/Login"
        headers = CaseInsensitiveDict()
        headers["Content-Type"] = "application/json"
        auth = {
            "account": "ADMIN",
            "password": "1"
        }

        contentAfterlogin = requests.post(urlLogin, data=json.dumps(auth, indent=10), headers=headers)
        myToken = json.loads(contentAfterlogin.text)

        headers[
            "Authorization"] = "Bearer " + myToken["token"]
        url = "http://localhost:44394/api/Category/updateCategoryPut/" + str(id)
        resPut = requests.put(url, data=json.dumps(req, indent=10), headers=headers)

        return resPut