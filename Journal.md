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

Class no.3

1. What did we do?

A model of traffic light

2. What did you learn?

We shouldn't use a delay() command because it breakes whole program.
Istead you millis().

3. Question that I have

N/A

Today's code:
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
Class no.4

1. What did we do?

Install Tinkercad, make a circuit of the traffic light, made a code for it.

2. What did you learn?

How to use Tinkercad to create a circuits.

3. Question that I have

N/A

Today's code:
```.py

int But =0;


void setup()
{

  pinMode(13, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(2, INPUT);
}

void loop()
{
 
 
  digitalWrite(13, HIGH);
  delay(1000); // Wait for 1000 millisecond(s)
  digitalWrite(13, LOW);
  delay(1000); // Wait for 1000 millisecond(s)
  
  digitalWrite(12, HIGH);
  delay(1000); // Wait for 1000 millisecond(s)
  digitalWrite(12, LOW);
  delay(1000); // Wait for 1000 millisecond(s)
  
  digitalWrite(11, HIGH);
  delay(1000); // Wait for 1000 millisecond(s)
  digitalWrite(11, LOW);
  delay(1000); // Wait for 1000 millisecond(s)
}
```
Online class no.1 
April 1 2020

1. What did we do?

I read an article "How your personal computer can help science battle the coronavirus while you sleep"　by John D'Anna for Arizona Republic Magazine.

Answered the questions.

2. What did you learn?

I learned that we can use our computers to find a ways to fight against COVID-19. You can dowload a program and while your are not your computer it can help scientists to find a ways to fight against COVID-19.

Questions:
What strategy is the most efficient to contain the spread of a virus in a general population?

The most efficient strategy in this situation is to declare a quarantine so that people are not able to go out of their homes, make a maximum distance for going out(may be up to 500 meters). Close the stores, except grocery stores and pharmacies.

In your opinion, should people enable access to the resources of their personal computers as tools for research? Are there any risks?

Of cource there is a risk, that people would be able to accept your personal data. But the advantages of using this type of method to find a way: 
    1. It can increase the speed of researching ways how to solve COVID-19.
    2. This program is optional, so if you afraid of it it is fine.
I think in this situation the risk is justified because everyone can probably safe a lot of lives without actually communicating with the affected.
    


3. Question that I have

N/A
