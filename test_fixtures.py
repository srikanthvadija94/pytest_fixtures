import pytest

# -k stands for method name execution, -s logs in output and  -v standsfor info metadata
# -m to run mark tests
# fixture are used as setup and teardown methods for test cases
@pytest.fixture()
def test_setup():
    print("execute first")
    yield
    print("execute after all test cases")


def test_homepage(test_setup):
    print("welcom to world")

