import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time


# @pytest.fixture(scope="class")
# def setup():
#     print("I will be executing first")
#     yield
#     print(" I will execute last")


@pytest.fixture(scope="class")   # the fixture using N no of files, we use conftest.py
def setup(request):
    ch_driver = webdriver.Chrome(ChromeDriverManager().install())
    request.cls.driver = ch_driver
    yield
    time.sleep(5)
    ch_driver.close()
    ch_driver.quit()
