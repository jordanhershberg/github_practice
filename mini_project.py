#Question 3
def calculation(player1, player2):
   if player1 == player2:
      return 0
   elif player1 == "rock" and player2 == "scissors":
      return 2
   elif player1 == "scissors" and player2 == "rock":
      return 1
   elif player1 == "scissors" and player2 == "paper":
      return 2
   elif player1 == "paper" and player2 == "scissors":
      return 1
   elif player1 == "paper" and player2 == "rock":
      return 2
   elif player1 == "rock" and player2 == "paper":
      return 1
   elif (player1 != "rock" or player1 != "scissors" or player1 != "paper"
         or player2 != "rock" or player2 != "scissors" or player2 != "paper"):
      return 3


def rounds(player1name, player2name):

   player1 = input(player1name + " what is your choice?")
   player2 = input(player2name + " what is your choice?")
   winner = calculation(player1, player2)
   if winner == 0:
      print("It's a tie!")
   elif winner == 1:
      print(player1name + " wins!")
      return (winner)
   elif winner == 2:
      print(player2name + " wins!")
      return (winner)
   elif winner == 3:
      print("Invalid input. Please try again.")
      return rounds(player1name, player2name)
   return winner


def playGame():
   print(
       "Welcome to Scissors Paper Rock! In this game, paper beats scissors,"
       "scissors beats rock, and rock beats paper. The game will be best 2 out of 3."
       "Have fun!")
   player1name = input("What is player 1's name?")
   player2name = input("What is player 2's name?")
   if input("Would you like to play best of three rounds?"):
      print(
          "Of course you're playing best of three rounds! Nobody plays just one round"
          " of Scissors Paper Rock!")
   realwinner = 0
   player1points = 0
   player2points = 0
   while player1points < 2 and player2points < 2:
      realwinner = rounds(player1name, player2name)
      if realwinner == 0:
         continue
      elif realwinner == 1:
         player1points += 1
      elif realwinner == 2:
         player2points += 1

   if player1points > player2points:
      return (player1name + " wins the game! Congratulations!")
   elif player2points > player1points:
      return (player2name + " wins the game! Congratulations!")


print(playGame())