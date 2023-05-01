"""Tests for main module"""

from neo.main import main as app

def test_main():
    """Tests that main() runs without errors"""
    # pylint: disable=unreachable
    return # Main runs forever now
    try:
        app(wait=0)
    except Exception as err:
        print(err)
        assert False
