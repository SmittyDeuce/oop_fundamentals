# oop_fundamentals

## **Overview**
here is my attempt at Coding Temple's *"OOP Fundamentals"* coding assignment


## Introduction

The City Transportation System Simulator is a Python project that calculates travel fares between cities within the contiguous United States. It utilizes the GeoPy library for geocoding and distance calculation, providing users with estimated travel fares based on predefined fare structures.

## Overview

The project consists of a main script (`main.py`) and a `Vehicle` class. The main script interacts with users, prompting for input and calculating travel fares based on the distance between cities. The `Vehicle` class provides a basic structure for representing vehicles, including attributes such as registration number, type, and owner.

## How the Code Works

1. **User Input**: The main script prompts users to input departure and arrival cities.
2. **Distance Calculation**: Using the GeoPy library, the script calculates the distance between the input cities based on latitude and longitude coordinates.
3. **Fare Estimation**: Based on the calculated distance and predefined fare structures, the script estimates the travel fare.
4. **Output**: The estimated travel fare is displayed to the user.


# `main.py`


### Prompts user for departure and arrival cities.
### Calculates distance between cities using GeoPy library.
### Estimates travel fare based on distance and predefined fare structure.
### Displays estimated travel fare to the user.


# `transportation.py`

### Defines a Bus class with attributes for base fare and city name.
### Implements a function to calculate travel fare based on distance.
