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
    print(place_collection.places)

    # Test sorting places
    print("Test sorting - priority:")
    from operator import itemgetter
    place_collection.places.sort(key=itemgetter(2)) #so that the 3rd element of the list 'priority' can be used as the key to sort
    print(place_collection)
    """conducted 2 sorting method tests"""
    #Test alphabetical sorting
    print("Test sorting - alphabetical:")
    place_collection.sort_alphabetically(place_collection.places)
    print(place_collection)

    print("Test sorting - by visted status")
    place_collection.sort_visited(place_collection.places)
    print(place_collection)


    """save file from places list in csv file"""
    print("Test saving:")
    place_collection.save_file('places.csv') #new edited file is now saved and csv is updated!

    # TODO: Add more tests, as appropriate, for each method


run_tests()
