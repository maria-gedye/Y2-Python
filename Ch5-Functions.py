# Chapter 5 Exercises 1, 6, 11, 14, 16, 18
import random

# Ex1 Kilometer Converter

# def km_to_miles():
#     km = input("Enter distance in kilometers(km): ")
#     miles = km * 0.6214
#     return miles
#
#
# m = km_to_miles()
# print "Miles: ", m, "m"


# Ex6 Calories from fat and carbohydrates
# print("Calorie calculator")
# calf = 0
# calc = 0
#
#
# def cal_from_fat(cf):
#     fat = input("Enter grams of fat: ")
#     cf = fat * 9
#     return cf
#
#
# def cal_from_carb(cc):
#     carb = input("Enter grams of carbohydrate:  ")
#     cc = carb * 4
#     return cc
#
#
# calf = cal_from_fat(calf)
# calc = cal_from_carb(calc)
# print "Total calories from fat: ", calf, "\nTotal calories from carbohydrate: ", calc


# Ex11 Math Quiz
#
# def quiz(n1, n2):
#     print "\t", n1, "\n+\t", n2, "\n="
#     answer = input("What is the answer?  ")
#     if answer == (n1 + n2):
#         print("Correct!")
#     else:
#         print "incorrect. Answer is: ", n1 + n2
#
#
# num1 = random.randint(1, 999)
# num2 = random.randint(1, 999)
# quiz(num1, num2)


# Exercise 14 Kinetic Energy
mass = input("Mass (kg):  ")
velocity = input("Velocity (m per sec):  ")


def kinetic_energy(m, v):
    ke = (0.5 * m) * (v * v)
    return ke


print "Kinetic energy in Joules is  ", kinetic_energy(mass, velocity), "J"
