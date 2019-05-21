
"""This code features a binary guessing game. The computer is supposed to guess
the number that the user thinks about by using binary search."""


def main():
    def Rules():  # for rules
        print(
            "\nGAME RULES: \nIf your secret number is higher - 'higher' \nIf your secret number is lower - 'lower' \nIt's correct - 'yes' \nStop Game - 'stop' or 'STOP' \n ")

    Rules()

    while True:  # input validation
        try:
            user = int(input(
                "Let's play a guessing game. Input a number between 1 and 20000, and I will try to guess it by using binary search:  "))
            break
        except ValueError:
            print("Whoops! I don't think that was a number :(. Try again. ")

    if user > 20000:  # another validation
        print("\nThe number is too high. \n")
        main()
    elif user < 1:
        print("\nThe number is too low. \n")
        main()

    max = 20000
    min = 1

    while True:
        mid = (
              max - min) / 2 + min  # formula to find the middle number between min and max (10000 in the first iteration)
        mid = round(mid)  # round the number, because if it's a float it would make the program very slow
        print("Is your secret number, by any chance? " + str(mid))
        guess = input()
        if guess == 'higher':  # if user num is higher
            min = mid  # for the next iteration
        elif guess == 'lower':  # if user num is lower
            max = mid
        elif guess == 'yes':
            print('Game is over. Your secret number was: ' + str(mid))
            restart = input('Would you like to play again? Y/N')
            if restart == 'y' or restart == 'Y':
                main()  # restart functionality
            else:
                print('Goodbye :(')
                break
        elif guess == 'STOP' or guess == "stop":
            print('Game stopped. Goodbye.')
            break
        else:
            print("Sorry, can't quite understand what you are saying =(")
            Rules()


main()
