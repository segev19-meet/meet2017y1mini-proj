
import turtle
import random #We'll need this later in the lab
turtle.tracer(1,0) #This helps the turtle move more smoothly
SIZE_X=900
SIZE_Y=600


turtle.setup(SIZE_X, SIZE_Y) #Curious? It's the turtle window
#size.
turtle.penup()
SQUARE_SIZE = 20





START_LENGTH = 2
#Initialize lists
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []
#Set up positions (x,y) of boxes that make up the snake
snake = turtle.clone()
snake.color("green")
snake.shape("circle")
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
LEFT_ARROW="Left"
DOWN_ARROW="Down"
RIGHT_ARROW="Right"
TIME_STEP=100

SPACEBAR="space"


UP=0
LEFT=1
DOWN=2
RIGHT=3



direction= UP
UP_EDGE=250
DOWN_EDGE=-250
RIGHT_EDGE=400
LEFT_EDGE=-400






def up():
    global direction
    direction=UP
    print("you pressed the up key!")
    
    
               

def down():
    global direction
    direction=DOWN
    print("you pressed the down key!")



def left():
    global direction
    direction=LEFT
    print("you pressed the left key!")



def right():
    global direction
    direction=RIGHT
    print("you pressed the right key!")


turtle.onkeypress(up, UP_ARROW)
turtle.onkeypress(down, DOWN_ARROW)
turtle.onkeypress(left, LEFT_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)
turtle.listen()


def make_food():
    min_x=-int(800/2/SQUARE_SIZE)+1
    max_x=int(800/2/SQUARE_SIZE)-1
    min_y=-int(500/2/SQUARE_SIZE)-1
    max_y=int(500/2/SQUARE_SIZE)+1

    food_x=random.randint(min_x, max_x)*SQUARE_SIZE
    food_y=random.randint(min_y, max_y)*SQUARE_SIZE
    food.goto(food_x, food_y)
    new_list=(food_x, food_y)
    food_pos.append(new_list)
    new_stamp=food.stamp()
    food_stamps.append(new_stamp)



    
    
def move_snake():
    my_pos=snake.pos()
    x_pos=my_pos[0]
    y_pos=my_pos[1]


    if direction==RIGHT:
        snake.goto(x_pos+SQUARE_SIZE, y_pos)
        print("you moved right!")
    elif direction==LEFT:
        snake.goto(x_pos-SQUARE_SIZE, y_pos)
        print("you moved left!")


    
    elif direction==UP:
        snake.goto(x_pos, y_pos+SQUARE_SIZE)
        print("you moved up!")
    else:
        snake.goto(x_pos, y_pos-SQUARE_SIZE)
        print("you moved down!")

    new_pos=snake.pos()
    new_x_pos=new_pos[0]
    new_y_pos=new_pos[1]

    if new_x_pos>=RIGHT_EDGE:
        print("you hit the right edge! Game over!")
        quit()

    elif new_x_pos<=LEFT_EDGE:
        print("you hit the left edge! Game over!")
        quit()

    elif new_y_pos>=UP_EDGE:
        print("you hit the up edge! Game over!")
        quit()

    elif new_y_pos<=DOWN_EDGE:
        print("you hit the down edge! Game over!")
        quit()

    my_pos=snake.pos()
    pos_list.append(my_pos)
    new_stamp=snake.stamp()
    stamp_list.append(new_stamp)
    global food_stamps, food_pos
    if snake.pos()in food_pos:
        food_ind=food_pos.index(snake.pos())
        food.clearstamp(food_stamps[food_ind])
        food_pos.pop(food_ind)
        food_stamps.pop(food_ind)
        print("you have eaten the food!")
        make_food()
    else:
        old_stamp=stamp_list.pop(0)
        snake.clearstamp(old_stamp)
        pos_list.pop(0)
    

    
    if snake.pos() in pos_list[0:-1]:
        print("Gmem over!")
        quit()



    turtle.ontimer(move_snake, TIME_STEP)

move_snake()


turtle.register_shape("trumpy.gif")
food=turtle.clone()
food.shape("trumpy.gif")



food_pos=[(100,100)]
food_stamps=[]
for this_food_pos in food_pos:
    food.goto(this_food_pos[0],this_food_pos[1])
    stamp_id = food.stamp()
    food_stamps.append(stamp_id)
    




        
    

        
        
        
        
        

