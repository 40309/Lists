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

def bubble_sort(search_list):
    for person in range(len(search_list)-1,0,-1):
        for i in range(person):
            if search_list[i]>search_list[i+1]:
                temp = search_list[i]
                search_list[i] = search_list[i+1]
                search_list[i+1] = temp
    print(search_list)
    return search_list
    
search_list = ["XU","Danish","Tony","Hamza","Zara","Harry R","Harry V","Touseef","Tavonga","Paul"]
#search_list,search_item = user_input()
sorted_list = bubble_sort(search_list)
