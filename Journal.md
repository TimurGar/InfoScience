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

```.py
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
```

Class no.1

1. What did we do?

A model of traffic light

2. What did you learn?

We should use a delay() command because it breakes whole program

3. Question that I have

N/A

```.py
    timer = 0
def setup():
    size(600,600)
    strokeWeight(10)
    fill(255,255,255)
    stroke(0,0,0)
    rect(200,100,200,400,20)
    
    timer=millis()    
    
def draw():
    global timer
    # turn off all LED
  
    
    clear()
    if millis()> timer + 1000:
        # red
        clear()
        fill(255,0,0)
        circle(300,180,100)
    if millis()> timer + 10000:
        # yellow
        clear()
        fill(255,255,0)
        circle(300,300,100)
        print(timer)
    
    if millis()> timer + 13000:
        clear()
        fill(0,255,0)
        circle(300,420,100)
        print(timer)
        
    if millis()> timer + 20000:
        timer = millis()

def clear():
    fill(128,0,0)
    circle(300,180,100)
    fill(149,143,24)
    circle(300,300,100)
    fill(0,100,0)
    circle(300,420,100)
```
