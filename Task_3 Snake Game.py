# importing Libraries
import turtle
import random
import time

# creating turtle screen
screen = turtle.Screen()
screen.title('welcome to Snake Game')
screen.setup(width=900, height=700)
screen.tracer(0)
turtle.bgcolor('#1a1a1a')

# score
score = 0
delay = 0.1

# snake
snake = turtle.Turtle()
snake.speed(0)
snake.shape('circle')
snake.color('#FE0000')
snake.penup()
snake.goto(0, 0)
snake.direction = "stop"

# food
fruit = turtle.Turtle()
fruit.speed(0)
fruit.shape('turtle')
fruit.color('#A7C957')
fruit.penup()
fruit.goto(30, 30)

old_fruit = []

# Scoring
scoring = turtle.Turtle()
scoring.speed(0)
scoring.color('white')
scoring.penup()
scoring.hideturtle()
scoring.goto(0, 300)
scoring.write("Start Eating Turtles", align="center", font=("Calibri", 24, "bold"))

# define Function
def snake_go_up():
    if snake.direction != "down":
        snake.direction = "up"

def snake_go_down():
    if snake.direction != "up":
        snake.direction = "down"

def snake_go_left():
    if snake.direction != "right":
        snake.direction = "left"

def snake_go_right():
    if snake.direction != "left":
        snake.direction = "right"

def snake_move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)

    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)

    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)
    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)

# keyboard Functions
screen.listen()
screen.onkeypress(snake_go_up, "Up")
screen.onkeypress(snake_go_down, "Down")
screen.onkeypress(snake_go_left, "Left")
screen.onkeypress(snake_go_right, "Right")

# Main loop
while True:
    screen.update()
    # snake and fruit collision
    if snake.distance(fruit) < 20:
        x = random.randint(-290, 270)
        y = random.randint(-240, 240)
        fruit.goto(x, y)
        scoring.clear()
        score += 1
        scoring.write("Score: {}".format(score), align="center", font=("Calibri", 24, "bold"))
        delay -= 0.001

        # creating new_fruit
        new_fruit = turtle.Turtle()
        new_fruit.speed(0)
        new_fruit.shape('circle')
        new_fruit.color('#00fe1f')
        new_fruit.penup()
        old_fruit.append(new_fruit)

    # adding fruit to snake
    for index in range(len(old_fruit) - 1, 0, -1):
        a = old_fruit[index - 1].xcor()
        b = old_fruit[index - 1].ycor()

        old_fruit[index].goto(a, b)

    if len(old_fruit) > 0:
        a = snake.xcor()
        b = snake.ycor()
        old_fruit[0].goto(a, b)
    snake_move()

    # snake and border collision
    if snake.xcor() > 400 or snake.xcor() < -400 or snake.ycor() > 240 or snake.ycor() < -240:
        time.sleep(1)
        screen.clear()
        screen.bgcolor('#1a1a1a')
        scoring.goto(0, 0)
        scoring.write("    GAME OVER \n Your Score is {}".format(score), align="center",
                      font=("Calibri", 30, "bold"))

    # snake collision
    for food in old_fruit:
        if food.distance(snake) < 20:
            time.sleep(1)
            screen.clear()
            screen.bgcolor('#1a1a1a')
            scoring.goto(0, 0)
            scoring.write("    GAME OVER \n Your Score is {}".format(score), align="center",
                          font=("Courier", 30, "bold"))
    time.sleep(delay)
