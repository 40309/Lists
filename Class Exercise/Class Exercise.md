#Class Exercises - Lists
These tasks are designed to help you practice the knowledge and skills you have developed. There are exercises to help you revise and develop your understanding and also to challenge you further.

##Syntax
Here is an example of a list:

```python
names = ["Laura", "Tom", "Ryan", "Alice", "Callum"]
```

We can access a particular item in the list as follows:

```python
next_name = names[3]
```

This would return:

```
'Alice'
```

One of the major benefits of **lists** over individual variables is they enable us to iterate over the list so we can look at each value in turn:

```python
for name in names:
    print(name)
```

or

```python
for index in range(len(names)):
    print(name[index])
```

###List of Lists
Because a list can contain values of any data type we can create a list in which each item of that list is another list. This is very useful as it allows us to model a grid structure in a program:

|index|0|1|2|3|
|-|-|-|-|-|
|**0**|1|2|3|4|
|**1**|5|6|7|8|
|**2**|9|10|11|12|
|**3**|13|14|15|16|

This would be represented as list of lists:

```python
grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
```

We can access a particular item in the list of lists as follows:

```python
next_num = grid[1][3]
```

This would return `8`.

##Task 1 - Improving a piece of code
Run the python file called `SearchName.py` (shown below) and test it with 2 names:

- a name that is in the list
- a name that is not in the list

**Fix** the program so that it:

- works efficiently in either scenario
- shows the correct information to the user

```python
names = ['Jim', 'Bob', 'Alison', 'Jo', 'James']

element_sought = input('Enter the name you are searching for : ')
this_element = 0
found = False
while not found:
       if names[this_element] == element_sought:
          Found = True
       else:
          this_element = this_element + 1

if Found:
   print('{0} was in element {1} in the list'.format(element_sought, this_element))
else:
   print('Not found')
```

##Task 2 - Class Exercises
In this section you may choose the exercises you attempt. There are three types of exercises to consider:

1. **Revision Exercises** - choose these exercises if you are not confident in your understanding of selection statements
2. **Development Exercises** - choose these exercises if you are confident in your understanding but want some more practice
3. **Stretch and Challenge Exercises** - choose these exercises if you feel you have mastered selection and want to tackle some tougher problems

Once you feel more confident attempt some of the more difficult exercises. The more practice you get now the more comfortable you will be using selection in more complex programs later in the course.

Remember, practice makes perfect!

###Attempting These Exercises
You should do the following for each exercise you attempt:

1. Create **flowcharts** first - plan your solution on paper before attempting it
2. Create a set of **test data** - select values you will enter to test the program and know beforehand what you expect the answers to be
3. Write the **program** - write the program in Python using the pseudocode to assist you and the test data to ensure the program functions correctly

###Revision Exercises
1. Write a program that populates a list with 6 names which are entered by the user. The program should then display the names in the same order that they were entered.
2. Enhance the program written in 1 above. After prompting for the names and storing them in the list the program should prompt the user for the range of number positions for the names they wish to view.

    The program will then display the names in the range. So for example if the names entered were John, Jim, Mary, Alex, Stephen, Luke and the user asks to see names 4 to 6 the program will display Alex, Stephen, Luke.

3. A list WeeklyTemperature contains the temperatures for 7 days Sunday to Saturday as real numbers.

    Populate the list as follows :

    ```python
    weekly_temperature = [20.7, 23.4, 24.5, 24, 23.8, 19.7, 20.1]
    ```

    Calculate the average weekly temperature and report it to the user.

4. We can declare two lists, `Student` and `DoB`, to store the name of Students and their dates of birth.

    For example, if Fred is born on 22/12/84 then we could store `Fred` in `Student[0]` and `22/12/84` in `DoB[0]`.

    Write a program that stores 5 students’ names and dates of birth and then searches for a particular student selected by the user and displays that student’s date of birth and current age.

    Display a suitable message if the student’s details cannot be found.

###Development Exercises
Attempt these tasks if you are confident in your understanding but feel you need more practice

1. Write a program that stores the names of ten countries in column1 and their capitals in column2. The program should then pick a random country and ask the user for the capital.

    Display an appropriate message to the user to show whether they are right or wrong.

2. Expand the above to ask the user 5 questions and give a score of how many they got right out of 5.
3. Write a program to select 6 different random numbers between 1 and 19. Output the numbers selected. You can use your own algorithm with lists or try using the following algorithm:

    - Initialise a list by using a for loop to store the values 1 to 19
    - Repeatedly select a random element from the list until a non-zero value is selected
    - Display this value
    - Set that element to zero
    - Repeat the above 3 steps until six numbers have been selected

    Example 1 : if the list contains `[1,2,3,4,5,6,7,8,0,10,11,12,13,14,15,0,17,18,19]` and you generate a 5 set the 4th slot (remember indexing of lists starts at zero) to 0

    i.e. `[1,2,3,4,0,6,7,8,0,10,11,12,13,14,15,0,17,18,19]`

    Example 2 : if the list contains `[1,2,3,4,5,6,7,8,0,10,11,12,13,14,15,0,17,18,19]` and you generate a 9 do not update the list as the number 9 has already been used. In this scenario you would need to generate another number.

###Stretch and challenge exercises
Attempt these tasks if you feel you have mastered selection and want to tackle tougher problems.

1. Write a program which allows users to maintain a list. It works as follows:

    - starts off with a hard coded list with 5 items on it.
    - Continuously shows the user the following menu until the user requests to exit the program by pressing 9.

        ![](https://www.dropbox.com/s/3eu64e3uz679lsa/list_menu.jpg?dl=1)

    - captures the choice selected by the user and actions it. Note that if they enter an invalid option you should inform them of this and re-prompt.
    - Actions the option selected. Note that you will need to use the following functions to achieve this (see python documentation):

    ```python
    my_list.insert()
    my_list.remove()
    del my_list[]
    my_list.append()
    my_list[] = "new value"
    ```

    - After making a change to the list the list should be redisplayed in sequence with the sequence number showing on the left hand side of the items. (see example of program running below)

    **Try to structure your program by using functions.**

    ![](https://www.dropbox.com/s/szp34oijzqxf5aj/list_menu2.jpg?dl=1)

2. Store in a list a set of 5 place names, and in a list of lists the distances between the places. Ensure that the order of the places is the same in both lists. When the names of 2 places are input, the distance between them is displayed. If they are not both in the table, a suitable message should be displayed.
3. Write a program which asks the user for the subjects done in each period for each day and then prints out the timetable with suitable headings.
4. A Latin Square of order n is an n x n grid which contains the numbers 1,2,3,...,n such that each row and column contains each number exactly once. For example the following diagram shows a Latin Square of order 4. You can see that each row can be obtained from the previous one by shifting the elements one place to the left.

    |1|2|3|4|
    |-|-|-|-|
    |2|3|4|1|
    |3|4|1|2|
    |4|1|2|3|

    Design an write a program to store such a Latin Square of a size given by the user. The program should also display the Latin Square.


> Written with [StackEdit](https://stackedit.io/).