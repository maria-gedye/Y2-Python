# Write a program that calculates the number of packages of hot dogs and buns needed for a cookout with the minimum
# amount of leftovers.
print("\n** Hot Dog Cookout Calculator **")
people = input("How many people attending?  ")
hotDogsPP = input("How many hot dogs per person?  ")
totalDogs = people * hotDogsPP
# print(totalDogs)

# hot dogs come in packs of 10, buns come in packs of 8
hotDogsSubtotal = totalDogs / 10
hotDogsRemainder = totalDogs % 10   # find remainder(if any) of hot dogs once packages have been calculated
if 0 < hotDogsRemainder < 9:    # so if remainder ranges between 1-9, add another package to the final total
    hTotal = hotDogsSubtotal + 1

bunsSubtotal = totalDogs / 8
bunsRemainder = totalDogs % 8
if 0 < bunsRemainder < 8:       # repeat same method as above for the bun packages, this time check for range between 1-8
    bTotal = bunsSubtotal + 1

print "\nCookout order for:", totalDogs, "hotdogs /", people, "people"
print "*Item* hot dogs 10pk: ", hTotal
print "\tovershipped hot dogs: ", (hTotal * 10) - totalDogs     # subtract initial total from the final total to find number of left over hot dogs
print "\n*Item* long buns 8pk: ", bTotal
print "\tovershipped long buns: ", (bTotal * 8) - totalDogs
