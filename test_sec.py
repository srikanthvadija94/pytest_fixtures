import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.mark.mail
def test_setup():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("http://www.gmail.com")


@pytest.mark.xfail
def test_case():
    print("test completed")
