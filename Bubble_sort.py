#Tony K.
#12/01/2015
#List, lesson

def user_input():
    search_list = []
    rogue = 0
    print("Once finished entering the name of students enter -1")
    while rogue == 0:
        student = input("Please enter the first name of the student: ")
        if student == "-1":
            rogue = -1
        else:
            student = student.lower()
            student = student.capitalize()
            search_list.append(student)
    search_item = input("Please enter the name of the student you are looking for: ")
    search_item = search_item.lower()
    search_item = search_item.capitalize()
    return search_list,search_item

    
    

def linear_search(search_list,search_item):
    found = False
    index = 0
    while not found and index < len(search_list):
        if search_item == search_list[index]:
            found = True
        else:
            index = index + 1
    return found

def display(found):
    if found == True:
        print("The person you searched for is in the list.")
    else:
        print("The person you searched for doesn't exist in the list.")

def bubble_sort(search_list):
    index = 0
    index_2 = 1
    length = len(search_list)
    length = length - 1
    for count in range(10):
        while len(search_list) > index_2:
            if search_list[index] > search_list[index_2]:
                temp = search_list[index]
                search_list[index] = search_list[index_2]
                search_list[index_2] = temp
                index = index + 1
                index_2 = index_2 + 1
            else:
                index = index + 1
                index_2 = index_2 + 1
    print(search_list)
    sorted_list = search_list
    return sorted_list
            
            
                


    
#search_list = ["Danish","Tony","Hamza","Jack","Harry R","Harry V"]
#search_item = input("Please enter the student name: ")
search_list,search_item = user_input()
found = linear_search(search_list,search_item)
display(found)
sorted_list = bubble_sort(search_list)
