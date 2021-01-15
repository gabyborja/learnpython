# Define cars
cars = 100
# Define space in a car as floating point number
space_in_a_car = 4.0
# Define drivers
drivers = 30
# Define passengers
passengers = 90
# Subtract drivers from cars
cars_not_driven = cars - drivers
# Cars driven is equal to the number of available drivers
cars_driven = drivers
# carpool capacity is the space in a car multiplied by the number of cars being driven
carpool_capacity = cars_driven * space_in_a_car
# passengers per car divided by the number of cars being driven
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car")

# carpool_capacity was called as car_pool_capacity
