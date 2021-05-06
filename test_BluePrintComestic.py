import json
from unittest import TestCase

from BluePrintComestic import Comestic

class TestComestic(TestCase):
    # def test_checking_create_null_data(self):
    #     comesticObj = Comestic()
    #     self.assertEqual(comesticObj.checkingCreateNullData(), True)
    #
    # def test_cheking_create_null_data_1(self):
    #     comesticObj = Comestic()
    #     self.assertEqual(comesticObj.checkingCreateNullData_1(), True, "is existed data is null")
    #
    # def test_check_delete_with_brand_is_null(self):
    #     comesticObj = Comestic()
    #     comesticObj.checkDeleteWithBrandIdIsNull()

    # #is empty
    # def test_check_delete_brand_follow_id_1(self):
    #     comesticObj = Comestic()
    #     self.assertEqual(comesticObj.checkDeleteBrandFollowId(""), "Deleted")
    #
    # # is not found
    # def test_check_delete_brand_follow_id_2(self):
    #     comesticObj = Comestic()
    #     self.assertEqual(comesticObj.checkDeleteBrandFollowId("fasdfwwwwssw"), "not found ID")
    #
    # # Acnes
    # def test_check_delete_brand_follow_id_3(self):
    #     comesticObj = Comestic()
    #     self.assertEqual(comesticObj.checkDeleteBrandFollowId("Acnes"), None)
    #
    # #BAF
    # def test_check_delete_brand_follow_id_4(self):
    #     comesticObj = Comestic()
    #     self.assertEqual(comesticObj.checkDeleteBrandFollowId("BAF"), None)
    #
    # #CETAPHIL
    # def test_check_delete_brand_follow_id_5(self):
    #     comesticObj = Comestic()
    #     self.assertEqual(comesticObj.checkDeleteBrandFollowId("CETAPHIL"), None)

    #req is empty
    def test_check_update_brand_follow_id(self):
        comesticObj = Comestic()
        req = {

        }
        self.assertEqual(comesticObj.checkUpdateBrandFollowId("Acnes", req).status_code, 501, comesticObj.checkUpdateBrandFollowId("Acnes", req).text)

    #req has field error
    def test_check_update_brand_follow_id_1(self):
        comesticObj = Comestic()
        req = {
            "AASDWCVC": "2021-03-04"
        }
        self.assertEqual(comesticObj.checkUpdateBrandFollowId("Acnes", req).status_code, 501,comesticObj.checkUpdateBrandFollowId("Acnes", req).text)

    #update_success
    def test_check_update_brand_follow_id_2(self):
        comesticObj = Comestic()
        req = {
            "brandId": "Acnes",
            "name": "Acnes",
            "phoneNumber": "9012301",
            "email": "ffwwwfwwww",
            "description": "Sản phẩm trị mụn",
            "startedDate": "2021-05-05T00:00:00",
            "note": "",
            "product": None
        }
        self.assertEqual(comesticObj.checkUpdateBrandFollowId("Acnes", req).status_code, 200)
        print(comesticObj.checkUpdateBrandFollowId("Acnes", req).text)

    # not found id
    def test_check_update_brand_follow_id_3(self):
        comesticObj = Comestic()
        req = {

        }
        self.assertEqual(comesticObj.checkUpdateBrandFollowId("FCWWFWFFFADFW", req).status_code, 200)
        print(comesticObj.checkUpdateBrandFollowId("FCWWFWFFFADFW", req).text)
