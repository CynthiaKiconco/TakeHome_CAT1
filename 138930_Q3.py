class Vehicle:
    def __init__(self, registration_number, make, model):
        self.registration_number = registration_number
        self.make = make
        self.model = model

    def display_info(self):
        return f'Registration Number: {self.registration_number}, Make: {self.make}, Model: {self.model}'

class Car(Vehicle):
    def __init__(self, registration_number, make, model, number_of_seats):
        super().__init__(registration_number, make, model)
        self.number_of_seats = number_of_seats

    def display_info(self):
        return super().display_info() + f', Number of Seats: {self.number_of_seats}'

class Truck(Vehicle):
    def __init__(self, registration_number, make, model, cargo_capacity):
        super().__init__(registration_number, make, model)
        self.cargo_capacity = cargo_capacity

    def display_info(self):
        return super().display_info() + f', Cargo Capacity: {self.cargo_capacity}kg'

class Motorcycle(Vehicle):
    def __init__(self, registration_number, make, model, engine_capacity):
        super().__init__(registration_number, make, model)
        self.engine_capacity = engine_capacity

    def display_info(self):
        return super().display_info() + f', Engine Capacity: {self.engine_capacity}cc'

class Fleet:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
        print(f'Vehicle with registration number {vehicle.registration_number} added.\n')

    def display_vehicles(self):
        if self.vehicles:
            print("List of Vehicles in the Fleet:")
            for vehicle in self.vehicles:
                print(vehicle.display_info())
        else:
            print("No vehicles found in the fleet.\n")

    def search_vehicle(self, registration_number):
        for vehicle in self.vehicles:
            if vehicle.registration_number == registration_number:
                print(f'Vehicle found: {vehicle.display_info()}\n')
                return vehicle
        print(f'No vehicle found with registration number {registration_number}.\n')
        return None

# Example usage:
if __name__ == "__main__":
    fleet = Fleet()

    # Adding vehicles
    car = Car("UBA705", "Toyota", "Corolla", 5)
    truck = Truck("KDA456", "Ford", "F-150", 1000)
    motorcycle = Motorcycle("TDA789", "Honda", "CBR600RR", 600)

    fleet.add_vehicle(car)
    fleet.add_vehicle(truck)
    fleet.add_vehicle(motorcycle)

    # Display all vehicles
    fleet.display_vehicles()

    # Search for a vehicle by registration number
    fleet.search_vehicle("Benz")
    fleet.search_vehicle("NONEXISTENT")  # Non-existent