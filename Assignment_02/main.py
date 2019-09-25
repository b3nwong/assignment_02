from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from Assignment_02.placecollection import PlaceCollection
from Assignment_02.place import Place

class TravelTrackerApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        travel_locations = PlaceCollection()
        self.app_list = travel_locations.load_places('places.csv')


    def build(self):
        self.title = "Travl Tracker App"
        self.root = Builder.load_file('app.kv')
        self.create_widgets()
        return self.root

  #  def sort_method_priority(self):
    # call sorting method from placecollection
    #change display on sorting label

    def clear_input(self):
        self.root.ids.input_name.text = ""
        self.root.ids.input_country.text = ""
        self.root.ids.input_priority.text = ""

    def create_widgets(self):
        """ Create buttons from list of objects and add them to the GUI."""
        #todo self.status_text = "Click on a guitar to reduce its cost by {:.1%}%".format(1 - DISCOUNT_RATE)
        for location in self.app_list:
           #Create a button for each PlaceCollection object, specifying the text
           temp_button = Button(text= "{} in {}, priority {} ({})".format(location[0],location[1],location[2],location[3]))
           temp_button.bind(on_release=self.press_entry)
         # Store a reference to the location object in the button object
           temp_button.location = location
           self.root.ids.entries_box.add_widget(temp_button)


    def press_entry(self, instance):
        """this function will change the place's visited/unvisited status upon pressing"""
        # Each button was given its own ".location" object reference, so we can get it directly
        location = instance.location
        if location[3] == "Visited":
            location[3] = "Unvisited"
            #changes the value to "visited" or "unvisted" and vice versa
        else:
            location[3] = "Visited"
        # Update button text and label
        instance.text = "{} in {}, priority {} ({})".format(location[0],location[1],location[2],location[3])



TravelTrackerApp().run()