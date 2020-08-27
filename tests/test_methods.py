import sys
import os
import pytest
from pandas import DataFrame

# Add to path: current working directory.
sys.path.append(os.getcwd())
# Add to path: parent of current working directory.
sys.path.append(os.path.dirname(os.getcwd()))

from trundlerpy import Trundler

TRUNDLER_KEY = os.environ['TRUNDLER_KEY']

tr = Trundler(key=TRUNDLER_KEY)


# Test methods
def test_retailer():
    try:
        result = tr.retailer(5)
        assert isinstance(result, DataFrame)
    except:
        pytest.fail("Test failed \n", False)

    try:
        result = tr.retailer()
        assert isinstance(result, DataFrame)
    except:
        pytest.fail("Test failed \n", False)


def test_retailer_products():
    try:
        result = tr.retailer_products(5, product="coffee", brand="nespresso")
        assert isinstance(result, DataFrame)
    except:
        pytest.fail("Test failed \n", False)

    try:
        result = tr.retailer_products(5, head=True)
        assert isinstance(result, str)
    except:
        pytest.fail("Test failed \n", False)


def test_product():
    try:
        result = tr.product(530290)
        assert isinstance(result, DataFrame)
    except:
        pytest.fail("Test failed \n", False)


def test_products():
    try:
        result = tr.products(product="coffee", brand="nespresso|nescafe")
        assert isinstance(result, DataFrame)
    except:
        pytest.fail("Test failed \n", False)


def test_product_prices():
    try:
        result = tr.product_prices(530290)
        assert isinstance(result, DataFrame)
    except:
        pytest.fail("Test failed \n", False)


# Test exceptions
def test_retailer_exceptions():
    """Test retailer exceptions."""
    string = "string"
    integer = 1
    float = 0.1

    # Test Key is not supported
    key_dict = string
    value = integer

    with pytest.raises(Exception) as e:
        assert tr.retailer(**{
            key_dict: value})
    assert str(e.value) == f"\'{key_dict}\' is not supported"

    # Test Key type
    key_dict = 'id'
    value = float
    with pytest.raises(Exception) as et:
        assert tr.retailer(**{
            key_dict: value})
    assert str(et.value) == f"\'{key_dict}\' type must be <class \'int\'>."

    with pytest.raises(SystemExit) as e:
        assert tr.retailer(0)


def test_retailer_products_exceptions():
    """Test retailer_products exceptions."""
    string = "string"
    integer = 1
    float = 0.1

    # Test Required argument is missing.
    key_dict = string
    value = integer
    key_req = 'id'

    with pytest.raises(Exception) as e:
        assert tr.retailer_products(**{
            key_dict: value})
    assert str(e.value) == f"Required argument '{key_req}' is missing."

    # Test Key is not supported
    key_dict = string
    value = integer

    with pytest.raises(Exception) as e:
        assert tr.retailer(**{
            'id': 1,
            key_dict: value})
    assert str(e.value) == f"\'{key_dict}\' is not supported"

    # Test Key type
    key_dict = 'id'
    value = float
    with pytest.raises(Exception) as et:
        assert tr.retailer(**{
            key_dict: value})
    assert str(et.value) == f"\'{key_dict}\' type must be <class \'int\'>."


def test_product_exceptions():
    """Test product exceptions."""
    # Test Required argument is missing.
    key_req = 'id'

    with pytest.raises(Exception) as e:
        assert tr.product()
    assert str(e.value) == f"Required argument '{key_req}' is missing."


def test_product_prices_exceptions():
    """Test product_prices exceptions."""

    # Test Required argument is missing.
    key_req = 'id'

    with pytest.raises(Exception) as e:
        assert tr.product_prices()
    assert str(e.value) == f"Required argument '{key_req}' is missing."
