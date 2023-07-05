# import random() class
import random

# list of available colors
colors = ["B", "G", "Y", "R", "C", "P", "D", "W"]

# color codes for changing console string color and style
PURPLE = '\033[95m'
CYAN = '\033[96m'
DARK_CYAN = '\033[36m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
DARK_GREY = '\33[90m'
WHITE = '\033[97m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
END = '\033[0m'


# function for Easy Game Mode
def easy():

    print("\nLets Start!")

    # randomly select four colors from color list to generate secret code
    code = random.choices(colors, k=4)
    print(code)
    print("\nA secret code is generated... Start guessing!")

    print("\nTo guess the colors, enter:\n'B' for Blue\n'G' for Green\n'R' for Red\n'Y' for Yellow\n"
          "'C' for Cyan\n'P' for Purple\n'D' for Dark Grey\n'W' for White\n")

    # start counter for number of attempts
    counter = 0

    # get the guessed list
    while True:

        guess = input("\nGuess(eg: BPRY = Blue, Purple, Red, Yellow):").upper()
        chars = list(guess)

        # increment counter
        counter += 1
        wrongcolor = []

        # start if statement to check length of user input
        if len(chars) == 4:

            # start for loop to check for wrong input color
            for characters in chars:
                if characters in colors:
                    pass
                else:
                    wrongcolor.append(characters)

            # start if statement for no wrong color input
            if len(wrongcolor) == 0:

                correct = 0
                result = 0

                # print message when user guessed the correct code
                if chars == code:

                    print(BOLD + "\nYOU'VE GUESSED THE SECRET CODE!!!!" + END)
                    print('Number of attempt(s): ' + str(counter))
                    print('\nThe secret code: ')

                    for element in code:

                        if element == 'B':
                            print(BLUE + 'BLUE' + END + ' ', end='')
                        elif element == 'C':
                            print(CYAN + 'CYAN' + END + ' ', end='')
                        elif element == 'R':
                            print(RED + 'RED' + END + ' ', end='')
                        elif element == 'Y':
                            print(YELLOW + 'YELLOW' + END + ' ', end='')
                        elif element == 'P':
                            print(PURPLE + 'PURPLE' + END + ' ', end='')
                        elif element == 'G':
                            print(GREEN + 'GREEN' + END + ' ', end='')
                        elif element == 'D':
                            print(DARK_GREY + 'DARK GREY' + END + ' ', end='')
                        elif element == 'W':
                            print(WHITE + 'WHITE' + END + ' ', end='')

                    print()

                    # start while loop to ask if user wants to try again
                    while True:
                        again = input('\nDo you want to try again?(Yes/No)\n').lower()

                        if again == 'yes':
                            start()
                            break

                        elif again == 'no':
                            print('Thank you for playing Mastermind!!')
                            break

                        else:
                            print('Please enter Yes or No')
                    break

                # check for numbers of correct colors and positions
                else:
                    guess_temp = []
                    code_temp = []

                    for i in range(4):
                        if chars[i] == code[i]:
                            correct += 1
                        else:
                            guess_temp.append(chars[i])
                            code_temp.append(code[i])

                    for j in range(len(guess_temp)):
                        if guess_temp[j] != code_temp[j] and code_temp[j] in guess_temp:
                            result += 1

                    print('Number(s) of color(s) guessed correctly and in correct position: '
                          + str(correct))
                    print('Number(s) of color(s) guessed correctly but in wrong position: ' + str(result))

            # print message for wrong color input
            else:
                print(str(wrongcolor) + ' is/are not an available color(s)')

        # print message for wrong input length
        else:
            print("Please enter a 4-colors combination to guess the code")


