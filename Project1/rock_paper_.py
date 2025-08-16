'''
rock= -1
paper= 0
scissor=1
'''

import random
def get_computer_choice():
    return random.randint(-1,1)

def get_user_choice():
    get_user_choice = input("chose rock,paper,scissor: ").strip().lower()
    if (get_user_choice== "rock"):
        return -1
    elif (get_user_choice== "paper"):
        return 0
    elif (get_user_choice== "scissor"):
        return 1
    else:
        print ("Invalid options. Try again!")
        return get_user_choice()
        
def get_determine_winner(user, computer):
    if (user==computer):
        return "Match is Tie!"
    
    elif (user==-1 and computer==1):
        return "You Win!"
    elif (user== 0 and computer==-1):
        return "You Win!"
    elif (user== 1 and computer==0):
        return "You Win!"
    else:
        return "Computer Wins!"

while True:
    
    user_choice= get_user_choice()
    computer_choice= get_computer_choice()
    
    mapping_choice= {-1:"rock", 0:"paper", 1:"scissor"}
    
    print (f"\nyou choice {mapping_choice[user_choice]}")
    print (f"computer choice {mapping_choice[computer_choice]}")
    print (get_determine_winner(user_choice, computer_choice))
    
    play_again = input("\nPlay again? (y/n): ").strip().lower()
    if play_again != 'y':
        print("Thanks for playing!")
        break


  