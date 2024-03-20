'''1. The Calculator App'''

#division
#handdle division by zero errors and other errors

operation_choice = input("Pick an peration (addition, subtraction, multiplication, division): ")
number_one = float(input("First number: "))
number_two = float(input("Second number: "))
#addition: will return the sum of both numbers
def addition_function (num_one,num_two): 
    sum = num_one + num_two
    print(sum)
    return sum

#subtraction: will return the diffrence of the two numbers    
def subtraction_function (num_one ,num_two): 
    diffrence = num_one - num_two
    print(diffrence)
    return diffrence

#multiplication: will return the product of both numbers
def multiplication_function (num_one ,num_two ): 
    product = num_one * num_two
    print(product)
    return product

#division: will return the quotient of the two numbers
def division_function (num_one ,num_two ): 
    if num_two == 0:
        pass
    else:
        quotient = num_one / num_two
        print(quotient)
        return quotient

if operation_choice == "addition":
    addition_function(number_one,number_two)
elif operation_choice == "subtraction":
    subtraction_function(number_one,number_two)
elif operation_choice == "multiplication":
    multiplication_function(number_one,number_two)
elif operation_choice == "division":
    division_function(number_one,number_two)




