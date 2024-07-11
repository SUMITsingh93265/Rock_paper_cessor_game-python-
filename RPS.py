import random
import time

print()
print("*Note:- 1) If you win you get 10 points.")
print("        2) Your win or lose depends on the final score.")
time.sleep(5)
print()
print("So without wasting any time let start the game.")
print()
print("********************************************************************************************************")
print("***************************************** Let's start the game *****************************************")
print("********************************************************************************************************")
print()
results = []
while True:
    num = random.randint(1, 3)
    if num == 1:
        comp_move = "Rock"
        user_move = input("Select your move : ")
        if comp_move == "Rock" and user_move.capitalize() == "Rock":
            print("Computer choose Rock.")
            print("Game Draw")
            results.append("Game draw")
            game_con = input(
                "Do you want to continue the game type (Yes/yes) if you want to quit type (No/no) : ")
            if game_con.capitalize() == "Yes":
                print()
            elif game_con.capitalize() == "No":
                break
            else:
                print("I think you have type something wrong. If you want to continue the game type (Yes/yes) or you want to quit the game type (No/no).")

        elif comp_move == "Rock" and user_move.capitalize() == "Paper":
            print("Computer choose Rock.")
            print("You win.")
            results.append("You win")
            game_con = input(
                "Do you want to continue the game type (Yes/yes) if you want to quit type (No/no) : ")
            if game_con.capitalize() == "Yes":
                print()
            elif game_con.capitalize() == "No":
                break
            else:
                print("I think you have type something wrong. If you want to continue the game type (Yes/yes) or you want to quit the game type (No/no).")

        elif comp_move == "Rock" and user_move.capitalize() == "Cessor":
            print("Computer choose Rock.")
            print("You lose.")
            print("Computer win.")
            results.append("Computer win")
            game_con = input(
                "Do you want to continue the game type (Yes/yes) if you want to quit type (No/no) : ")
            if game_con.capitalize() == "Yes":
                print()
            elif game_con.capitalize() == "No":
                break
            else:
                print("I think you have type something wrong. If you want to continue the game type (Yes/yes) or you want to quit the game type (No/no).")

    elif num == 2:
        comp_move = "Paper"
        user_move = input("Select your move : ")
        if comp_move == "Paper" and user_move.capitalize() == "Rock":
            print("Computer choose Paper.")
            print("You lose.")
            print("Computer win.")
            results.append("Computer win")
            game_con = input(
                "Do you want to continue the game (Yes/yes) if you want to quit type (No/no) : ")
            if game_con.capitalize() == "Yes":
                print()
            elif game_con.capitalize() == "No":
                break
            else:
                print("I think you have type something wrong. If you want to continue the game type (Yes/yes) or you want to quit the game type (No/no).")
        elif comp_move == "Paper" and user_move.capitalize() == "Paper":
            print("Computer choose Paper.")
            print("Game draw.")
            results.append("Game draw")
            game_con = input(
                "Do you want to continue the game (Yes/yes) if you want to quit type (No/no) : ")
            if game_con.capitalize() == "Yes":
                print()
            elif game_con.capitalize() == "No":
                break
            else:
                print("I think you have type something wrong. If you want to continue the game type (Yes/yes) or you want to quit the game type (No/no).")
        elif comp_move == "Paper" and user_move.capitalize() == "Cessor":
            print("Computer choose Paper.")
            print("You win.")
            results.append("You win")
            game_con = input(
                "Do you want to continue the game (Yes/yes) if you want to quit type (No/no) : ")
            if game_con.capitalize() == "Yes":
                print()
            elif game_con.capitalize() == "No":
                break
            else:
                print("I think you have type something wrong. If you want to continue the game type (Yes/yes) or you want to quit the game type (No/no).")

    elif num == 3:
        comp_move = "Cessor"
        user_move = input("Select your move : ")
        if comp_move == "Cessor" and user_move.capitalize() == "Rock":
            print("Computer choose Cessor.")
            print("You win.")
            results.append("You win")
            game_con = input(
                "Do you want to continue the game (Yes/yes) if you want to quit type (No/no) : ")
            if game_con.capitalize() == "Yes":
                print()
            elif game_con.capitalize() == "No":
                break
            else:
                print("I think you have type something wrong. If you want to continue the game type (Yes/yes) or you want to quit the game type (No/no).")
        elif comp_move == "Cessor" and user_move.capitalize() == "Paper":
            print("Computer choose Cessor.")
            print("You lose.")
            print("Computer win.")
            results.append("Computer win")
            game_con = input(
                "Do you want to continue the game (Yes/yes) if you want to quit type (No/no) : ")
            if game_con.capitalize() == "Yes":
                print()
            elif game_con.capitalize() == "No":
                break
            else:
                print("I think you have type something wrong. If you want to continue the game type (Yes/yes) or you want to quit the game type (No/no).")
        elif comp_move == "Cessor" and user_move.capitalize() == "Cessor":
            print("Computer choose Cessor.")
            print("Game draw.")
            results.append("Game draw")
            game_con = input(
                "Do you want to continue the game (Yes/yes) if you want to quit type (No/no) : ")
            if game_con.capitalize() == "Yes":
                print()
            elif game_con.capitalize() == "No":
                break
            else:
                print("I think you have type something wrong. If you want to continue the game type (Yes/yes) or you want to quit the game type (No/no).")

    else:
        print("Something went wrong.")

print()
print("********************************************************************************************************")
print("************************************************ Scores ************************************************")
print("********************************************************************************************************")
print()
print("Total (result/score).")

user_scores = 0
computer_scores = 0
game_draws = 0
for result in results:
    if result == "You win":
        user_scores = user_scores + 10
    elif result == "Computer win":
        computer_scores = computer_scores + 10
    elif result == "Game draw":
        game_draws += 1
    else:
        print(":(")

print()
print(f"Your score is {user_scores}")
print(f"Computer score is {computer_scores}")
print(f"Game draw {game_draws} times.")

print()
print("********************************************************************************************************")
print()
if user_scores > computer_scores:
    print("You Win the game. Congratulations")
elif user_scores < computer_scores:
    print("You Lose the game. Try again to win the game.")
elif user_scores == computer_scores:
    print("Game Draw your score and computer score is equal.")
else:
    print("Something went wrong.")

print()
print("********************************************************************************************************")
print("**************************** Thanks for playing this game hopw you like it. ****************************")
print("********************************************************************************************************")