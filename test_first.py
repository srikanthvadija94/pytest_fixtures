def test_first_program():
    msg = "hello"
    assert msg == "bye", "test failed bcoz of msg doesn't match"


def test_second_program():
    a = 10
    b = 8
    assert a+2 == 12, "addition done"
    assert b+2 == 10,  "addition done"
