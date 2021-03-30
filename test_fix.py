import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time


@pytest.fixture(params=["chrome", "firfox"], scope="class")   # the fixture using N no of files, we use conftest.py
def setup(request):

    if request.param == "Chrome":
        wb_driver = webdriver.Chrome(ChromeDriverManager().install())
    if request.param == "Firefox":
        wb_driver = webdriver.Firefox(GeckoDriverManager().install())
    request.cls.driver = wb_driver
    yield
    time.sleep(5)
    wb_driver.close()
    wb_driver.quit()


# @pytest.fixture(scope="class")   # the fixture using N no of files, we use conftest.py
# def setup(request):
#     ch_driver = webdriver.Chrome(ChromeDriverManager().install())
#     request.cls.driver = ch_driver
#     yield
#     time.sleep(5)
#     ch_driver.close()
#     ch_driver.quit()
