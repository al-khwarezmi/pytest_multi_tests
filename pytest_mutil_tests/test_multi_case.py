# content of test_multi_params_case.py
import pytest
from params import get_config


@pytest.mark.parametrize("multi_tests", get_config())
def test_multi_case(multi_tests):
    """Demo Using same test for multible parameters"""
    assert multi_tests > 1
