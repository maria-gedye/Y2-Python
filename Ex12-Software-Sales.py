# write a program that asks the user to enter the number of packages purchased. The program should then display
# the amount of discount (if any) and the total amount after the discount
# Quantity      Discount
# 10-19         10%
# 20-49         20%
# 50-99         30%
# 100 or more   40%
print("$oftware $ales \n")

pckg = 99.0
discnt = 0.0
numOfPackages = input("Please enter number of packages purchased: ")
total = pckg*numOfPackages

if numOfPackages >= 100:
    d4 = 0.4
    discnt = total * d4
elif 99 >= numOfPackages >= 50 :
    d3 = 0.3
    discnt = total*d3
elif 20 <= numOfPackages <= 49:
    d2 = 0.2
    discnt = total*d2
elif 10 <= numOfPackages <= 19:
    d1 = 0.1
    discnt = total*d1
else:
    pass

print "Your discount:  $", discnt
print "Total amount: $", total - discnt