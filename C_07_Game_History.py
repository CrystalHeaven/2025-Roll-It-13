
# initialise list to hold game history
game_history = []

# get data (base component does this already, code below fore testing purposes

while True:
    rounds_played = input("Round? ")
    if rounds_played == "":
        break

    user_points = int(input("User points? "))
    comp_points = int(input("Computer points"))
    winner = input("Who won? ")
    user_score = int(input("User score: "))
    comp_score = int(input("Computer score: "))

    game_results = f"Round {rounds_played}: User Points  {user_points} | " \
                   f"Computer Points {comp_points}, {winner} wins ({user_score} | " \
                   f"{comp_score})"

    game_history.append(game_results)

# output game history using game history list
print("Game History")

for item in game_history:
    print(item)
