from calc import add


def test_add_whole_numbers():
    assert add(1, 2) == 3


def test_add_negative():
    assert add(-5, 2) == -3
