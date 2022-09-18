import getpass
moves = ["rock", "paper", "scissor"]

while True:
    player1 = getpass.getpass(prompt="Player 1: Scissor, Paper, Rock: ")
    player2 = getpass.getpass(prompt="Player 2: Scissor, Paper, Rock: ")

    if (player1 == player2):
        print("ITS A TIE")
    elif player1 == "Rock" or player1 == "rock":
      if player2 == "Paper" or player2 == "paper":
        print("Player 2 WINS!")
    elif player1 == "Paper" or player1 == "paper": 
      if player2 == "Rock" or player2 == "rock" :
        print("Player 1 WINS!")
    elif player1 == "Scissor" or player1 == "scissor": 
      if player2 == "Rock" or player2 == "rock":
        print("Player 2 WINS!")   
    if player1 == "Rock" or player1 == "rock": 
      if player2 == "Scissor" or player2 == "scissor":
        print("Player 1 WINS!")
    if player1 == "Scissor" or player1 == "scissor": 
      if player2 == "Paper" or player2 == "paper":
        print("Player 1 WINS!")
    if player1 == "Paper" or player1 == "paper": 
      if player2 == "Scissor" or player2 == "scissor":
        print("Player 2 WINS!")
    