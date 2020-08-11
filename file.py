from appJar import gui
import sys
import random
from time import sleep

app = gui(showIcon = False)

app.setTitle("Magic 8-Ball")
app.setIcon("assets/sport_8ball.gif")

def press(button):
    if button == "Ask":
        sleep(0.25)
        app.setImage("empty", "assets/rotate1.gif")
        sleep(0.7)
        app.setImage("empty", "assets/rotate2.gif")
        sleep(0.7)
        app.setImage("empty", "assets/rotate3.gif")
        answer = app.getEntry("Ask the Magic 8-Ball Something")
        print(answer)
        if answer == "":
            sleep(1)
            app.setImage("empty", "assets/19.gif")
        else:
            responses = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
            randresponse = random.choice(responses)
            app.setImage("empty", "assets/" + str(randresponse) + ".gif")
    elif button == "Clear":
        app.setImage("empty", "assets/empty.gif")
        app.clearEntry("Ask the Magic 8-Ball Something", callFunction=True)
    elif button == "Exit":
        sys.exit(0)

app.addLabel("l1", "Magic 8-Ball")
app.addImage("empty", "assets/empty.gif")
app.addLabelEntry("Ask the Magic 8-Ball Something")
app.addButtons(["Ask", "Clear", "Exit"], press)
app.go()