'''2. The Shopping List Maker'''

#function1 : user add items to a list 
#^^^ remove items as well
#function2 : prints out the entire list (formatted)

list = []

#Task 1: Write a function that lets the user add items to a list.
def user_list():
    print("Lets make a list! Write 5 items")
    for i in range(5):
        user_input = input(f"{i+1}) ")
        list.append(user_input)

#Task 2: Include a feature to remove items from the list.
def remove_list():
    print(f"Would you like to remove anything from this list:")
#Task 3: Add a function that prints out the entire list in a formatted way.
    for i in range(len(list)):
        print(f"{i+1}) {list[i]}")
    question = input("yes/no:")
    if question == "yes":
        remove_item = input("Write which item you would like to remove: ")
        if remove_item in list :
            list.remove(remove_item)
            print("Ok the new list looks like this: ")
            for i in range(len(list)):
                print(f"{i+1}) {list[i]}")
    if question == "no":
        print("The list is done!")


user_list()
remove_list()
