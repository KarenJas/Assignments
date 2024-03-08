#3. Mastering Python's For Loop
    #Task 1: Code Correction
import random

for i in range(1, 11):
    if i == 5:
        continue
    print(i)

    #Task 2: Your Mood Swings
am_list = list(range(1,12))
am_list.insert (0,12)
pm_list = list(range(1,12))
pm_list.insert (0,12)
lunch_time = 1
am_time_mood = []
pm_time_mood = []
moods = ["Happy", "Sad", "Excited", "Relaxed", "Angry", "Surprised", "Content", "Stressed", "Confused", "Playful", "Grateful", "Inspired"]

for i in range(len(am_list)):
        am_time_mood_dic = { "TIME" : f"{am_list[i]} a.m.","MOOD": random.choice(moods) }
        am_time_mood.append(am_time_mood_dic)
print(am_time_mood)

for i in range(len(pm_list)):
        if pm_list[i] == lunch_time:
                continue
        pm_time_mood_dic = { "TIME" : f"{am_list[i]} p.m.","MOOD": random.choice(moods) }
        pm_time_mood.append(pm_time_mood_dic)
print(pm_time_mood)

    #Task 3: The Persistent Loop
number_list = list(range(1,11))
chosen_number = 1
for num in range(len(number_list)):
    if num == chosen_number:
        print("found number")
        break     
else:
    print("number not found")