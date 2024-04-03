'''4. The Quiz Game'''

#Task 1: Develop a list of questions and answers.
questions = ["which is not a Hozier song:","which is not a Kendrick Lamar song:","which is not a Harry Style song:","which is not a Kali Uchis song:","which is not a Bad Bunny song:"]
hozier_answers = ["Take Me to Church", "Someone New", "From Eden", "Work Song", "King Kunta"]
kendrick_lamar_answers = ["HUMBLE.","Alright", "DNA.","Swimming Pools (Drank)", "Cherry Wine"]
harry_styles_answers = ["Watermelon Sugar","Sign of the Times","Adore You","Golden","Loner"]
kali_uchis_answers = ["Telepatía","After the Storm (feat. Tyler, The Creator & Bootsy Collins)","Isolation","Dead to Me","Falling"]
bad_bunny_answers = ["Dákiti (with Jhay Cortez)","Safaera (with Jowell & Randy and Ñengo Flow)","Yo Perreo Sola","La Noche de Anoche (with Rosalía)","Sale el Sol"]
score = 0

#Task 2: Write a function that quizzes the user and takes their answers.
def quiz():
    global score
    print(questions[0])
    for i in range(len(hozier_answers)):
        print(f"{i+1}) {hozier_answers[i]}")
    user_input1 = input("Answer:")
    if user_input1 == "King Kunta":
        score+=1

    print(questions[1])
    for i in range(len(kendrick_lamar_answers)):
        print(f"{i+1}) {kendrick_lamar_answers[i]}")
    user_input2 = input("Answer:")
    if user_input2 == "Cherry Wine":
        score+=1

    print(questions[2])
    for i in range(len(harry_styles_answers)):
        print(f"{i+1}) {harry_styles_answers[i]}")
    user_input3 = input("Answer:")
    if user_input3 == "Loner":
        score+=1

    print(questions[3])
    for i in range(len(kali_uchis_answers)):
        print(f"{i+1}) {kali_uchis_answers[i]}")
    user_input4 = input("Answer:")
    if user_input4 == "Falling":
        score+=1

    print(questions[4])
    for i in range(len(bad_bunny_answers)):
        print(f"{i+1}) {bad_bunny_answers[i]}")
    user_input5 = input("Answer:")
    if user_input5 == "Sale el Sol":
        score+=1

#Task 3: Score the quiz and give the user feedback on their performance.
    if score >= 3:
        print(f"You did great You got {score}/5!  :)")
    elif score <3 :
        print(f"You got {score}/5. Better luck next time :( ")

#Test
quiz()
