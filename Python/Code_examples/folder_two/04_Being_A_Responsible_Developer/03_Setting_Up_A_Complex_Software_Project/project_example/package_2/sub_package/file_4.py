# from package_2.file_3 import file_3_function
from ..file_3 import file_3_function


def file_4_function():
    file_3_function()
    print("package_2.file_4_function")
