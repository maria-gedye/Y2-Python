# Exercises 1, 2, 6 pages 161-162

# Ex1 Days of the week
# userNum = input("Choose a number between 1-7 to see the matching day of the week: ")
# daysList = ["null", "monday", "taco tuesday", "Wednesday", "thirsty thursday", "TGIF!", "saturday", "Sunday"]
#
# if userNum > len(daysList):
#     print("Error! Choose a number from 1 to 7")
# else:
#     print "You've chosen: ", daysList[userNum]



# Ex2 Areas of Rectangle
# length1 = input("Enter length of rectangle 1: ")
# width1 = input("Enter width of rectangle 1:")
# length2 = input("Enter length of rectangle 2: ")
# width2 = input("Enter width of rectangle 2: ")
#
# area1 = length1 * width1
# area2 = length2 * width2
#
# if area1 > area2:
#     print "Rectangle 1 is larger than rectangle 2. Area is: ", area1
# elif area2 > area1:
#     print "Rectangle 2 is larger than rectangle 1. Area is: ", area2
# else:
#     print "Both rectangles are the same size. Area of rectangle 1:", area1, "Area of rectangle 2: ", area2



# Ex6 Magic Dates
print("Magic Dates")
month = input("Please enter a month (1-12): ")
day = input("Please enter day number: ")
year = input("Please enter the last two digits of the year: ")

magic = month * day

if year == magic:
    print("This date is magic!")
    print "month:", month, "multiplied by day:", day, "=", magic
    print day, "/", month, "/", year
else:
    print("Boo, this date is not magic")
    print "month:", month, "multiplied by day:", day, "=", magic
    print day, "/", month, "/", year
