'''2. User Input Data Processor'''

  #Task 1: Input Length Validator
user_name = input("Your Full Name: ")
count_of_name = sum(1 for char in user_name if char.isalpha())

if count_of_name >= 2 :
    print(f"Length of Name: {count_of_name} Characters")
else :
    print("Error Name Must Be Longer Than 2 Characters.")


    #Task 2: Password Complexity Checker
password = input("Eneter Password ")
password_count = sum(1 for char in password if char.isalpha())
uppercase_check = sum(1 for upper in password if upper.isupper())
lowercase_check = sum(1 for lower in password if lower.islower())
number_check = sum(1 for num in password if num.isdigit())

if password_count >= 8 :
    character_req = True 
else:
    character_req = False

if uppercase_check >= 1 :
    uppercase_req = True 
else: 
    uppercase_req = False

if lowercase_check >= 1 :
    lowercase_req = True 
else: 
    lowercase_req = False

if number_check >= 1 :
    number_req = True 
else: 
    number_req = False

check_list = [character_req,uppercase_req,lowercase_req,number_req]
print_list = ["8 Character requirement", "1 Uppercase letter requirement","1 Lowercase letter requirement","1 number requirement"]

def met_criteria(list_to_check,list_to_print):
    for i in range(len(list_to_check)):
        if list_to_check[i] == True :
            print(f"{list_to_print[i]} is met")           
        elif list_to_check[i] == False :
            print(f"{list_to_print[i]} not met")

met_criteria(check_list,print_list)

    #Task 3: Email Formatter
def email_check (email = input("Email: ")):
    symbol = False
    domain_name = False 
    tld = False
    if "@" in email : 
        symbol = True 
    if ".com" in email : 
        tld = True 
    if "gmail" in email: 
        domain_name = True 
    if symbol == True & tld == True & domain_name == True : 
        print ("Gmail adress is in standard format")  
    else:
        print("Email is not in standord format ")  

email_check()