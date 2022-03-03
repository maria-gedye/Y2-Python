# Write a program that asks the user to enter an object's mass, then calculates its weight.
print("Mass and Weight")
mass = input("Enter the object's mass(kg):  ")
weight = mass * 9.8

if weight > 500:
    print("This object is too heavy to calculate")  # limit is around 51kg
elif weight < 100:
    print("This object is too light to calculate") # limit is around 11kg
else:
    print "Mass: ", mass, "kg   Weight: ", weight, "newtons"