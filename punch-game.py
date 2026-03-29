import turtle

t = turtle.Turtle()
t.color("blue")
t.speed(0)

screen = turtle.Screen()
screen.tracer(0)
screen.listen()

def move_forward():
    t.forward(20)

def move_backward():
    t.backward(20)

def turn_left():
    t.left(15)

def turn_right():
    t.right(15)
running = True
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")

screen.onkey(move_forward, "Up")
screen.onkey(move_backward, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")

while running:
  screen.update()
