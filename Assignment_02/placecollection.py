"""..."""
from Assignment_02.place import Place
import csv

# Create your PlaceCollection class in this file


class PlaceCollection:
    """..."""
    def __init__(self, places=[]):
        self.places = places

    def __repr__(self):
        return str(self.places)

    def load_places(self, file):
        with open(file, 'r') as f:
            reader = csv.reader(f)
            self.places = list(reader)



    pass
