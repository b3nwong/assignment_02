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
            for i in self.places:
                i[2] = int(i[2])
                if i[3] == 'n':
                    i[3]= 'Unvisited'   # change 'n' to 'unvisited' to match rest of the list
                elif i[3] == 'v':
                    i[3] = 'Visited'    # change'v'to 'visited' to match rest of the list
            return self.places

    def save_file(self, file):
        with open(file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(self.places)
        print("Your file has been updated and saved!")

    def add_place(self, location):
        """add a single place to the places attribute"""
        temp_list = []
        temp_list.append(location.name)
        temp_list.append(location.country)
        temp_list.append((location.priority))
        temp_list.append(location.check_visited())
        self.places.append(temp_list)

    def sort_priority(self, list_to_sort):
        """sort the list based on the 'priority' object in ascending"""
        from operator import itemgetter
        list_to_sort.sort(key=itemgetter(2))
        return list_to_sort

    def sort_alphabetically(self, list_to_sort):
        """sort the list in alphabetical order"""
        list_to_sort.sort()
        return list_to_sort
    def sort_visited(self, list_to_sort):
        """sort the list according to visited or not"""
        from operator import itemgetter
        list_to_sort.sort(key=itemgetter(3), reverse = False)
        return list_to_sort
    pass
