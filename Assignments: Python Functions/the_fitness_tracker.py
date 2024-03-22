'''5. The Fitness Tracker'''

#activities:'Dancing', 'Swimming', 'Biking'
#duration: 10, 20, 15
activities = [ ]
duration_time = [ ]
calories_lost = [ ]

#Task 1: Develop a function to log different fitness activities and their duration.
def fitness_activity(activity,duration):
    activities.append(activity)
    duration_time.append(duration)

#Task 2: Write a simple function that estimates calories burned based on the activity and duration
def calories_burned(duration):
    total_calories_burned = duration*3.5
    calories_lost.append(total_calories_burned)
    return print(f"{total_calories_burned} total calories lost")

#Task 3: Create a summary function that provides a report of all activities and total calories burned for the day.
def summary(activity_list,calories_function):
    print("List of Activities: ")
    for i in range(len(activities)):
        print(f"{i}) {activities[i]}")
    print("Calories Burned: ")
    for i in range(len(calories_lost)):
        print(f"{i}) {calories_lost[i]}")

#test 
#fitness_activity(input("activity:"),input("duration: "))
#print(activities)
#print(duration_time)
#print(calories_burned(float(input("Duration:"))))