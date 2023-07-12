#!/usr/bin/env python3
import ipdb

from classes.national_park import NationalPark
from classes.visitor import Visitor
from classes.trip import Trip

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    # Create instances of NationalPark, Visitor, and Trip
    national_park = NationalPark("Yellowstone")
    visitor = Visitor("John Doe")
    trip = Trip(visitor, national_park, "2023-07-01", "2023-07-05")

    # Test the properties and methods
    print(national_park.name)  # Output: Yellowstone
    national_park.name = "Yosemite"  # Raises an exception because the name cannot be changed
    print(visitor.name)  # Output: John Doe
    visitor.name = "Jane Smith"  # Changes the visitor's name to Jane Smith
    print(visitor.name)  # Output: Jane Smith
    print(trip.visitor)  # Output: <Visitor object at ...>
    print(trip.national_park)  # Output: <NationalPark object at ...>
    national_park.trips(trip)  # Adds the trip to the national park's trips list
    trips = national_park.trips()  # Retrieves the list of trips associated with the national park
    print(len(trips))  # Output: 1
    print(trips[0].visitor)  # Output: <Visitor object at ...>
    print(trips[0].start_date)  # Output: 2023-07-01

    # Additional testing items
    trip.start_date = "2023-08-01"
    trip.end_date = "2023-08-05"
    print(trip.start_date)  # Output: 2023-08-01
    print(trip.end_date)  # Output: 2023-08-05

    trip2 = Trip(visitor, national_park, "2023-07-10", "2023-07-15")
    national_park.trips(trip2)
    trips = national_park.trips()
    print(len(trips))  # Output: 2
    for trip in trips:
        print(trip.start_date, trip.end_date)

    trips = visitor.trips()
    print(len(trips))  # Output: 2 (assuming visitor has made two trips)
    for trip in trips:
        print(trip.national_park.name, trip.start_date, trip.end_date)

    parks = visitor.national_parks()
    print(len(parks))  # Output: 2 (assuming visitor has visited two national parks)
    for park in parks:
        print(park.name)

    total_visits = national_park.total_visits()
    print(total_visits)  # Output: 2 (assuming the national park has two trips associated with it)

    best_visitor = national_park.best_visitor()
    print(best_visitor.name)  # Output: The name of the visitor who has visited the park the most

    # Start the ipdb debugger
    ipdb.set_trace()
