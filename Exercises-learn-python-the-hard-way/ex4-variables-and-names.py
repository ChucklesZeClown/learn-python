# define variables and assign values.
# values can be directly assigned,
# or be the product of calculations using previosly defined variables

cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

# display a set of statements about the values, which provide meaningful information
# about the carpool, including how many passengers should be in each car
print "There are only", cars, "cars available."
print "There are only", drivers, 'drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today"
print "We need to put about", average_passengers_per_car, "in each car."