class Vehicle:
    """
    Base class for vehicles.

    Attributes:
        vehicle_id (str): Unique identifier for the vehicle.
        make (str): Manufacturer of the vehicle.
        model (str): Model name of the vehicle.
        year (int): Year of manufacture.
        color (str): Vehicle color.
        fuel_efficiency (float): Fuel efficiency in km per liter.
        service_history (list): List of service records.
    """

    def __init__(self, vehicle_id, make, model, year, color, fuel_efficiency):
        self.vehicle_id = vehicle_id
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.fuel_efficiency = fuel_efficiency
        self.service_history = []

    def display_info(self):
        """Displays the vehicle's information."""
        print(f"Vehicle ID: {self.vehicle_id}")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Color: {self.color}")
        print(f"Fuel Efficiency: {self.fuel_efficiency} km/l")

    def calculate_fuel_consumed(self, distance):
        """Calculates the fuel consumed over a given distance."""
        if self.fuel_efficiency <= 0:
            raise ValueError("Fuel efficiency must be greater than zero.")
        return distance / self.fuel_efficiency

    def add_service(self, service_date, description, cost):
        """Adds a service record."""
        self.service_history.append({"date": service_date, "description": description, "cost": cost})
        print(f"Service record added for vehicle {self.vehicle_id}.")

    def display_service_history(self):
        """Displays the vehicle's service history."""
        if not self.service_history:
            print("No service history available.")
        else:
            print(f"Service History for {self.vehicle_id}:")
            for record in self.service_history:
                print(f"Date: {record['date']} | Description: {record['description']} | Cost: ${record['cost']}")


class Car(Vehicle):
    """A class representing a car."""

    def __init__(self, vehicle_id, make, model, year, color, fuel_efficiency, num_doors, air_conditioned):
        super().__init__(vehicle_id, make, model, year, color, fuel_efficiency)
        self.num_doors = num_doors
        self.air_conditioned = air_conditioned

    def display_info(self):
        """Displays the car's information."""
        super().display_info()
        print(f"Number of Doors: {self.num_doors}")
        print(f"Air Conditioned: {'Yes' if self.air_conditioned else 'No'}")


class Truck(Vehicle):
    """A class representing a truck."""

    def __init__(self, vehicle_id, make, model, year, color, fuel_efficiency, payload_capacity):
        super().__init__(vehicle_id, make, model, year, color, fuel_efficiency)
        self.payload_capacity = payload_capacity

    def display_info(self):
        """Displays the truck's information."""
        super().display_info()
        print(f"Payload Capacity: {self.payload_capacity} kg")


class VehicleManager:
    """Manages a collection of vehicles."""

    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        """Adds a vehicle to the manager."""
        self.vehicles.append(vehicle)
        print(f"Vehicle with ID {vehicle.vehicle_id} added successfully.")

    def remove_vehicle(self, vehicle_id):
        """Removes a vehicle by ID."""
        vehicle = self.get_vehicle_by_id(vehicle_id)
        if vehicle:
            self.vehicles.remove(vehicle)
            print(f"Vehicle with ID {vehicle_id} removed successfully.")
        else:
            print("Vehicle not found.")

    def get_vehicle_by_id(self, vehicle_id):
        """Finds and returns a vehicle by ID."""
        for vehicle in self.vehicles:
            if vehicle.vehicle_id == vehicle_id:
                return vehicle
        return None

    def display_all_vehicles(self):
        """Displays all vehicles."""
        if not self.vehicles:
            print("No vehicles available.")
            return
        for vehicle in self.vehicles:
            vehicle.display_info()
            print("-" * 40)

    def calculate_fuel_consumption(self, vehicle_id, distance):
        """Calculates the fuel consumption for a vehicle."""
        vehicle = self.get_vehicle_by_id(vehicle_id)
        if vehicle:
            try:
                fuel_consumed = vehicle.calculate_fuel_consumed(distance)
                print(f"Fuel consumed for {distance} km: {fuel_consumed:.2f} liters.")
            except ValueError as e:
                print(e)
        else:
            print("Vehicle not found.")

    def add_service_record(self, vehicle_id, service_date, description, cost):
        """Adds a service record to a vehicle."""
        vehicle = self.get_vehicle_by_id(vehicle_id)
        if vehicle:
            vehicle.add_service(service_date, description, cost)
        else:
            print("Vehicle not found.")

    def display_vehicle_service_history(self, vehicle_id):
        """Displays the service history of a vehicle."""
        vehicle = self.get_vehicle_by_id(vehicle_id)
        if vehicle:
            vehicle.display_service_history()
        else:
            print("Vehicle not found.")

    def sort_vehicles_by_year(self):
        """Sorts vehicles by year in descending order."""
        self.vehicles.sort(key=lambda v: v.year, reverse=True)
        print("Vehicles sorted by year.")

    def sort_vehicles_by_fuel_efficiency(self):
        """Sorts vehicles by fuel efficiency in descending order."""
        self.vehicles.sort(key=lambda v: v.fuel_efficiency, reverse=True)
        print("Vehicles sorted by fuel efficiency.")

    def total_maintenance_cost(self):
        """Calculates the total maintenance cost of all vehicles."""
        total_cost = sum(
            service['cost'] for vehicle in self.vehicles for service in vehicle.service_history
        )
        print(f"Total maintenance cost for all vehicles: ${total_cost:.2f}")

    def update_vehicle_info(self, vehicle_id, **kwargs):
        """Updates a vehicle's information."""
        vehicle = self.get_vehicle_by_id(vehicle_id)
        if vehicle:
            for key, value in kwargs.items():
                if hasattr(vehicle, key):
                    setattr(vehicle, key, value)
            print(f"Vehicle {vehicle_id} info updated successfully.")
        else:
            print("Vehicle not found.")

    def display_vehicle_info(self, vehicle_id):
        """Displays information about a specific vehicle."""
        vehicle = self.get_vehicle_by_id(vehicle_id)
        if vehicle:
            vehicle.display_info()
        else:
            print("Vehicle not found.")
