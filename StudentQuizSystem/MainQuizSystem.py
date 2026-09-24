import random 


PINK = "\033[38;2;255;183;206m"
YELLOW = "\033[38;2;255;255;0m"
GREEN = "\033[38;2;0;255;0m"
RED = "\033[38;2;255;0;0m"
RESET = "\033[0m"
hlpink = "\033[48;2;255;183;206m"
#black [38;2;0;0;0 ; 48;2;255;183;206]
answerpink = "\33[38;2;0;0;0;1;4;3;48;2;255;183;206m"
kulaypink = "\33[1;4;38;2;255;183;206m"
WHITE = "\033[3;38;2;255;255;255m"
normalwayt = "\033[38;2;255;255;255m"
BLUE = "\033[1;48;2;135;206;235;38;2;0;0;0m"

answer = [] # Q1 = a, Q2 = c, Q3 = b, Q4 = t
correct_answers = ["a", "c", "b", "t"]


def Questions_1():  
    print(f"{BLUE}                  🦋 🦋            🦋        {RESET}")
    print(f"{BLUE}Question #1🌷🌷🐇🌱🌷🌷🌱🌱🌷🌷🌷🌱🌱🌷🌷🌷🌱{RESET}")
    print(f"{hlpink} {RESET}"* 45)
    print(f"{kulaypink}These languages run code through an {RESET}")
    print(f"{kulaypink}interpreter built into your OS or browser{RESET}")
    print(f"{hlpink} {RESET}"* 45) 
    
    print(f"\n{YELLOW}[A]{RESET}{answerpink}Compiled Languages{RESET}")
    print(f"\n{YELLOW}[B]{RESET}{answerpink}Interpreted Languages{RESET}")
    print(f"\n{YELLOW}[C]{RESET}{answerpink}Query Languages{RESET}\n")
    
    while True:  
         sagot = input(f"Enter answer: ").lower().strip()
         
         if sagot == "a":
            print(f"\n{GREEN}[CORRECT ANSWER!!]{RESET}\n")
            answer.append(sagot)
            break
         elif sagot in ("b", "c"):
            print(f"{RED}[ WRONG ANSWER!! Correct answer is{RESET} A.{RED}]{RESET}\n")
            answer.append(sagot)
            break   
         else:  
            print(f"{RED}[Please enter letter{RESET} A. {RED}to{RESET} C. {RED}only]{RESET}")
         
def Question_2(): 
    print(f"{BLUE}                  🦋 🦋            🦋        {RESET}")
    print(f"{BLUE}Question #2🌷🌷🐇🌱🌷🌷🌱🌱🌷🌷🌷🌱🌱🌷🌷🌷🌱{RESET}")
    print(f"{hlpink} {RESET}"* 45)
    print(f"{kulaypink}What is an example of Requirements Analysis?{RESET}")
    print(f"{hlpink} {RESET}"* 45)
    print(f"\n{YELLOW}[A]{RESET}{answerpink}Gathers requirements from stakeholders.{RESET}")
    print(f"\n{YELLOW}[B]{RESET}{answerpink}Verify Documents{RESET}")
    print(f"\n{YELLOW}[C]{RESET}{answerpink}Review, organize and Identify Conflicts{RESET}\n")
    
    while True:
         sagot = input("Enter answer: ").lower().strip()
        
         if sagot == "c":
            print(f"\n{GREEN}[ CORRECT ANSWER!! keep going!! ]{RESET}\n")
            answer.append(sagot)
            break
         elif sagot in ("b", "a"):
            print(f"\n{RED}[ WRONG ANSWER!! Correct answer is{RESET} C. {RED}]{RESET}\n")
            answer.append(sagot)
            break
         else:
            print(f"{RED}[ Please enter letter{RESET} A. {RED}to{RESET} C. {RED}only{RESET} ]")
            
