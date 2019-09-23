"""class to track whether location has been visited by user and assign priority"""

# Create your Place class in this file

class Place:
    """construct a Place class from the given values."""
    def __init__(self, name="", country="", priority=0, is_visited=False):
        self.name = name
        self.country = country
        self.priority = priority
        self.is_visited = is_visited

    def __str__(self):
        """return string representation of location."""
        return "{} in {}, priority {}{}".format(self.name, self.country, self.priority, self.check_visited())

    def __repr__(self):
        """so the objects in list will be in string form"""
        return str(self)

    def check_visited(self):
        """mark the place as visited"""
        if self.is_visited == False:
            return ""
            #does not state if place is unvisited like the sample output
        if self.is_visited == True:
            return "(Visited)"


    def is_important(self):
        """if a place has priority <= 2 it will be added to this list"""
        important = []
        if self.priority <= 2:
            important.append(self)
        return important

    pass
