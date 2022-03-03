# Write a program that prompts the user to enter a number within the range of 1 through 10
# The program should display the Roman numeral version of that number
print("** Roman Numerals **")
userNum = input("Enter a number from 1 to 10:  ")
romanNum = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]

if userNum > 10:
    print("Error. This number is greater than 10")

userRN = userNum - 1
for i in romanNum:
    indexRN = romanNum.index(i)
    if indexRN == userRN:
        print(i)
        break
    # print(romanNum.index(i))

