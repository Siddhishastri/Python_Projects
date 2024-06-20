#This class will represent a car in the rental system

from datetime import datetime

class Car:
    def __init__(self, car_id, model, rate_per_hour):
        self.car_id = car_id
        self.model = model
        self.rate_per_hour = rate_per_hour
        self.is_available = True

    def __str__(self):
        return f"Car ID: {self.car_id}, Model: {self.model}, Rate per Hour: {self.rate_per_hour}, Available: {self.is_available}"


#This class will manage the car rental process, including recording rental times and calculating bills

class CarRental:
    def __init__(self):
        self.cars = []
        self.rented_cars = {}

    def add_car(self, car):
        self.cars.append(car)

    def rent_car(self, car_id):
        for car in self.cars:
            if car.car_id == car_id and car.is_available:
                car.is_available = False
                rental_start_time = datetime.now()
                self.rented_cars[car_id] = rental_start_time
                print(f"Car {car_id} rented at {rental_start_time}")
                return
        print(f"Car {car_id} is not available.")

    def return_car(self, car_id):
        if car_id in self.rented_cars:
            rental_end_time = datetime.now()
            rental_start_time = self.rented_cars.pop(car_id)
            rental_duration = rental_end_time - rental_start_time
            rental_hours = rental_duration.total_seconds() / 3600
            for car in self.cars:
                if car.car_id == car_id:
                    bill_amount = rental_hours * car.rate_per_hour
                    car.is_available = True
                    print(f"Car {car_id} returned at {rental_end_time}")
                    print(f"Rental duration: {rental_hours:.2f} hours")
                    print(f"Total bill: ${bill_amount:.2f}")
                    return
        print(f"Car {car_id} was not rented.")

    def available_cars(self):
        for car in self.cars:
            if car.is_available:
                print(car)
