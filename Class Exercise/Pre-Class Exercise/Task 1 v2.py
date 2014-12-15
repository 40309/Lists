#Tony K.
#15/12/14
#Task 1 V2

NameList = ['Jim', 'Bob', 'Alison', 'Jo', 'James']

user_input = input("Enter the name you are searching for: ")
ThisElement = 0
Checker = False
not_found = False

length = len(NameList)
length = length -1

while Checker != False:
    if NamesList[ThisElement] == user_input:
        Checker = True
    elif length == ThisElement:
        Checker = True
        not_found = True
    else:
        ThisElement = ThisElement + 1

if NameList[ThisElement] == user_input:
    print("{0} was in element {1} in the list".format(ElementSought, ThisElement))
elif not_found == True:
    print("The Name was not found")
else:
    print()
    
