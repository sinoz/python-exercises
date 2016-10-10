# Constants
AMT_PLAYERS = 3
ADVANTAGES = {
   # Each choice has its advantages mapped in a dictionary for scalability
   'rock' : "scissors",
   'paper' : "rock",
   'scissors' : "paper"
}

# Mutable fields
choices = []
points = [0, 0, 0]

def poll_choices():
   for i in range(0, AMT_PLAYERS):
       choice = raw_input("Choose Rock/Paper/Scissors:").lower()
       # TODO: allow user to try again if an invalid choice was given
       if choice != "rock" and choice != "paper" and choice != "scissors":
           print "Invalid input, please choose Rock, Paper or Scissors."
           break

       choices.append(choice)

def present_points_per_player():
   for playerId in range(0, len(points)):
       print "Player", playerId, "has", points[playerId], "points"

def handout_points(player_idx, player_choice, opponent_choice):
    if ADVANTAGES[player_choice] == opponent_choice:
       points[player_idx] += 1

def play():
   for player_choice_idx in range(0, len(choices)):
       selected_choice = choices[player_choice_idx]
       for opponent_choice_idx in range(0, len(choices)):
           # To avoid the user from playing against him/herself
           if player_choice_idx == opponent_choice_idx:
               continue
           opponent_choice = choices[opponent_choice_idx]

           handout_points(player_choice_idx, selected_choice, opponent_choice)

poll_choices()
play()
present_points_per_player()