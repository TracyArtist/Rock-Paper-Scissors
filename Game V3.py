player1 = 'paper'
player2 = 'rock'
player1 = 'spock'
player2 = 'lizard'

#tie
if player1 == player2:
    print("It's a Tie")
    #player 1 wins
elif player1 == "paper" or player1 == "spock" or player1 == "lizard":
    if player2 == "rock" or player2 == "spock" or player2 == "lizard":
        print("Player 2 wins")
        #player2 wins
elif player2 == "Scissors":
    if player1 == "paper":
        print("Player2 wins")
        #player1 wins
elif player2 == "Scissors":
    if player1 == "rock":
        print("player1 wins")