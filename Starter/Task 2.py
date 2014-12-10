shopping_list = []
finished = False
while not finished:
    shopping_item = input("Enter next item (-1 to end list): ")
    if shopping_item == "-1":
        finished = True
    else:
        shopping_list.append(shopping_item) #add new item to the list

length = 1 + (len(shopping_list))

for index in range(length):
    print("item {0} is {1}".format(index,shopping_list[index]))
