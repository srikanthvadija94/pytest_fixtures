import pytest
from .conftest import setup


@pytest.mark.usefixtures("setup")
class TestExample:

    def test_gmail(self):
        #self.driver.get("http://gmail.com")
        print("welcome to gmail")

    def test_online_course(self):
        #self.driver.get("http://gradeup.com")
        print("welcome to gradeup online courses")

    #
    # def test_selected_course(self):
    #     print("select courses ")
    #
    #
    # def test_add_cart(self):
    #     print("successfully added to cart")

