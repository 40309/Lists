student_1 = input("Please enter the name of the first student: ")
student_2 = input("Please enter the name of the second student: ")
student_3 = input("Please enter the name of the third student: ")
student_4 = input("Please enter the name of the fourth student: ")
student_5 = input("Please enter the name of the fifth student: ")
student_6 = input("Please enter the name of the six student: ")
student_7 = input("Please enter the name of the seventh student: ")
student_8 = input("Please enter the name of the eight student: ")
print()
test = False

print("1. {0}".format(student_1))
print("2. {0}".format(student_2))
print("3. {0}".format(student_3))
print("4. {0}".format(student_4))
print("5. {0}".format(student_5))
print("6. {0}".format(student_6))
print("7. {0}".format(student_7))
print("8. {0}".format(student_8))
print("0. Exit Programm")

print()

while test == False:
    edit = int(input("Please select a student to edit: "))
    if edit == 1:
        student_1 = input("Please select a student to edit: ")
        test = True
    elif edit == 2:
        student_2 = input("Please select a student to edit: ")
        test = True
    elif edit == 3:
        student_3 = input("Please select a student to edit: ")
        test = True
    elif edit == 4:
        student_4 = input("Please select a student to edit: ")
        test = True
    elif edit == 5:
        student_5 = input("Please select a student to edit: ")
        test = True
    elif edit == 6:
        student_6 = input("Please select a student to edit: ")
        test = True
    elif edit == 7:
        student_7 = input("Please select a student to edit: ")
        test = True
    elif edit == 8:
        student_8 = input("Please select a student to edit: ")
        test = True
    else:
        print("You have entered an invalid number, please try again")
