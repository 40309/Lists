#Tony K.
#15/12/14
#Task 1

# Program to search for a name in a list

NamesList = ["Jim', 'Bob', 'Alison', 'Jo', 'James"]

ElementSought = input('Enter the name you are searching for : ')
ThisElement = 0
Found = False
while =! Found:
       if NamesList[ThisElement] == ElementSought:
          Found = True
       else:
          ThisElement = ThisElement + 1

if Found:
   print('{0} was in element {1} in the list'.format(ElementSought, ThisElement))
else:
   print('Not found')
