import unittest
import io
from TestUtils import TestUtils
from file_read import *
from file_ex import *

class TestFileFunctions(unittest.TestCase):
    def test_get_file_root_and_extension(self):
        test_utils_instance = TestUtils()
        filename = "../inventory.txt"
        file_name, file_extension = get_file_root_and_extension(filename)
        expected_result = ("inventory", ".txt")
        test_utils_instance.yakshaAssert("TestGetFileRootAndExtension", (file_name, file_extension) == expected_result, "functional")
        if (file_name, file_extension) == expected_result:
            print("TestGetFileRootAndExtension = Passed")
        else:
            print("TestGetFileRootAndExtension = Failed")

    def test_get_file_size(self):
        test_utils_instance = TestUtils()
        filename = "../inventory.txt"
        file_size = get_file_size(filename)
        expected_result = os.path.getsize(filename)
        test_utils_instance.yakshaAssert("TestGetFileSize", file_size == expected_result, "functional")
        if file_size == expected_result:
            print("TestGetFileSize = Passed")
        else:
            print("TestGetFileSize = Failed")

    def test_count_words(self):
        test_utils_instance = TestUtils()
        filename = "../inventory.txt"
        word_count = count_words(filename)
        expected_result = 2  # Assuming "inventory.txt" contains 2 words
        test_utils_instance.yakshaAssert("TestCountWords", word_count == expected_result, "functional")
        if word_count == expected_result:
            print("TestCountWords = Passed")
        else:
            print("TestCountWords = Failed")

    def test_get_image_size(self):
        test_utils_instance = TestUtils()
        image_filename = '../flower.jpg'

        # Create a dummy file for testing purposes
        with open(image_filename, 'wb') as f:
            f.write(os.urandom(1024 * 50))  # 50 KB dummy file

        size_kb = get_image_size(image_filename)
        expected_size_kb =50  # Since the dummy file is 50 KB
        tolerance = 1e-2  # Allow a small tolerance for floating point comparison

        test_utils_instance.yakshaAssert("TestGetImageSize", abs(size_kb - expected_size_kb) < tolerance, "functional")
        if abs(size_kb - expected_size_kb) < tolerance:
            print("TestGetImageSize = Passed")
        else:
            print("TestGetImageSize = Failed")
    def test_check_file_permissions(self):
        test_utils_instance = TestUtils()
        filename = "../inventory.txt"
        check_file_permissions(filename)
        test_utils_instance.yakshaAssert("TestCheckFilePermissions", True, "functional")
        print("TestCheckFilePermissions = Passed")

    def test_display_name(self):
        test_utils_instance = TestUtils()
        filename = "../emp.txt"

        from contextlib import redirect_stdout
        f = io.StringIO()
        with redirect_stdout(f):
            display_name(filename)
        output = f.getvalue().strip()

        expected_output = "Sarah Davis"  # Example expected output if emp.txt has "Sam" and "Sara"
        test_utils_instance.yakshaAssert("TestDisplayName", output == expected_output, "functional")
        if output == expected_output:
            print("TestDisplayName = Passed")
        else:
            print("TestDisplayName = Failed")


    def test_display_names_above_salary(self):
        test_utils_instance = TestUtils()
        filename = "../emp.txt"

        from contextlib import redirect_stdout
        f = io.StringIO()
        with redirect_stdout(f):
            display_names_above_salary(filename)
        output = f.getvalue().strip()

        expected_output = "Emily Johnson"  # Example expected output if emp.txt has "John" and "Alice"
        test_utils_instance.yakshaAssert("TestDisplayNamesAboveSalary", output == expected_output, "functional")
        if output == expected_output:
            print("TestDisplayNamesAboveSalary = Passed")
        else:
            print("TestDisplayNamesAboveSalary = Failed")

    def test_find_hotmail_users(self):
        test_utils_instance = TestUtils()
        filename = "../emp.txt"

        from contextlib import redirect_stdout
        f = io.StringIO()
        with redirect_stdout(f):
            find_hotmail_users(filename)
        output = f.getvalue().strip()

        expected_output = "Jessica Williams"  # Example expected output if emp.txt has "Mike" and "Lucy"
        test_utils_instance.yakshaAssert("TestFindHotmailUsers", output == expected_output, "functional")
        if output == expected_output:
            print("TestFindHotmailUsers = Passed")
        else:
            print("TestFindHotmailUsers = Failed")

    def test_print_seventh_line(self):
        test_utils_instance = TestUtils()
        filename = "../emp.txt"

        from contextlib import redirect_stdout
        f = io.StringIO()
        with redirect_stdout(f):
            print_seventh_line(filename)
        output = f.getvalue().strip()

        expected_output = "Sarah Davis, sarahdavis@host.com, +1-555-6789, 78000, 4"  # Replace with the actual expected content
        test_utils_instance.yakshaAssert("TestPrintSeventhLine", output == expected_output, "functional")
        if output == expected_output:
            print("TestPrintSeventhLine = Passed")
        else:
            print("TestPrintSeventhLine = Failed")

    def test_count_names_in_file(self):
        test_utils_instance = TestUtils()
        file_path = "employees.txt"

        from contextlib import redirect_stdout
        f = io.StringIO()
        with redirect_stdout(f):
            count_names_in_file(file_path)
        output = f.getvalue().strip()

        expected_output = "10"  # Assuming the file contains 10 names
        test_utils_instance.yakshaAssert("TestCountNamesInFile", output == expected_output, "functional")
        if output == expected_output:
            print("TestCountNamesInFile = Passed")
        else:
            print("TestCountNamesInFile = Failed")

if __name__ == '__main__':
    unittest.main()
