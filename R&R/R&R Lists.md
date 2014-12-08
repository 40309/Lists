#Reading and Research - Lists

These tasks are designed to introduce you to the programming topic we will be studying in class next lesson. You **must** complete these activities prior to the lesson.

##Task 1
Create a program that will:

- Store the names of eight students and then display them on the screen as a menu.
- Select a student from the menu and edit their name.
- Redisplay the menu so that it is possible to see the changes you have made

You can see an example of the running program below. Try and use **iteration** where possible.

![](https://www.dropbox.com/s/6xiv9uolyftxxit/lists_program_q1.jpg?dl=1)

#Task 2
Having created the program in Task One, use the space below to describe its shortcomings:

*The program is very long and tedious. Also the program doesn't repeat in-case the user wants to change/edit more than one user.*

##Task 3 - Arrays
Rather than creating individual variables for each student it is possible to create a single data structure called an **array** to store all of the students names.

Research array data structure on the internet (e.g. wikipedia) and then in the space below explain how an array could be used to improve the program from Task 1.


##Task 4 - Lists
Most programming languages have the concept of an array data structure but Python does not. Instead, Python has **Lists**, which are similar to arrays but with important differences.

|Array|List|
|-----|----|
|Initial size must be declared e.g. this array has 100 items|No initial size is required|
|Once declared the size can not be changed|Size can expand or contract as required|
|Contains only data of a single type e.g. strings|Can contain different data types|

There are various concepts and operations you need to be familiar with before you can use Lists in Python. Read about Lists in Python on the Python School website:

1. [Lists in Python](http://www.pythonschool.net/basics/creating-a-list/)
2. [Lists and FOR Loops](http://www.pythonschool.net/basics/lists-with-a-for-loop/)
3. [List Operations](http://www.pythonschool.net/basics/list-operations/)

##Task 5
Using your knowledge of Python Lists, Functions and Iteration improve the program from Task 1.

**Paste** the code for your original Task 1 in the space provided below:

```python
#original code for task 1
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
```

**Paste** the code for your improved Task 1 in the space provided below:

```python
#improved code for task 1


```

##Summary
In this R&R you have investigated Lists. You have see how Lists are used to simplify your code when you need to work with lots of similar data. You have read about the differences between Lists in Python and Arrays in other programming languages.

Please make sure you have completed this R&R fully before your next programming lesson as it will form the basis of the initial classroom discussion and starter tasks.
> Written with [StackEdit](https://stackedit.io/).