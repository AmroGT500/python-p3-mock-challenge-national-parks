# national_park.py
from classes.trip import Trip
from classes.visitor import Visitor

class NationalPark:
    def __init__(self, name):
        self._name = name
        self._trips = []
        self._visitors = []
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if hasattr(self, "_name"):
            raise Exception("Cannot change name")
        else:
            raise Exception("Name should not be able to change after NationalPark is created")

    def trips(self):
        return [trip for trip in self._trips if isinstance(trip, Trip)]

    def visitors(self):
        unique_visitors = list(set([trip.visitor for trip in self._trips if isinstance(trip.visitor, Visitor)]))
        return unique_visitors

    def total_visits(self):
        return len(self._trips)

    def best_visitor(self):
        visitor_count = {}
        for trip in self._trips:
            visitor = trip.visitor
            if visitor in visitor_count:
                visitor_count[visitor] += 1
            else:
                visitor_count[visitor] = 1
        sorted_visitors = sorted(visitor_count.items(), key=lambda x: x[1], reverse=True)
        if sorted_visitors:
            return sorted_visitors[0][0]
        else:
            return None