def Question_3():
    print(f"{BLUE}                  🦋 🦋            🦋        {RESET}")
    print(f"{BLUE}Question #3🌷🌷🐇🌱🌷🌷🌱🌱🌷🌷🌷🌱🌱🌷🌷🌷🌱{RESET}")
    print(f"{hlpink} {RESET}"* 45)
    print(f"{kulaypink}What is the correct way to create a {RESET}")
    print(f"{kulaypink}function in Python?                  {RESET}")
    print(f"{hlpink} {RESET}"* 45)
    print(f"\n{YELLOW}[A]{RESET}{answerpink}function.name():{RESET}\n")
    print(f"\n{YELLOW}[B]{RESET}{answerpink}Def function_name():{RESET}\n")
    print(f"\n{YELLOW}[C]{RESET}{answerpink}Create fuction_name():{RESET}\n")
    
    while True:
        sagot = input("Enter answer: ").lower().strip()
        
        if sagot == "b":
            print(f"\n{GREEN}[ CORRECT ANSWER!! kaya mo yan ]{RESET}\n")
            answer.append(sagot)
            break
        elif sagot in ("a", "c"):
            print(f"\n{RED}[ WRONG!! review ka pa ]{RESET}\n")
            answer.append(sagot)
            break
        else: 
            print(f"\n{RED}[ Please enter letter{RESET} A. {RED}to{RESET} C. {RED}only ]{RESET}\n")
            
def Question_4():
    print(f"{BLUE}                  🦋 🦋            🦋        {RESET}")
    print(f"{BLUE}Question #4🌷🌷🐇🌱🌷🌷🌱🌱🌷🌷🌷🌱🌱🌷🌷🌷🌱{RESET}")
    print(f"{hlpink} {RESET}"* 45)
    print(f"{kulaypink}Enter T if True F if False:{RESET}")
    print(f"{kulaypink}Python is a key sensitive programming language{RESET}")
    print(f"{hlpink} {RESET}"* 45)
    print("TRUE OR FALSE?")
    
    while True:
         sagot = input("Enter T or F only: ").lower().strip()
          
         if sagot == "t":
            print(f"\n{GREEN}[ CORRECT GOODJOB!! ]{RESET}\n")
            answer.append(sagot)
            break
         elif sagot == "f":
            print(f"{RED}WRONG!!! python is a key sensitive{RESET}")
            answer.append(sagot)
            break
         else:
            print(f"{RED}[Please chooce{RESET} T {RED}for True{RESET} F {RED}for False only]{RESET}")

