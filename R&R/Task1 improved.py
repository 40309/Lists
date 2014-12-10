student_list = [0,1, 2, 3, 4, 5, 6, 7, 8]
test = False
for count in range(1,9):
    student_list[count] = input("Please enter a name for student {0}: ".format(count))

while test == False:
    for count in range(1,9):
        print("{0}. {1}".format(count, student_list[count]))
    edit = int(input("Please select a number from student list to edit: "))
    if edit == 0:
        test = True
    else:
        new_name = input("Please enter the name of the new student: ")
        student_list[edit] = new_name
print()
print("Thank you for using this program")
