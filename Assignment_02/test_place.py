"""(Incomplete) Tests for Place class."""
from Assignment_02.place import Place


def run_tests():
    """Test Place class."""

    # Test empty place (defaults)
    print("Test empty place:")
    default_place = Place()
    print(default_place)
    assert default_place.name == ""
    assert default_place.country == ""
    assert default_place.priority == 0
    assert not default_place.is_visited

    # Test initial-value place
    print("Test initial-value place:")
    new_place = Place("Malagar", "Spain", 1, False)
    # TODO: Write tests to show this initialisation works
    print(new_place) #string representation of place
    print(new_place.check_visited()) #check if place is visited, if unvisited should be blank
    print(new_place.is_important()) #important place is added to this list
    # TODO: Add more tests, as appropriate, for each method


run_tests()