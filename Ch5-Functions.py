# Chapter 5 Exercises 1, 6, 11, 14, 16, 18

# Ex1 Kilometer Converter

def km_to_miles():
    km = input("Enter distance in kilometers(km): ")
    miles = km * 0.6214
    return miles


m = km_to_miles()
print "Miles: ", m, "m"
