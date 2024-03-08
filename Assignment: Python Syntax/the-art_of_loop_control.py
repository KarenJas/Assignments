'''6. The Art of Loop Control'''
    #Task 1: Using else with while
fruits = ["apple", "banana", "orange", "grape", "watermelon", "kiwi", "strawberry", "mango", "pineapple", "pear"]
# The loop will first check to see if the condition is true 
# If the condition is false the else clause will run
while "apple" in fruits:
    if "apple" in fruits:
        print("Found appple")
        break
else:
    print("Apple not found in list")

    #Task 2: Loop Interruption with break
time_of_day = 12
# The code will output the time of day in order but once it reaches 3 pm the if stamement condition will be true and break the loop 
while True:
    if time_of_day == 12 :
        print(str(time_of_day),"am")
        time_of_day = 0
        while True:
            if time_of_day < 11:
                time_of_day += 1
                print(str(time_of_day),"am")
                if time_of_day == 11:
                    time_of_day = 12
                    while True:
                        if time_of_day == 12 :
                            print(str(time_of_day),"pm")
                            time_of_day = 0
                            while True:
                                if time_of_day < 11:
                                    time_of_day += 1
                                    if time_of_day == 3:
                                     break
                                    print(str(time_of_day),"pm")
    

    #Task 3: Skipping Iterations with continue
#the continue statment allows the code to skip over multiples of 3 
task3_numbers = list(range(1,31))
index = 0
new_task3_numbers = []
while index < 30: 
    if task3_numbers[index] % 3 == 0 :
        index += 1
        continue
    new_task3_numbers.append(task3_numbers[index])
    index +=1
print(new_task3_numbers)

    #Task 4: The Placeholder pass
#the loop uses pass to allow the code to run and add code later on 
# Pass might be useful when you need to run the code but dont have it finished yet
number_check = [list(range(1,10))]
while True:
    if 5 in number_check:
        pass