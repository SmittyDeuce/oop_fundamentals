import os
import transportation
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

# print("first Owner: ",vehicle1.owner)

# vehicle1.new_owner()
# print("2nd Owner: ", vehicle1.owner)


# vehicle1.new_owner()
# print("3rd Owner: ", vehicle1.owner)

# vehicle1.new_owner()
# print("Last Owner: ", vehicle1.owner)




# Task 2: Event Management System Enhancement

# Problem Statement: Extend an existing Event class by adding a feature to keep track of the number of participants. Implement a method add_participant that increases the count and a method get_participant_count to retrieve the current count.
# Code Example: Basic Event class without participant tracking.
# ```python
# class Event:
# def init(self, name, date):
# self.name = name
# self.date = date
# ```

class Event:
    def __init__(self, name, Date):
        
        self.name = name
        self.date = Date
        self.participant_count = 1 # I made 1 because when declaring lottery as an event I have to pass in a partipant
        self.participants = [self.name]
    def add_participant(self):
       participants = [self.name]
       while True:
           participant = input("enter partipant name: (enter 'done' when finished) ")
           if participant.lower() == 'done':
               break
           
           else:
               print(f"{participant} added")
               self.participants.append(participant)
               self.participant_count += 1

    def get_participant_count(self):
        return self.participant_count, self.participants





# lottery = Event("Mike", "10-3-24")

# lottery.add_participant()

# print(f"Participants: {lottery.get_participant_count()}")






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

class Buildings:
    def __init__ (self, name, floors):
        self.name = name
        self.floors = int(floors)

    def add_builiding_file(self):
        while True:
            building_name = input("Enter building name: (enter 'done' when finished) ")
            if building_name == 'done':
                break
            else:
                try:
                    building_floors = int(input("How many floors?: "))
                except ValueError:
                    print("Error: floors has to be a number")
                    continue
                if not os.path.isfile("buildings.txt"):
                    with open("buildings.txt", 'w') as file:
                        file.write(f"{building_name}: {building_floors}\n")
                else:
                    with open("buildings.txt", "a") as file:
                        file.write(f"{building_name}: {building_floors}\n")


    def load_building_file(self):
        file_name = input("enter file name: (include extension) ")

        if os.path.isfile(file_name):
            with open(file_name, 'r') as file:
                for line in file:
                    print(line)

        else:
            print(f"{file_name} not found try again")
            

building = Buildings("", 0)

# building.add_builiding_file()
# building.load_building_file()






# 3. City Services Simulation: Python OOP and Modular Design
# Objective:
# This assignment aims to strengthen your skills in Python Object-Oriented Programming (OOP) and modular programming by building a simulation of city services. The focus will be on using class variables and organizing code into modules, simulating services like public transportation, park management, and city utilities.

# Task 1: Public Transportation Module

# Problem Statement: Develop a Bus class as part of a public transportation module. Use class variables to represent common attributes like city name and base fare. Implement instance variables for specific attributes like route number and passenger capacity.
# Expected Outcome: A Bus class with both class and instance variables, and a transportation module to manage different bus routes. A test script should demonstrate creating bus instances and accessing both class and instance attributes.


class Bus:
    def __init__ (self, base_fare, city_name):
        self.base_fare = int(base_fare)
        self.city_name = city_name



metro = Bus(15, "Hemet")
greys = Bus(45, "orlando" )
apple = Bus(100, "New York")
southern = Bus(5, "McAllen")

transportation.travel_destinations(metro.base_fare, metro.city_name)
transportation.travel_destinations(greys.base_fare, greys.city_name)
transportation.travel_destinations(apple.base_fare, apple.city_name)
transportation.travel_destinations(southern.base_fare, southern.city_name)

