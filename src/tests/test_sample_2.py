import pytest
import allure


@allure.title("Sample TestCase")
def test_sample():
    assert True == True