# test_app.py
from app import add  # Assuming you have an add function in app.py

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    # Add more tests as needed
    pass