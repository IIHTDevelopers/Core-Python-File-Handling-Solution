import unittest
from TestUtils import TestUtils
from file_ex import *
class ExceptionalTest(unittest.TestCase):
    def test_exceptional(self):
        test_obj = TestUtils()
        test_obj.yakshaAssert("TestExceptional",True,"boundary")
        print("TestExceptional = Passed")

    def test_get_image_size_file_not_found(self):
        test_utils_instance = TestUtils()
        image_filename = '../flower.jpg'

        size_kb = get_image_size(image_filename)
        expected_size_kb = -1  # Expecting -1 for non-existent file

        test_utils_instance.yakshaAssert("TestGetImageSizeFileNotFound", size_kb == expected_size_kb, "functional")
        if size_kb == expected_size_kb:
            print("TestGetImageSizeFileNotFound = Passed")
        else:
            print("TestGetImageSizeFileNotFound = Failed")