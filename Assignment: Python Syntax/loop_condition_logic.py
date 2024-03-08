#5. Loop Condition Logic
    #Task 1: Loop Condition Exploration
number = 0
# Because the loop condition is set to always be true the loop will never end
# Thanks to the break statment once the number variable reaches 6 the loop will instantly stop
while True:
    number += 1
    if number == 6:
        break
    print(number)

    #Task 2: Conditional Exit
# The loop will first check the value of the number variable 
# as long as the number variable is lesss than 5 the loop will increas the number variable by 1
# Once the number variable reaches 5 the loop will end 
while number < 5:
    number += 1
    print(number)

    #Task 3: Loop with Multiple Conditions
#Combining conditions allows us to be more spesific about when a loop is executated making it more complex than a loop with a singular condition
list = [1,2,3,4,5,]
end = 0
while 1 and 2 in list:
    end += 1
    print(end)
    if end == 5:
        break