# function for Medium Game Mode
def medium():

    print("\nLets Start!")

    # randomly pick four colors from color list
    code = random.choices(colors, k=4)

    print("\nA secret code is generated... Start guessing!")

    print("To guess the colors, enter:\n'B' for Blue\n'G' for Green\n'R' for Red\n'Y' for Yellow\n"
          "'C' for Cyan\n'P' for Purple\n'D' for Dark Grey\n'W' for White\n")

    # set counter for number of attempts
    counter = 0

    # start while loop to get the guessed list
    while True:

        # start if statement for attempts limit
        if counter <= 15:

            # get user input
            guess = input("\nGuess(eg: BPRY = Blue, Purple, Red, Yellow):").upper()
            chars = list(guess)

            # increment counter
            counter += 1

            wrongcolor = []

            # check length of user input
            if len(chars) == 4:

                # start for loop to check if user input the available color
                for characters in chars:
                    if characters in colors:
                        pass
                    else:
                        wrongcolor.append(characters)

                # start if statement for user input all available colors
                if len(wrongcolor) == 0:

                    result = 0
                    correct = 0

                    # print message when user guessed the correct code
                    if chars == code:

                        print(BOLD + "\nYOU'VE GUESSED THE SECRET CODE!!!!" + END)
                        print('Number of attempt(s): ' + str(counter))
                        print('\nThe secret code: ')

                        for element in code:

                            if element == 'B':
                                print(BLUE + 'BLUE' + END + ' ', end='')
                            elif element == 'C':
                                print(CYAN + 'CYAN' + END + ' ', end='')
                            elif element == 'R':
                                print(RED + 'RED' + END + ' ', end='')
                            elif element == 'Y':
                                print(YELLOW + 'YELLOW' + END + ' ', end='')
                            elif element == 'P':
                                print(PURPLE + 'PURPLE' + END + ' ', end='')
                            elif element == 'G':
                                print(GREEN + 'GREEN' + END + ' ', end='')
                            elif element == 'M':
                                print(DARK_GREY + 'DARK GREY' + END + ' ', end='')
                            elif element == 'W':
                                print(WHITE + 'WHITE' + END + ' ', end='')

                        print()

                        # start while loop to ask if user want to play again
                        while True:
                            again = input('\nDo you want to try again?(Yes/No)\n').lower()

                            if again == 'yes':
                                start()
                                break

                            elif again == 'no':
                                print('Thank you for playing Mastermind!!')
                                break

                            else:
                                print('Please enter Yes or No')
                        break

                    # check number of correct color and position
                    else:

                        guess_temp = []
                        code_temp = []

                        for i in range(4):
                            if chars[i] == code[i]:
                                correct += 1
                            else:
                                guess_temp.append(chars[i])
                                code_temp.append(code[i])

                        for j in range(len(guess_temp)):
                            if guess_temp[j] != code_temp[j] and code_temp[j] in guess_temp:
                                result += 1

                        print('Number(s) of color(s) guessed correctly and in correct position: '
                              + str(correct))
                        print('Number(s) of color(s) guessed correctly but in wrong position: ' + str(result))

                # print message for wrong input color
                else:
                    print(str(wrongcolor) + ' is/are not an available color(s)')

            # print message for wrong input length
            else:
                print("Please enter a 4-colors combination to guess the code")

        # print message when user used up all attempts
        else:
            print("\nUh oh.. You used up all your attempts...")

            # start while loop to check if user want to play again
            while True:
                again = input('\nDo you want to try again?(Yes/No)\n').lower()

                if again == 'yes':
                    start()
                    break

                elif again == 'no':
                    print('Thank you for playing Mastermind!!')
                    break

                else:
                    print('Please enter Yes or No')
            break


