# A program that asks the user for their name, age, and location and then prints out a personalized message.

name = input("What is your name_:?")
age = int(input("What is your age:?"))
location = input("What is your location_:?")

print("Your name is {} , your age is {} and you live in {} city.".format({name},{age},{location}))