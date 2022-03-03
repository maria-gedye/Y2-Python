# exercise 7

print('Colour Mixer')

colour1 = raw_input('Enter primary colour 1: ')
colour2 = raw_input("Enter primary colour 2: ")

allColours = colour1 + " " + colour2
# red = orange/purple
# blue = purple/green
# yellow = green/orange

if "red" in allColours and "yellow" in allColours:
    print("secondary colour is orange")
elif "red" in allColours and "blue" in allColours:
    print("secondary colour is purple")
elif "blue" in allColours and "yellow" in allColours:
    print("secondary colour is green")
else:
    if colour1 == colour2:
        print("both colours are the same")
    else:
        print("one or more colours are not a primary colour")

