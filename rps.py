import random
print('Lets Play Rock,Paper,Scissors!')
valid_choice = ["Rock", "Paper", "Scissors"]
compchoice = random.choice(("Rock", "Paper", "Scissors"))
playerchoice = input("Choose: Rock, Paper, Scissors. ")
if playerchoice not in valid_choice:
    print("Let's try again")
else:
    if compchoice == "Rock" and playerchoice == 'Paper':
        print(' The Computer Has Selected ', compchoice)
        print('You Win!')
    elif compchoice == 'Rock' and playerchoice == 'Scissors':
        print(' The Computer Has Selected', compchoice)
        print('You Lose!')
    elif compchoice == 'Paper' and playerchoice == 'Rock':
        print('The Computer Has Selected', compchoice)
        print('You lose')
    elif compchoice == 'Paper' and playerchoice == 'Scissors':
        print ('The Computer Has Chosen', compchoice)
        print('You Win!')
    elif compchoice == 'Scissors' and playerchoice == 'Rock':
        print ('The Computer Has Chosen', compchoice)
        print ('You Win!')
    elif compchoice == 'Scissors' and playerchoice == 'Paper':
        print ('The Computer Has Chosen', compchoice)
        print ('You Lose!')
    elif compchoice == playerchoice:
        print ('The Computer Has Chosen', compchoice)
        print ("It's a Draw!")
