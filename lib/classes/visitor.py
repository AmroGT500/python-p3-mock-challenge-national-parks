# visitor.py
from classes.trip import Trip
from classes.national_park import NationalPark

class Visitor:
    def __init__(self, name):
        self._name = name
        self._trips = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and 1 <= len(new_name) <= 15:
            self._name = new_name
        else:
            raise Exception("Name must be a string between 1 and 15 characters")

    def trips(self):
        return [trip for trip in self._trips if isinstance(trip, Trip)]

    def national_parks(self):
        visited_parks = [trip.national_park for trip in self._trips if isinstance(trip.national_park, NationalPark)]
        unique_parks = list(set(visited_parks))
        return unique_parks
