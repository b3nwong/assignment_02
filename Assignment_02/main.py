from kivy.app import App
from kivy.lang import Builder
from Assignment_02.placecollection import PlaceCollection
from Assignment_02.place import Place

class TravelTrackerApp(App):

    def build(self):
        self.title = "Travl Tracker App"
        self.root = Builder.load_file('app.kv')
        return self.root

  #  def sort_method_priority(self):
    # call sorting method from placecollection
    #change display on sorting label

    def clear_input(self):
        self.root.ids.input_name.text = ""
        self.root.ids.input_country.text = ""
        self.root.ids.input_priority.text = ""




TravelTrackerApp().run()