from geopy.distance import geodesic
from geopy.geocoders import Nominatim

destinations = Nominatim(user_agent="city_coordninates")
# New_York_City = (40.7128, -74.0060)
# Los_Angeles = (34.0522, -118.243)


def travel_destinations(base_fare, departure_city):

    additonal_fare = 0
    
    
    # departure = input("What city are you leaving from?: ")
    arrival = input("What city are you arriving at?: ")

    departure_location = destinations.geocode(departure_city + ", USA")
    arrival_location = destinations.geocode(arrival + ", USA")

    if departure_location and arrival_location:
        departure_coords = (departure_location.latitude, departure_location.longitude)
        arrival_coords = (arrival_location.latitude, arrival_location.longitude)
        
        distance = geodesic(departure_coords, arrival_coords).miles
        distance = int(distance)
        

        if distance < 50:
            print(f"We are sorry but travel distance ({distance}) needs to be at least 50 miles")
        
        else: 
            if distance > 3000:
                additonal_fare = 200
                total_fare = additonal_fare + base_fare
                print(f"Traveling {distance} miles will cost {total_fare}")
            
            elif distance > 2000:
                additonal_fare = 175
                total_fare = additonal_fare + base_fare
                print(f"Traveling {distance} miles will cost {total_fare}")
        
            elif distance > 1000:
                additonal_fare = 150
                total_fare = additonal_fare + base_fare
                print(f"Traveling {distance} miles will cost {total_fare}")
        
            elif distance > 500:
                additonal_fare = 125
                total_fare = additonal_fare + base_fare
                print(f"Traveling {distance} miles will cost {total_fare}")
        
            elif distance > 400:
                additonal_fare = 100
                total_fare = additonal_fare + base_fare
                print(f"Traveling {distance} miles will cost {total_fare}")
        
            elif distance > 300:
                additonal_fare = 75
                total_fare = additonal_fare + base_fare
                print(f"Traveling {distance} miles will cost {total_fare}")
            
            elif distance >= 100:
                additonal_fare = 50
                total_fare = additonal_fare + base_fare
                print(f"Traveling {distance} miles will cost {total_fare}")

            elif distance >= 51:
                additonal_fare = 25
                total_fare = additonal_fare + base_fare
                print(f"Traveling {distance} miles will cost {total_fare}")
    
    else:
        print("Error: one or both cities can't be found")

# travel_destinations()