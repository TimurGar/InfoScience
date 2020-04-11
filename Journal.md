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
March 31 2020

1. What did we do?

I read an article "How your personal computer can help science battle the coronavirus while you sleep"　by John D'Anna for Arizona Republic Magazine.

Answered the questions.

2. What did you learn?

I learned that we can use our computers to find a ways to fight against COVID-19. You can dowload a program and while your are not your computer it can help scientists to find a ways to fight against COVID-19.

3. Question that I have

N/A



Online class no.1 
April 1 2020

1. What did we do?

I watched [e-learning] Video #1 and made a code in the end.

2. What did you learn?

That we can use abstraction in computer science to represent very complex things in a simple way. For example we know that every people are unique, they have different colors of eyes, height, weight, age, etc. But in our situation we know that this information is not important for us so can represent a human just as a circle. 

Code for the [e-learning] Video #1:

```.py
posX = 300
posY = 300

def setup():
    size(500,500)
    
def draw():
    global posX,posY
    background(255)
    strokeWeight(2)
    
    circle(posX, posY, 40) 
    posX = posX + random(-10,10)
    posY = posY + random(-10,10)
    
    if posX > 500:
        posX = 500
    if posX < 0:
        posX = 0
    if posY > 500:
        posY = 500
    if posY < 0:
        posY = 0
    
    delay(100)
```
3. Question that I have

Who can I test if my code is correct?

To check it, first, I commented out this two lines and a "delay(100)" command so that the circle(human) will not move randomly:
#posX = posX + random(-10,10)
#posY = posY + random(-10,10)

Then, instead of them I wrote this line:
posX = posX + 5
In this situation the circle(human) moved straight to the borther(right one) so that I would be able to check if it would stop when it will reach it.

Then, I deleted the previous line and I wrote this line:
posX = posX - 5
In this situation the circle(human) moved straight to the borther(left one) so that I would be able to check if it would stop when it will reach it.

Then, I deleted the previous line and I wrote this line:
posY = posY + 5
In this situation the circle(human) moved straight to the borther(Down one) so that I would be able to check if it would stop when it will reach it.

Then, I deleted the previous line and I wrote this line:
posY = posY - 5
In this situation the circle(human) moved straight to the borther(Up one) so that I would be able to check if it would stop when it will reach it.

After the test was done SUCCESSFULLY, I delete the previous line and agin paste this two lines and a "delay(100)" command: #posX = posX + random(-10,10)
#posY = posY + random(-10,10)

My second program

```.py
    Xlst = list()
    Ylst = list()
    Color = list()

    NumOfHumans = 40


    def setup():
        global Xlst,Ylst, NumOfHumans
        size(500,500)

        for i in range(NumOfHumans):
            ValX = int(random(50,450))
            Xlst.append(ValX)
            ValY = int(random(50,450))
            Ylst.append(ValY)

        print(Xlst)
        print(Ylst)  

    def draw():
        global Xlst,Ylst, NumOfHumans
        background(255)
        strokeWeight(2)

        for i in range(NumOfHumans):
            circle(Xlst[i], Ylst[i], 40) 
            Xlst[i] = Xlst[i] + random(-10,10)
            Ylst[i] = Ylst[i] + random(-10,10)

            if Xlst[i] > 500:
                Xlst[i] = 500
            if Xlst[i] < 0:
                Xlst[i] = 0
            if Ylst[i] > 500:
                Ylst[i] = 500
            if Ylst[i] < 0:
                Ylst[i] = 0

        delay(100)
```

Answering the questions:
What strategy is the most efficient to contain the spread of a virus in a general population?

The most efficient strategy in this situation is to declare a quarantine so that people are not able to go out of their homes, make a maximum distance for going out(may be up to 500 meters). Close the stores, except grocery stores and pharmacies.


In your opinion, should people enable access to the resources of their personal computers as tools for research? Are there any risks?

Of cource there is a risk, that people would be able to accept your personal data. But the advantages of using this type of method to find a way: 
    1. It can increase the speed of researching ways how to solve COVID-19.
    2. This program is optional, so if you afraid of it it is fine.
I think in this situation the risk is justified because everyone can probably safe a lot of lives without actually communicating with the affected.

What should be some behaviours (at least 3) that we will need to include in our simulation to be a realistic approximation of the current situation in the world? Explain.

    1. They should a wat from each other(a least 20px - may represent 2 meters) 
        Because now, people are trying to not come close to each other because they afraid to get a COVID-19.
    2. Stay in a groups of three people maximum.
        To again decrease the chance of getting COVID-19.
    3. Wear a masks to most of the people.
        To not spread the virus
    4. If a person doesn't have a mask, people will stay even futher(may be 75 px - 7.5 meters)
        Because almost everyone don't want to talk to a person who doesn't wear a mask.
    5. Add houses so that people will stay in it.
    


