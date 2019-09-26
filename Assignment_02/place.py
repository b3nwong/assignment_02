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
        return "{},{},{},{}".format(self.name, self.country, self.priority, self.check_visited())

    def __repr__(self):
        """so the objects in list will be in string form"""
        return str(self)

    def str_visit_to_bool(self):
        """so that the'v' and 'n' input for marking visit status we store in the list is converted back into boolean"""
        if self.is_visited == 'v':
            self.is_visited = True
            return self.is_visited
        elif self.is_visited == 'n':
            self.is_visited = False
            return self.is_visited

    def check_visited(self):
        """mark the place as visited"""
        self.str_visit_to_bool()  #slotted the function in here so that "v" and "n" values are caught when printing
        if self.is_visited == False:
            return "Unvisited"
        if self.is_visited == True:
            return "Visited"

    def is_important(self):
        """if a place has priority <= 2 it will be added to this list"""
        if self.priority <= 2:
            return True

    pass
