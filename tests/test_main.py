"""Tests for main module"""

from aws_iot.main import main as app

def test_main():
    """Tests that main() runs without errors"""
    try:
        app(wait=0)
    except Exception as err:
        print(err)
        assert False
