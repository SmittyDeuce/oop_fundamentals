# 1. City Infrastructure Management System
# Objective:
# The aim of this assignment is to apply the concepts of Object-Oriented Programming in Python to build a simulated City Infrastructure Management System. This system will incorporate classes, objects, methods, and data structures to manage different aspects of a city, such as buildings, traffic, and events.

# Task 1: Vehicle Registration System

# Problem Statement: Create a Python class Vehicle with attributes registration_number, type, and owner. Implement a method update_owner to change the vehicle's owner. Then, create a few instances of Vehicle and demonstrate changing the owner.
# Code Example: Provide a basic structure for the Vehicle class without methods.
# ```python
# class Vehicle:
# def init(self, reg_num, type, owner):
# self.registration_number = reg_num
# self.type = type
# self.owner = owner
# ```
# Expected Outcome: Completion of the Vehicle class with the update_owner method and a demonstration script showing the creation of Vehicle objects and updating their owners.
# 

class Vehicle:
    def __init__ (self, registration_num, type, owner):
        self.registration_number = registration_num
        self.type = type
        self.owner = owner

    def new_owner(self):
        updated_owner = input("Who is new Owner: ")
        self.owner = updated_owner


vehicle1 = Vehicle("asfdwer", "truck", "joe")

print("first Owner: ",vehicle1.owner)

vehicle1.new_owner()
print("2nd Owner: ", vehicle1.owner)


vehicle1.new_owner()
print("3rd Owner: ", vehicle1.owner)

vehicle1.new_owner()
print("Last Owner: ", vehicle1.owner)








# Task 2: Event Management System Enhancement

# Problem Statement: Extend an existing Event class by adding a feature to keep track of the number of participants. Implement a method add_participant that increases the count and a method get_participant_count to retrieve the current count.
# Code Example: Basic Event class without participant tracking.
# ```python
# class Event:
# def init(self, name, date):
# self.name = name
# self.date = date
# ```
# 2. Python City Planning Simulator
# Objective:
# The aim of this assignment is to solidify understanding of Python's Object-Oriented Programming concepts through the development of a simulated city planning system. This system will integrate the use of classes, objects, inheritance, and file handling to manage various city elements like buildings, traffic systems, and public events.

# Task 1: File Handling for Building Records

# Problem Statement: Implement a system to handle building records using file operations. Create a Building class and write a script to save and load building details to and from a file.
# Code Example: Skeleton of the Building class.
# ```python
# class Building:
# def init(self, name, floors):
# self.name = name
# self.floors = floors
# # Methods to save to file and load from file
# ```
# Expected Outcome: A complete Building class with methods for saving to and loading details from a file. A script demonstrating saving multiple buildings to a file and then reading them back into the program.
# 3. City Services Simulation: Python OOP and Modular Design
# Objective:
# This assignment aims to strengthen your skills in Python Object-Oriented Programming (OOP) and modular programming by building a simulation of city services. The focus will be on using class variables and organizing code into modules, simulating services like public transportation, park management, and city utilities.

# Task 1: Public Transportation Module

# Problem Statement: Develop a Bus class as part of a public transportation module. Use class variables to represent common attributes like city name and base fare. Implement instance variables for specific attributes like route number and passenger capacity.
# Expected Outcome: A Bus class with both class and instance variables, and a transportation module to manage different bus routes. A test script should demonstrate creating bus instances and accessing both class and instance attributes.
