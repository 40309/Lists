#Starter - Functions
These tasks are designed to refresh the reading and research you have undertaken at home prior to this lesson. If you have not completed the R&R assignment then please speak to your teacher before attempting these exercises.

##Task 1 - Dry Run
The following algorithm uses an array Values containing four numbers.

|Index|Value|
|-----|-----|
|1|24|
|2|13|
|3|57|
|4|45|

```
Result ←  0
Index ←  0
Repeat
    Index ←  Index + 1
    If Result < Values[Index]
        Then Result ←  Values[Index]
    EndIf
Until Index = 4
```

1. Dry run this algorithm by using the trace table below.

    |Result|Index|
    |------|-----|
    |0|0|
    |24|1|
    |24|2|
    |57|3|
    |57|4|
    |||

2. What is the purpose of this algorithm?

*Finding the greatest value in a set(list) of integers *

##Task 2
Check and comment on the Python code snippet given below **without** running the code in IDLE.

```python
shopping_list = []
finished = False
while not finished:
    shopping_item = input("Enter next item (-1 to end list): ")
    if shopping_item == "-1":
        finished = True
    else:
        shopping_list.append(shopping_item) #add new item to the list

for index in range(len(shopping_list)):
    print("item {0} is {1}".format(index,shopping_list[index]))
```

1. Replace the 2 slots above containing ‘XXXX’ with the correct python code.
*.append* , *shopping_list[index]*
2. What messages will the user see as the program runs if they enter as input :

    Peas
    Carrots
    Ham
    -1
 *Enter next item (-1 to end list):* **Peas**
 *Enter next item (-1 to end list):* **Carrots**
 *Enter next item (-1 to end list):* **Ham**
 *Enter next item (-1 to end list):* **-1**
 *item 0 is Peas*
*item 1 is Carrots*
*item 2 is Ham*

3. Suggest improvements to the program:
*The program could be improved:*
-Be more user friendly
-start from 1 instead of 0
4. Now key in this python program with your improvements incorporated and test it .
```python

```
##Task 3
Convert the pseudo-code in task 1 to python code and run and test it. Do this as follows:

1. Set the list values to those shown in the question and output the value of ‘result’ at the end of the program run.
2. Write down your expected result for the program run and then test it


> Written with [StackEdit](https://stackedit.io/).