def Question_5(): #dito papasok yung score
    print(f"\n Pick a number {YELLOW}[1]{RESET} {YELLOW}[2]{RESET} {YELLOW}[3]{RESET} ")
    user = int(input("Enter here: "))
    correct_word = "" #blank palang kasi dito papasok yung coorect word mamaya
    answ_user = "" #dito naman papasok answe ng user

    while True:     
        if user == 1: #pag yung user daw pinili is 1 lalabas tong nasa baba
            print(f"{BLUE}                  🦋 🦋            🦋        {RESET}")
            print(f"{BLUE}Question #5🌷🌷🐇🌱🌷🌷🌱🌱🌷🌷🌷🌱🌱🌷🌷🌷🌱{RESET}")
            print(f"{hlpink} {RESET}"* 45)
            print(f"{kulaypink}ARRANGE THE WORD.{RESET}\n{kulaypink}hint💡:this stores a value that can change{RESET}")
            word1 = "VARIABLE" #ang coorectanswer ay variable
            shufflemode = list(word1) #yung list() dito ihihiwalay yung mga letter
            random.shuffle(shufflemode) #dito bandang function na to is magshuffle 
            print("".join(shufflemode)) #tapos ipagdidikit para hindi hiwahiwalay yung letter na ginawa sa list kaya magiging magulo yung letter
            print(f"{hlpink} {RESET}"* 45)
            answ_user = input("Answer here: ")
            correct_word = word1 #dito naman sinabi na yung correct answ is word 1
            break #break lang ng loop
        elif user == 2: 
            print(f"{BLUE}                  🦋 🦋            🦋        {RESET}")
            print(f"{BLUE}Question #5🌷🌷🐇🌱🌷🌷🌱🌱🌷🌷🌷🌱🌱🌷🌷🌷🌱{RESET}") 
            print(f"{hlpink} {RESET}"* 45)
            print("ARRANGE THE WORD")
            word2 = "FUNCTION"
            shufflemode2 = list(word2)
            random.shuffle(shufflemode2)
            print("".join(shufflemode2))
            print(f"{hlpink} {RESET}"* 45)
            answ_user = input("Answer here: ")
            correct_word = word2
            break
        elif user == 3:
            print(f"{BLUE}                  🦋 🦋            🦋        {RESET}")
            print(f"{BLUE}Question #5🌷🌷🐇🌱🌷🌷🌱🌱🌷🌷🌷🌱🌱🌷🌷🌷🌱{RESET}")
            print(f"{hlpink} {RESET}"* 45)
            print("ARRANGE THE WORD")
            word3 = "LOOPS"
            shufflemode3 = list(word3)
            random.shuffle(shufflemode3)
            print("".join(shufflemode3))
            print(f"{hlpink} {RESET}"* 45)
            answ_user = input("Answer here: ")
            correct_word = word3
            break
            
        else: # pag wala nilagay yung user na 1-3 lalabas to 
            print(f"{RED}[Please pick 1, 2 or 3 only]{RESET}")
            user = int(input(" Pick a number 1-3 "))
            
     #dito na ilqlagay yung Quiz 5 na score magkahiwalay kasi puzzle to
    
    #kung yung sagot ng user ay parehas sa correct word
    if answ_user.strip().upper() == correct_word:
        print(f"\n{GREEN}[CORRECT ANSWER!! it was {correct_word}]{RESET}\n")
        return 1 #ipuplus 1 kasi correct so ibabalik yung points 1
    else:
        print(f"\n{RED}[WRONG!! the correct answer was {correct_word}]{RESET}\n")
        return 0 #zeri ang score
           

def show_score(plus_quiz5score): #yung scores at bonus score
    score = 0
    
    for sagot in range(len(answer)): #using len to measure ilan letter nasa loob
        if answer[sagot] == correct_answers[sagot]: #if == kada letter tama 
            score += 1  #plus 1 sa score

    score += plus_quiz5score  # add Q5's result (1 or 0) on top

    total = len(correct_answers) + 1  # +1 kasi may question 5
    percentage = round((score / total) * 100) # uwu percentage 
    
    print("\n" + "="*40)
    print(f"{PINK}YOUR FINAL SCORE{RESET}")
    print(f"Correct: {score} out of {total}")
    print(f"Grade: {percentage}%")
    
    if percentage == 100:
        print(f"{GREEN}Grabe naman super talino yarn PERFECT!!🥳{RESET}")
    elif percentage >= 50:
        print(f"{YELLOW}[ Good job! galing mo ]{RESET}")
    else:
        print(f"{RED}[ Ok lang bawi ka nalang ulit!! REVIEW PA:D ]{RESET}")
    print("="*40)


print(f"{PINK}✿✿–✿✿–✿✿{RESET}{BLUE}QUIZ{RESET}{PINK}✿✿–✿✿–✿✿{RESET}")
print(f"Enter {YELLOW}[1]{RESET} to start")
print(f"Enter {YELLOW}[2]{RESET} to exit")


while True:
    select = input("\nEnter here: ")
    
    if select == "1":
        # FIX: all 5 questions now actually get called, in the same
        # order as correct_answers, and Q5's bonus result is captured
        # and passed into show_score.
        Questions_1()
        Question_2()
        Question_3()
        Question_4()
        plus_quiz5score = Question_5()
        show_score(plus_quiz5score) 
        break
    elif select == "2":
        print("Goodbye!")
        break
    else:
        print(f"{RED}[Invalid! Enter 1 or 2 only!!]{RESET}")
