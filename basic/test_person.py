import pytest
from person import Person


def test_person():
    person = Person("Alice", 20)

    # Test greet method
    assert person.greet() == "Hello, my name is Alice."

    # Test is_adult method
    assert person.is_adult() == True

    # Test birthday method
    person.birthday()
    assert person.age == 21

    # Test rename method
    person.rename("Alicia")
    assert person.name == "Alicia"

    # Test with a minor
    minor = Person("Bob", 15)
    assert minor.is_adult() == False

    # Test invalid name
    with pytest.raises(ValueError):
        Person(123, 20)

    # Test invalid age
    with pytest.raises(ValueError):
        Person("Charlie", -1)

    # Make a quiz to find which line is missed
    # with pytest.raises(ValueError):
    #     person.rename(123)
