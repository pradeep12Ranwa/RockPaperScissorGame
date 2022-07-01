import random
from logs import logger


logger.info("Info:Welcome note")
print("---------------------------------------------")
print("Welcome to rock,paper,scissor Game")
print("---------------------------------------------")
possible_actions = ["rock", "paper", "scissors"]

# Printing the selection of user and computer
def printSelection(user_action,computer_action):
    logger.info("Info: into printSelection function")
    return (f"\nYou chose {user_action}, computer chose {computer_action}.\n")

# Printing action when it's a tie
def tie(user_action):
    logger.info("Info: into tie function")
    return (f"Both Users selected {user_action}. It's a tie!")

#result after taking input from user and computer
def gameAfterInput(user_action,computer_action,userCount,computerCount):
    logger.info("Info: Into gameAfterInput function")
    #tie cases
    if user_action == computer_action:
        print( tie(user_action))
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win one point")
            userCount+=1
        else:
            print("Paper covers rock! Computer win one point.")
            computerCount+=1
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win one point")
            userCount+=1
        else:
            print("Scissors cuts paper! Computer win one point.")
            computerCount+=1
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win one point")
            userCount+=1
        else:
            print("Rock smashes scissors!Computer win one point.")
            computerCount+=1
    #showing current score
    print(f"Current Score User= {userCount} and Computer={computerCount}\n")
    #returning current score of User and computer
    return userCount,computerCount

#winner declaration is done in this function
def winnerDeclaration(userCount,computerCount,MaxPoints):
    logger.info("Info: Into the winnerDeclaration function")
    if(userCount==MaxPoints):
        return "Congratualions you won against computer\n"
    else:
        return "Sorry! You lost against computer! Better luck next time\n"

def game():
    while True:   
        
        #Taking input the max number of points where a User wins
        logger.info("Info: Taking MaxPoints as input")
        while(True):
            MaxPoints=int(input("Enter the number of points to win the game by any User: "))
            if(MaxPoints>0):
                break
            else:
                print("Wrong input please input integer greater than 0")
                logger.error("Error: invalid input for Maxpoints")
       
        logger.info("Info: Starting the game")
        print("Starting the Game")
        print("--------------------------------------------------")
        global userCount
        global computerCount
        userCount=0
        computerCount=0

        #looping until any one wins
        while (userCount<MaxPoints and computerCount<MaxPoints):

            while(True):
                user_action = input("Enter a choice (rock, paper, scissors): ")
                if(user_action=="rock" or user_action=="paper" or user_action=="scissors"):
                    break;
                else:
                    print("Wrong input please enter a valid choice")
                    logger.error("Error: wrong input for user_action")
            computer_action = random.choice(possible_actions)
            print(printSelection(user_action,computer_action))
            userCount,computerCount = gameAfterInput(user_action,computer_action,userCount,computerCount)
            
        
        logger.info("Info: Game stopped as one Player wins")
        print(winnerDeclaration(userCount,computerCount,MaxPoints))
        print("-----------------------------------------")

        #asking for another game
        playAgain = input("Want to play Again? (y/n): ")
        if playAgain.lower() != "y":
            break
    logger.info("Info: game over")

#main function
if __name__ == "__main__":
    game()
    
    
    
    
        
        
        
        
        