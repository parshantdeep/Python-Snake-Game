
import turtle
import time
from random import randint as spooky

delay = 0.1 # defining delay as 0.1

wn = turtle.Screen()
wn.title("Snake Multiplayer Game")
wn.bgcolor("purple")
wn.setup(width=800, height=800) #setup of screen (size)
wn.tracer(0) # Turns off the screen updates

#Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

segments = [] #Creating a list of segments of snake's body which increases as it eats food



#Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("brown")
food.penup()
food.goto(200,200)  #Setting the coordinates of food here
##No Turtle appears till now because wn.tracer turns off the screen updates and hence the module goes as fast as posiible
##and we can't see anything

# Functions 

def go_up():
    head.direction = "up"
def go_down():
    head.direction = "down"
def go_right():
    head.direction = "right"
def go_left():
    head.direction = "left"



def move():
    if head.direction == "up":
        y = head.ycor() # sets the value of y as current y coordinate of turtle
        head.sety(y + 20) #we use the last defined value of y here to change the y coordinate of turtle
    
    if head.direction == "down":
        y = head.ycor() # sets the value of y as current y coordinate of turtle
        head.sety(y - 20) #we use the last defined value of y here to change the y coordinate of turtle

    if head.direction == "right":
        x = head.xcor() # sets the value of y as current y coordinate of turtle
        head.setx(x + 20) #we use the last defined value of y here to change the y coordinate of turtle
    
    if head.direction == "left":
        x = head.xcor() # sets the value of y as current y coordinate of turtle
        head.setx(x - 20) #we use the last defined value of y here to change the y coordinate of turtle

#Keyboard Bindings

wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_right, "Right")
wn.onkeypress(go_left, "Left")

  


#main game loop
while True:          #Here is keeps updating the screen and hence produces an anti-effect as wn.tracer(0)
    wn.update()


    #Check for collision of snake with food
    if head.distance(food) < 20 :  #20 because each turtle's default dimention is 20 by 20 and hence from a center of one turtle to a center of another turtle, the distance is 20
        x = spooky(-390,390)
        y = spooky(-390,390)
        food.goto(x,y)
        
        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)
        
    if segments:
        segments[0].goto(head.xcor(), head.ycor())

    if head.xcor() < -390 or head.xcor() > 390 or head.ycor() > 390 or head.ycor() < -390 :
        time.sleep(0.5)
        for i in range(len(segments)):
            segments[i].getturtle().reset()
     
     

     


        
    
    
    for index in range (len(segments) - 1, 0 , -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

                                   
    move()

    time.sleep(delay) ##we are delaying each operation of loop by 0.1s so that we can see turtle moving


wn.mainloop() #what does this do


