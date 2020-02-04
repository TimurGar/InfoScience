#This is journal

Class no.1

1. What did we do?

Made an algoritm how to make a bread with jelly.
2. What did you learn?

Compositive thinking.
3. Question that I have

N/A



Class no.2

1. What did we do?

Installed Python
Learned and practice many commands.

2. What did you learn?

How to write text on the window. 
How to work with text. Diferent to parameters(change size, textAlign).

Compositive thinking.
3. Question that I have

N/A

Today's code:

def setup():
    size(1000,1000)
    background(255)
    textAlign(CENTER)

def draw():
    print("")
    
def mouseClicked():
     x = random(0,1000)
     y = random(0,1000)
     s = random(10,100)
     R = random(0,255)
     G = random(0,255)
     B = random(0,255)
     fill(R,G,B)
     circle(mouseX,mouseY,s)
     print(R,G,B)
     fill(0)
     textSize(s/4)
    text("T&G",mouseX,mouseY)
