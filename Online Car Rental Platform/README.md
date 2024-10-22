# Online Car Rental Platform

## Project Overview

This project involves building an **online car rental platform using Object-Oriented Programming (OOP) principles in Python.** The platform allows customers to rent cars on an hourly, daily, or weekly basis, with auto-generated bills when the cars are returned. It handles inventory management and rental processes while providing a clean, user-friendly interface for both the company and its customers.

## Problem Statement

A car rental company needs an online platform where:

+ Customers can rent cars hourly, daily, or weekly.
* The company can track available inventory and fulfill customer requests based on available stock.
+ Customers receive an auto-generated bill after returning rented cars.

## Instructions and Steps to Perform

1. Car Rental Module (car_rental.py)

This module defines the core functionalities of the car rental system using a class-based design.

Step 1: Create the Car Rental Class
+ Use the CarRental class to manage the car rental system, including inventory, rental methods, and billing.
+ Define the constructor to initialize the number of available cars.

Step 2: Display Available Cars
+ Define a method display_stock to display how many cars are currently available for rent.

Step 3: Hourly, Daily, and Weekly Rentals
+ Implement methods to rent cars on an hourly, daily, or weekly basis.
+ Ensure the requested number of cars is valid and update the stock accordingly.
+ Store the rental start time to calculate billing later.

Step 4: Return Cars and Generate Bill
+ Define the return_car method to handle returning cars.
+ Calculate the rental duration based on the rental type and time.
+ Generate the final bill based on the rental duration and number of cars rented.
![car_rental_py](https://github.com/user-attachments/assets/ae670f1f-4805-4af6-8c09-716b70131920)

2. Main Project File (main.ipynb)

The main project file imports both the CarRental and Customer classes and manages the interaction between the customer and the rental platform.

Step 1: Import Modules

+ Import the CarRental and Customer classes from the respective modules.

Step 2: Define the Main Method
+ Create the main method to handle the flow of customer actions:
1. Display available cars.
2. Rent cars (hourly, daily, or weekly).
3. Return cars and generate the final bill.

Step 3: Run the Main Method
+ Run the main method to start the car rental system.
![car_rental_main](https://github.com/user-attachments/assets/a80c89eb-9ff0-4f1c-87c2-a7335c31f92d)
