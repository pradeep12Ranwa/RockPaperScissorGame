
import random
# Starting the game
print("---------------------------------------------")
print("Welcome to rock,paper,scissor Game")
print("---------------------------------------------")
possible_actions = ["rock", "paper", "scissors"]

# Printing the selection of user and computer
def printSelection(user_action,computer_action):
    return (f"\nYou chose {user_action}, computer chose {computer_action}.\n")

# Printing action when it's a tie
def tie(user_action):
    return (f"Both players selected {user_action}. It's a tie!")

def gameAfterInput(user_action,computer_action,playerCount,computerCount):
    if user_action == computer_action:
        print( tie(user_action))
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win one point")
            playerCount+=1
        else:
            print("Paper covers rock! Computer win one point.")
            computerCount+=1
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win one point")
            playerCount+=1
        else:
            print("Scissors cuts paper! Computer win one point.")
            computerCount+=1
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win one point")
            playerCount+=1
        else:
            print("Rock smashes scissors!Computer win one point.")
            computerCount+=1
    print(f"Current Score Player= {playerCount} and Computer={computerCount}\n")
    return playerCount,computerCount

def winnerDeclaration(playerCount,computerCount,MaxPoints):
    if(playerCount==MaxPoints):
        return "Congratualions you won against computer\n"
    else:
        return "Sorry! You lost against computer! Better luck next time\n"

def game():
    while True:   
        MaxPoints=int(input("Enter the number of points to win the game by any player: "))
        print("Starting the Game")
        print("--------------------------------------------------")
        global playerCount
        global computerCount
        playerCount=0
        computerCount=0
        while (playerCount<MaxPoints and computerCount<MaxPoints):
            user_action = input("Enter a choice (rock, paper, scissors): ")
            computer_action = random.choice(possible_actions)
            print(printSelection(user_action,computer_action))
            playerCount,computerCount = gameAfterInput(user_action,computer_action,playerCount,computerCount)
        
        print(winnerDeclaration(playerCount,computerCount,MaxPoints))
        print("-----------------------------------------")
        playAgain = input("Want to play Again? (y/n): ")
        if playAgain.lower() != "y":
            break

if __name__ == "__main__":
    game()
    
    
    
    
        
        
        
        
        