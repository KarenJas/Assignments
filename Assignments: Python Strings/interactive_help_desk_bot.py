'''3. Interactive Help Desk Bot'''

text_input = input("How can I best help you today? : ")
user_data = []

if "help" in text_input:
    help = input("what do you need help with? : ")
    user_data.append(help)
elif "issue" in text_input:
    issue = input('What seems to be the issue? : ')
    user_data.append(issue)
    if "login" in issue:
        print("This is a login issue ")
    elif "performance" in issue:
        print("This is a performance issue")
    elif "error" in issue:
        print("This is a error issue ")
elif "contact support" in text_input:
    contact_support = input("What department would you like to contact (a,b,c)? : ")
    user_data.append(contact_support)


print(user_data)


