#file handling

# This program opens an existing file in write mode, adds new text and reads it:
# file1 = open('file-handling.txt', 'w')
# file1.write('hello world\n')
# file1.write('how are you today?\n')
# file1.close()
#
# file1 = open('file-handling.txt', 'r')
# print(file1.read())


# This program asks user to enter number of students and names and then write/read to a file
import string

count = input("How many students?  ")
s_file = open('students.txt', 'w')


for i in range(count):
    print(i + 1)
    name = raw_input("Enter name: ")
    s_file.write(name + "\n")

s_file.close()  # close after finished writing

s_file = open('students.txt', 'r')
print(s_file.read())



