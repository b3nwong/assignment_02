from kivy.app import App
from kivy.lang import Builder
from Assignment_02.placecollection import PlaceCollection
from Assignment_02.place import Place

class TravelTrackerApp(App):

    def build(self):
        self.title = "Travl Tracker App"
        self.root = Builder.load_file('app.kv')
        return self.root

    def sort_method_

TravelTrackerApp().run()