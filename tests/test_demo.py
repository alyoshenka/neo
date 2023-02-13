"""Tests for main module"""

from aws_iot.demo import sub_pub as app

def test_demo():
    """Tests that main() runs without errors"""
    try:
        app(wait=0)
    except Exception as err:
        print(err)
        assert False
