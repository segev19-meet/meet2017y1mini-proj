import turtle
import random #We'll need this later in the lab
turtle.tracer(1,0) #This helps the turtle move more smoothly
SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X, SIZE_Y) #Curious? It's the turtle window
#size.
turtle.penup()
SQUARE_SIZE = 20
START_LENGTH = 8
#Initialize lists
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []
#Set up positions (x,y) of boxes that make up the snake
snake = turtle.clone()
snake.shape("square")
#Hide the turtle object (it's an arrow - we don't need to see it)
turtle.hideturtle()






for i in range(START_LENGTH):
    x_pos=snake.pos()[0]
    y_pos=snake.pos()[1]
    x_pos+=SQUARE_SIZE

    my_pos=(x_pos,y_pos)
    snake.goto(x_pos,y_pos)
    pos_list.append(my_pos)
    new_stamp=snake.stamp()
    stamp_list.append(new_stamp)


UP_ARROW="Up"
LEFT_AROW="Left"
DOWN_ARROW="Down"
RIGHT_ARROW="Right"
TIME_STEP=100

SPACEBAR="space"


UP=0
LEFT=1
DOWN=2
RIGHT=3



direction= UP

def up():
    global direction
    direction=UP
    move_snake()
    print("you pressed the up key!")
    
    
               

direction= DOWN

def down():
    global direction
    direction=DOWN
    move_snake()
    print("you pressed the down key!")




    
direction= LEFT

def left():
    global direction
    direction=LEFT
    move_snake()
    print("you pressed the left key!")





direction= RIGHT

def right():
    global direction
    direction=RIGHT
    move_snake()
    print("you pressed the right key!")


    turtle.onkeypress(up, UP_ARROW)
    turtle.listen()
    turtle.onkeypress(down, DOWN_ARROW)
    turtle.listen()
    turtle.onkeypress(left, LEFT_ARROW)
    turtle.listen()
    turtle.onkeypress(right, RIGHT_ARROW)
    turtle.listen()


def move_snake():
    my_pos=snake.pos()
    x_pos=my_pos[0]
    y_pos=my_pos[1]
        
        
        
        
        

