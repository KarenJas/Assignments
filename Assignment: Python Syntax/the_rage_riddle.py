'''1. The Range Riddle'''
import random
    #Task 1: Code Correction
for i in range(5,2,-1):
    print(i)
   
    #Task 2: Your Mood Today
mood = ["happy","sad","energetic","calm","nervouse","tired","excited"]
day =["monday","tuesday","wednessday","thursday","friday","saturday","sunday"]

for i in range(len(day)):
    todays_mood = random.choice(mood)
    print(f"{day[i]}: {todays_mood}")
    
    #Task 3: Going Backwards
for i in range(10,0,-1):
    print(i)
