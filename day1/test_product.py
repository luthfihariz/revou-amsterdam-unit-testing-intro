import pytest
from product import Product


@pytest.fixture
def product():
    return Product("Test Product", 100, 10)


def test_product_creation(product):
    assert product.name == "Test Product"
    assert product.price == 100
    assert product.qty == 10


@pytest.mark.parametrize(
    "name, price, qty",
    [
        (123, 100, 10),  # Invalid name
        ("Test Product", -1, 10),  # Invalid price
        ("Test Product", 100, -1),  # Invalid quantity
    ],
)
def test_invalid_product_creation(name, price, qty):
    with pytest.raises(ValueError):
        Product(name, price, qty)


def test_apply_discount(product):
    product.apply_discount(10)
    assert product.price == 90


@pytest.mark.parametrize(
    "discount",
    [
        -1,  # Negative discount
        101,  # Discount greater than 100
        "10",  # Discount not a number
    ],
)
def test_invalid_discount(product, discount):
    with pytest.raises(ValueError):
        product.apply_discount(discount)


def test_update_description(product):
    product.update_description("This is a test product.")
    assert product.description == "This is a test product."


@pytest.mark.parametrize(
    "description",
    [
        123,  # Description not a string
        "a" * 301,  # Description longer than 300 characters
    ],
)
def test_invalid_description(product, description):
    with pytest.raises(ValueError):
        product.update_description(description)


def test_increase_qty(product):
    product.increase_qty(5)
    assert product.qty == 15


def test_decrease_qty(product):
    product.decrease_qty(5)
    assert product.qty == 5


@pytest.mark.parametrize(
    "amount",
    [
        -1,  # Negative amount
        "5",  # Amount not an integer
        15,  # Amount greater than current quantity
    ],
)
def test_invalid_qty_change(product, amount):
    with pytest.raises(ValueError):
        product.decrease_qty(amount)
