"""
Wong Jie An
26/09/2019
this program tracks where the user has been and places they hope to visit in future and runs it on a kivy app
https://github.com/b3nwong/assignment_02/tree/master/Assignment_02
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty
from Assignment_02.placecollection import PlaceCollection
from Assignment_02.place import Place

class TravelTrackerApp(App):
    status_text = StringProperty()
    current_sort = StringProperty()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        travel_locations = PlaceCollection()
        self.app_list = travel_locations.load_places('places.csv')

    def build(self):
        """to build the kivy app"""
        self.title = "Travel Tracker App"
        self.root = Builder.load_file('app.kv')
        self.create_widgets()
        return self.root

    def clear_input(self):
        """to reset the text entry fields"""
        self.root.ids.input_name.text = ""
        self.root.ids.input_country.text = ""
        self.root.ids.input_priority.text = ""

    def create_widgets(self):
        """ Create buttons from list of objects and add them to the GUI."""
        self.status_text = "Click on a place to change it to visited/unvisited."
        for location in self.app_list:
           #Create a button for each PlaceCollection object, specifying the text
           temp_button = Button(text="{} in {}, priority {} ({})".format(location[0],location[1],location[2],location[3]))
           temp_button.bind(on_release=self.press_entry)
         # Store a reference to the location object in the button object
           temp_button.location = location
           if location[3] == "Unvisited":
               #if location is visited, button will now be different color
                temp_button.background_color = [1,0,0,1]
           else:
               temp_button.background_color = [1,1,1,1]
           self.root.ids.entries_box.add_widget(temp_button)


    def press_entry(self, instance):
        """this function will change the place's visited/unvisited status upon pressing"""
        # Each button was given its own ".location" object reference, so we can get it directly
        location = instance.location
        if location[3] == "Visited":
            location[3] = "Unvisited"
            #changes the value to "visited" or "unvisted" and vice versa
            #also changes color on press
        else:
            location[3] = "Visited"
        # Update button text and label
        self.root.ids.entries_box.clear_widgets()
        # gets rid of the old widgets
        self.create_widgets()
        if self.is_important(location[2]) == True:
            #if location is important, it will display a different msg
            if location[3] == "Visited":
                self.status_text = "You visited {}. Great travelling!".format(location[0])
            elif location[3] == "Unvisited":
                self.status_text = "You need to visit {}. Get going!".format(location[0])
        else:
            if location[3] == "Visited":
                self.status_text = "You visited {}.".format(location[0])
            #will print this if not impt and unvisited
            elif location[3] == "Unvisited":
                self.status_text = "You need to visit {}.".format(location[0])

    def add_place(self):
        """insert a new location into the list"""
        temp_list = []
        name = self.root.ids.input_name.text
        country = self.root.ids.input_country.text
        try:
            priority = int(self.root.ids.input_priority.text)
            if name == "" or country == "" or priority == "":
                self.status_text = "All fields must be filled in."
            elif priority <= 0:
                self.status_text = "INVALLD number input."
            else:
                temp_list.append(name)
                temp_list.append(country)
                temp_list.append(priority)
                temp_list.append("Unvisited")
                self.app_list.append(temp_list)
                self.root.ids.entries_box.clear_widgets()
                #gets rid of the old widgets
                self.create_widgets()
                #updates the location widgets with the new place
                self.status_text = "{} has been added.".format(name)
                #tells user they have managed to add their new location to visit
        except ValueError:
            #will be displayed if user enters incorrect input
            self.status_text = "Invalid input. Fill in all fields and a number is chosen for 'Priority'."
        self.root.ids.input_name.text = ""
        self.root.ids.input_country.text = ""
        self.root.ids.input_priority.text = ""

    def sort_priority(self):
        """sort the list based on the 'priority' object in ascending"""
        from operator import itemgetter
        self.app_list.sort(key=itemgetter(2))
        print(self.app_list)
        self.root.ids.entries_box.clear_widgets()
        # gets rid of the old widgets
        self.create_widgets()

    def sort_alphabetical(self):
        """sort the list on alphabetical order by name of places"""
        self.app_list.sort()
        print(self.app_list)
        self.root.ids.entries_box.clear_widgets()
        # gets rid of the old widgets
        self.create_widgets()

    def sort_visited(self):
        """sort the list according to visited or not"""
        from operator import itemgetter
        self.app_list.sort(key=itemgetter(3), reverse=False)
        print(self.app_list)
        self.root.ids.entries_box.clear_widgets()
        # gets rid of the old widgets
        self.create_widgets()

    def is_important(self,priority):
        """if a place has priority <= 2 it will be added to this list"""
        if priority <= 2:
            return True

    def on_stop(self):
        """writes the new csv file"""
        import csv
        with open('places.csv', 'w', newline='') as f:
            #takes out the empty row in between
            writer = csv.writer(f)
            writer.writerows(self.app_list)


TravelTrackerApp().run()