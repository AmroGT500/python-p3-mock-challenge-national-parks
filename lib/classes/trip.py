# trip.py
from classes.visitor import Visitor
from classes.national_park import NationalPark

class Trip:
    def __init__(self, visitor, national_park, start_date, end_date):
        self._visitor = visitor
        self._national_park = national_park
        self.start_date = start_date
        self.end_date = end_date

    @property
    def visitor(self):
        return self._visitor

    @visitor.setter
    def visitor(self, new_visitor):
        if isinstance(new_visitor, Visitor):
            self._visitor = new_visitor
        else:
            raise Exception("Visitor must be of type Visitor")

    @property
    def national_park(self):
        return self._national_park

    @national_park.setter
    def national_park(self, new_national_park):
        if isinstance(new_national_park, NationalPark):
            self._national_park = new_national_park
        else:
            raise Exception("NationalPark must be of type NationalPark")
