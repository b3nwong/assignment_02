"""(Incomplete) Tests for PlaceCollection class."""
from Assignment_02.placecollection import PlaceCollection
from Assignment_02.place import Place

import csv

def run_tests():
    """Test PlaceCollection class."""

    # Test empty PlaceCollection (defaults)
    print("Test empty PlaceCollection:")
    place_collection = PlaceCollection()
    print(place_collection)
    assert not place_collection.places  # an empty list is considered False

    # Test loading places
    print("Test loading places:")
    place_collection.load_places('places.csv')
    print(place_collection)
    assert place_collection.places  # assuming CSV file is non-empty, non-empty list is considered True

    # Test adding a new Place with values
    print("Test adding new place:")
    place_collection.add_place(Place("Smithfield", "Australia", 5, False))
    print(place_collection)

    # Test sorting places
    print("Test sorting - priority:")
    from operator import itemgetter
    place_collection.sort(key=itemgetter(2))
    print(place_collection)
    # TODO: Add more sorting tests

    # TODO: Test saving places (check CSV file manually to see results)

    # TODO: Add more tests, as appropriate, for each method


run_tests()