import random
import sys


# Magic 8 ball program made my kaleb (klebdotio)
# you may add more responses into the "answers" list
# if the program does not work it may be because you do not
# have the random or sys library installed

exitvar = "Exit"
# Change to change the word that exits the program

print("Exit the program by typing 'Exit'")
while True:
    inp = input("Please ask the Magic 8-Ball Something: ")

    if inp == exitvar:
        sys.exit()
    # exit code, checks if the input is the exit word

    answers = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes - definitely', 'You may rely on it',
               'As I see it, yes', 'Most likely', 'Outlook good', 'Yes', 'Signs point to yes', 'Reply hazy, try again',
               'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again',
               'Dont count on it', 'My reply is no', 'My sources say no']
    # all of the magic 8 ball responses, feel free to add more

    randchoice = random.choice(answers)
    # randomly chooses a response and prints it out

    print(randchoice)

# Protected under the MIT License see LICENSE for more info




