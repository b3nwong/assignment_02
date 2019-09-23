"""..."""
from Assignment_02.place import Place
import csv

# Create your PlaceCollection class in this file


class PlaceCollection:
    """..."""
    def __init__(self, places=[]):
        self.places = places

    def __repr__(self):
        """Represent list as string values"""
        return str(self.places)

    def load_places(self, file):
        """load the obejcts from csv file into a list"""
        with open(file, 'r') as f:
            reader = csv.reader(f)
            self.places = list(reader)

    def add_place(self, location):
        """add a single place to the places attribute"""
        temp_list = []
        temp_list.append(location.name)
        temp_list.append(location.country)
        temp_list.append(location.priority)
        temp_list.append(location.is_visited)
        self.places.append(temp_list)


    pass
