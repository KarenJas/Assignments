#2. Double Scoop with Nested Loops
    #Task 1: Code Correction
import random

for i in range(3):
    for j in range(3):
        print("*", end="")
    print("\n",end="")
   
   #Task 2: Your Mood Tracker
mood = ["happy","sad","energetic","calm","nervouse","tired","excited"]
time_of_day = ["morning","afternoon","evening"]
day =["monday","tuesday","wednessday","thursday","friday","saturday","sunday"]
mood_tracker = []
for i in range(len(day)):
    current_day = day[i]
    print(f"{current_day}:")
    for j in range(len(time_of_day)):
        current_time = time_of_day[j]
        print(f"{current_time}- {random.choice(mood)}")
        
    #Task 3: Multiplication Table
for i in range(1,6):
    for j in range(1,6):
        product = i * j
        print(f"{i} x {j} = {product}  ",end="")
    print("\n",end="")
