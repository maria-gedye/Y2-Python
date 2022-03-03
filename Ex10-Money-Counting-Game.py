# Create a change-counting game that gets the user to enter the number of coins required to make exactly one dollar
# penny = 1 cent
# nickel = 5 cents
# dime = 10 cents
# quarter = 25 cents

print("Money Counting Game")
print("Enter the right amounts to make a quick buck! $$$\n")
i_pennies = input("Pennies: ")
i_nickls = input("Nickels: ")
i_dimes = input("Dimes: ")
i_quartrs = input("Quarters: ")

s_pennies = i_pennies * 0.01
s_nickls = i_nickls * 0.05
s_dimes = i_dimes * 0.10
s_qrtrs = i_quartrs * 0.25

total_money = s_qrtrs + s_dimes + s_nickls + s_pennies

if total_money == 1.0:
    print("Congratulations! You made your first buck!")
else:
    if total_money < 1.0:
        print "Your total: $", total_money, "was too low"
    else:
        print "Your total: $", total_money, "was too high"