player1 = 'paper'
player2 = 'paper'

#tie
if player1 == player2:
    print("It's a Tie")
    #player 1 wins
elif player1 == "paper":
    if player2 == "rock":
        print("Player 1 wins")
        #player2 wins
elif player2 == "Scissors":
    if player1 == "paper":
        print("Player2 wins")
        #player1 wins
elif player2 == "Scissors":
    if player1 == "rock":
        print("player1 wins")