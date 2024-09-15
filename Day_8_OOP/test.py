#  Multiple Inheritance
# Problem: Vehicle, ElectricVehicle, and SolarVehicle
# Create a class Vehicle with:
# Attributes: brand
# Method:
# get_brand() - prints the brand of the vehicle.
# Create a class ElectricVehicle with:

# Attribute: battery_capacity
# Method:
# get_battery_info() - prints the battery capacity of the vehicle.
# Create a class SolarVehicle that inherits from both Vehicle and ElectricVehicle and adds:
# Attribute: solar_panel_area

# Method:
# get_solar_panel_info() - prints the solar panel area of the vehicle.
# Objective:
# Implement the classes using multiple inheritance.
# Create an object of class SolarVehicle and call all the methods from Vehicle, ElectricVehicle, and SolarVehicle.
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def get_brand(self):
        print(f"Vehicle Brand {self.brand}")    

class ElectricVehicle:
    def __init__(self, battery_capacity):
        self.battery_capacity = battery_capacity

    def get_battery_info(self):
        print(f"Battery capacity {self.battery_capacity}")  

class SolarVehicle(Vehicle , ElectricVehicle):
    def __init__(self, brand , battery_capacity,solor_pannel_area   ):
        Vehicle.__init__(self, brand)
        ElectricVehicle.__init__(self, battery_capacity)
        self.solor_pannel_area = solor_pannel_area
    def get_solar_panel_info(self):
        print(f"Solar pannel area {self.solor_pannel_area}")  


solar = SolarVehicle("Toyota", "1300 kwh", "12sqm") 
solar.get_brand() 
solar.get_battery_info()
solar.get_solar_panel_info()   
        

 





        
        

       












  


            




        

