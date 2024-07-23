# 1. City Infrastructure Management System
#Objective: The aim of this assignment is to apply the concepts of 
# Object-Oriented Programming in Python to build a simulated City Infrastructure Management System. 
# This system will incorporate classes, objects, methods, and data structures to manage different 
# aspects of a city, such as buildings, traffic, and events.

# Task 1: Vehicle Registration System

#- Problem Statement: Create a Python class Vehicle with attributes 
# registration_number, type, and owner. 
# Implement a method update_owner to change the vehicle's owner. 
# Then, create a few instances of Vehicle and demonstrate changing the owner.

# Code Example: Provide a basic structure for the Vehicle class without methods.

class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner

    def update_owner(self, new_owner):
        self.owner = new_owner

vehicle = Vehicle("ABC456", "Sedan", "Matt Gomez")
print(f"Car registration: {vehicle.registration_number}, Car type: {vehicle.type} waz owned by {vehicle.owner}.")

vehicle.update_owner = ("Michael Smith")
print(f"Car registration: {vehicle.registration_number}, Car type: {vehicle.type} is now owned by {vehicle.update_owner}.")


    
# - Expected Outcome: Completion of the Vehicle class with the update_ownermethod and a 
# demonstration script showing the creation of Vehicle objects and updating their owners.

# Task 2: Event Management System Enhancement

# - Problem Statement: Extend an existing Event class by adding a feature to 
# keep track of the number of participants. 
# Implement a method add_participant that increases the count and a 
# method get_participant_count to retrieve the current count.

# - Code Example: Basic Event class without participant tracking.

class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participants = 23
        
    def add_participant(self):
        self.participants += 1

    def get_participant_count(self):
        return self.participants

event = Event("Annual Meeting 2024", "July 23 2024")

event.add_participant()
print(f"Event: {event.name}")
print(f"Date: {event.date}")
print(f"Total number of participants: {event.get_participant_count()}")