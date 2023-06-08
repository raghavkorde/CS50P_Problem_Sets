from bank import value


def test_startWithHello():
    assert value("Hello") == 0
    assert value('Hello, Newman') == 0
    assert value('Hello, Potter') == 0

def test_startWithH():
    assert value('Hey') == 20
    assert value('How are you?') == 20
    assert value('How you doing?') == 20

def test_random():
    assert value('What?') == 100
    assert value("What's happening?") == 100
    assert value('Quiet') == 100


