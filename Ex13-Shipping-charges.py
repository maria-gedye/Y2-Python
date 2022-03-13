# write a program that takes in package weight and displays shipping charges
# package weight(lb)    rate per lb
# 2 or less             $1.50
# over 2 / under 6      $3.00
# over 6 / under 10     $4.00
# over 10               $4.75

print("Shipping Calculator")
weight = input("Enter package weight in pounds(lb):  ")
rates = [1.50, 3.00, 4.00, 4.75]
shipping = 0

if weight <= 2:
    shipping = weight * rates[0]
elif 2 < weight < 6:
    shipping = weight * rates[1]
elif 6 < weight < 10:
    shipping = weight * rates[2]
else:
    shipping = weight * rates[3]

print "Total shipping charges:  $", shipping, "\nPackage weight: ", weight, "lb"