# function for Hard Game Mode
def hard():
    print("\nLets Start!")

    # randomly pick four colors from color list
    code = random.choices(colors, k=4)

    print("\nA secret code is generated... Start guessing!")

    print("To guess the colors, enter:\n'B' for Blue\n'G' for Green\n'R' for Red\n'Y' for Yellow\n"
          "'C' for Cyan\n'P' for Purple\n'D' for Dark Grey\n'W' for White\n")

    # set counter for number of attempts
    counter = 0

    # start while loop to get the guessed list
    while True:

        # start if statement for attempts limit
        if counter <= 10:

            # get user input
            guess = input("\nGuess(eg: BPRY = Blue, Purple, Red, Yellow):").upper()
            chars = list(guess)

            # increment counter
            counter += 1

            wrongcolor = []

            # check length of user input
            if len(chars) == 4:

                # start for loop to check if user input the available color
                for characters in chars:
                    if characters in colors:
                        pass
                    else:
                        wrongcolor.append(characters)

                # start if statement for user input all available colors
                if len(wrongcolor) == 0:

                    result = 0
                    correct = 0

                    # print message when user guessed the correct code
                    if chars == code:

                        print(BOLD + "\nYOU'VE GUESSED THE SECRET CODE!!!!" + END)
                        print('Number of attempt(s): ' + str(counter))
                        print('\nThe secret code: ')

                        for element in code:

                            if element == 'B':
                                print(BLUE + 'BLUE' + END + ' ', end='')
                            elif element == 'C':
                                print(CYAN + 'CYAN' + END + ' ', end='')
                            elif element == 'R':
                                print(RED + 'RED' + END + ' ', end='')
                            elif element == 'Y':
                                print(YELLOW + 'YELLOW' + END + ' ', end='')
                            elif element == 'P':
                                print(PURPLE + 'PURPLE' + END + ' ', end='')
                            elif element == 'G':
                                print(GREEN + 'GREEN' + END + ' ', end='')
                            elif element == 'M':
                                print(DARK_GREY + 'DARK GREY' + END + ' ', end='')
                            elif element == 'W':
                                print(WHITE + 'WHITE' + END + ' ', end='')

                        print()

                        # start while loop to ask if user want to play again
                        while True:
                            again = input('\nDo you want to try again?(Yes/No)\n').lower()

                            if again == 'yes':
                                start()
                                break

                            elif again == 'no':
                                print('Thank you for playing Mastermind!!')
                                break

                            else:
                                print('Please enter Yes or No')
                        break

                    # check number of correct color and position
                    else:

                        guess_temp = []
                        code_temp = []

                        # start for loop to check correct position and color
                        for i in range(4):
                            if chars[i] == code[i]:
                                correct += 1
                            else:
                                guess_temp.append(chars[i])
                                code_temp.append(code[i])

                        # start for loop to check correct color but wrong position
                        for j in range(len(guess_temp)):
                            if guess_temp[j] != code_temp[j] and code_temp[j] in guess_temp:
                                result += 1

                        print('Number(s) of color(s) guessed correctly and in correct position: '
                              + str(correct))
                        print('Number(s) of color(s) guessed correctly but in wrong position: ' + str(result))

                # print message for wrong input color
                else:
                    print(str(wrongcolor) + ' is/are not an available color(s)')

            # print message for wrong input length
            else:
                print("Please enter a 4-colors combination to guess the code")

        # print message when user used up all attempts
        else:
            print("\nUh oh.. You used up all your attempts...")

            # start while loop to check if user want to play again
            while True:
                again = input('\nDo you want to try again?(Yes/No)\n').lower()

                if again == 'yes':
                    start()
                    break

                elif again == 'no':
                    print('Thank you for playing Mastermind!!')
                    break

                else:
                    print('Please enter Yes or No')
            break


# function to start game
def start():

    # start while loop to get user input for game mode
    while True:
        mode = input("\nPlease choose a Game Mode(Easy/Medium/Hard)\n").lower()

        if mode == 'easy':
            easy()
            break

        elif mode == 'medium':
            medium()
            break

        elif mode == 'hard':
            hard()
            break

        else:
            print("Please enter Easy, Medium or Hard...\n")


# instructions
def instruction():

    # print rules and gameplay for the game
    print(BOLD + "\nGAMEPLAY AND RULES" + END)
    print("1. A secret code is generated for each round of game play. The code is made up of four colors "
          "(Color choice: Blue, Green, Red, Yellow, Cyan, Purple)\n"
          "2. Your task is to guess the secret code. Enter one combination of four colored code for each turn. "
          "Note that one color has the chance to be used more than once in the secret code.\n"
          "3. To guess the colors, enter:\n\t'B' for Blue\n\t'G' for Green\n\t'R' for Red\n\t'Y' for Yellow\n\t"
          "'C' for Cyan\n\t'P' for Purple\n\t'D' for Dark Grey\n\t'W' for White\n"
          "4. After each guess, you will be informed of your progress in the game. You will know:\n"
          "\t1. The number of color(s) that is/are correctly guessed and in the correct position\n"
          "\t2. The number of color(s) that is/are correctly guessed but in the wrong position\n"
          "5. At the end of the game, you will be informed the number of attempt(s) you took to guess the secret "
          "code\n"
          "6. There are three Game Modes available:\n\tEasy: unlimited attempts\n\tMedium: 15 attempts\n\tHard: 10 "
          "attempts\n")


# print welcome message when user first launch the game
print('\n//////MASTERMIND//////' + END)

# start while loop to get user input for start game, instructions or quit game
while True:

    Input = input('Please enter "Start Game" to start playing Mastermind, "Help" to view the Gameplay and Rules of '
                  'Mastermind and "Quit" to end the program\n')

    if Input.lower() == "start game":
        start()

        break

    elif Input.lower() == "help":
        instruction()

    elif Input.lower() == "quit":

        # start while loop to confirm user wants to quit game
        while True:
            quit_game = input("Are you sure you want to quit Mastermind?(Yes/No)\n")

            if quit_game.lower() == 'yes':
                print("\nHope to see you soon... :(")
                loop = True
                break

            elif quit_game.lower() == 'no':
                loop = False
                break

            else:
                print("\nPlease enter 'Yes' or 'No'")
                loop = False

        if loop:
            break

        else:
            continue

    else:
        print("\nPlease enter a correct input..")
        continue

# end of program
