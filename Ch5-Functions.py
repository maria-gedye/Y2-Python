# Chapter 5 Exercises 1, 6, 11, 14, 16, 18

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
print("Calorie calculator")
calf = 0
calc = 0


def cal_from_fat(cf):
    fat = input("Enter grams of fat: ")
    cf = fat * 9
    return cf


def cal_from_carb(cc):
    carb = input("Enter grams of carbohydrate:  ")
    cc = carb * 4
    return cc


calf = cal_from_fat(calf)
calc = cal_from_carb(calc)
print "Total calories from fat: ", calf, "\nTotal calories from carbohydrate: ", calc
