# Algorithm Workbench on Page 357

#1 write name to file
f1 = open('my_name.txt', 'w')
f1.write("Maria")
f1.close()

#2 read file
f1 = open('my_name.txt', 'r')
print(f1.read())
f1.close()

#3 write using loop
f2 = open('list.txt', 'w')
for i in range(100):
    myindex = str(i+1)
    f2.write(myindex + "\n")

f2.close()

#4 read using loop
# f2 = open('list.txt', 'r')
# print(f2.read())
# f2.close()

#****  5 add all previous numbers and display total
f2 = open('list.txt', 'r')
for i in range(100):
    sumthis = int(f2.readline())
    total += sumthis


f2.close()