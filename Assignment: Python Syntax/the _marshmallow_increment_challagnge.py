'''4. The Marshmallow Increment Challenge'''
    #Task 1: Increment at the Start
#I predict that it will output the print statement 5 times
marshmallows = 0
while marshmallows < 5:
    marshmallows += 1
    print("Added a marshmallow! Now there are " + str(marshmallows) + " marshmallows.")
#First the program will check to see if the value of marshmallows is less than 0
#If it is true the program will then add 1 to the value of marshmallows and then print the statment
#Once the value of marshmallows reaches the number 6 the loop will no longer be true and will stop

    #Task 2: Increment at the End
#I predict that the output will remain the same as the previous code
marshmallows = 0
while marshmallows < 5:
    print("Added a marshmallow! Now there are " + str(marshmallows) + " marshmallows.")
    marshmallows += 1
#In this output the print statment number starts at 0 and ends at 4 istead or starting at 1 and ending on 5
#This is caused becasue the print stament uses the marshmallow variable before it is updated to the correct number making it be one off
    
    #Task 3: Off-by-One Error Investigation
marshmallows = 0
#code with one off error 
while marshmallows < 11:
    marshmallows +=1
    print("Added a marshmallow! Now there are " + str(marshmallows) + " marshmallows.")
#fixed code
#increasing the marshmallow count after the print statment allows it to be delayed by one as to not exceed the 10 marshmallow limit regardless of the loop condition
#another way to correct the code would be to set the loop condition to less than 10 and flip the order of the loop
#it is import to prioritize the order in which you increment because it can cause a one off error
while marshmallows < 11:
    print("Added a marshmallow! Now there are " + str(marshmallows) + " marshmallows.")
    marshmallows +=1
