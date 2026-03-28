import turtle

t = turtle.Turtle()
t.color("blue")

def on_key_press(event):
  if event.char == "a":
    t.color("red")
    
