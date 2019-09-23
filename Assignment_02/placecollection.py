"""..."""
from Assignment_02.place import Place
import csv

# Create your PlaceCollection class in this file

travel_list = []


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
            loaded_list = list(reader)
            #sort out these list items to fit the format of places in Place class
            length = len(loaded_list)
            sub_length =len(loaded_list[0])
            true_list= []
            for i in range(length):
                temp_list=[]
                for j in range(sub_length):
                    temp_list.append(loaded_list[i][j])
                true_list.append(temp_list)
                print(true_list)


    def add_place(self, location):
        """add a single place to the places attribute"""
        temp_list = []
        temp_list.append(location.name)
        temp_list.append(location.country)
        temp_list.append(str(location.priority))
        temp_list.append(location.is_visited)
        self.places.append(temp_list)

    def take_priority(self, list_elem):
        return list_elem[2]
    pass
