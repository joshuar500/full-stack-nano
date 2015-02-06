import turtle

def draw_window():
    window = turtle.Screen()
    window.bgcolor("blue")
    
    draw_jr()
#    draw_angie()
#    draw_bert()
    
    window.exitonclick()

def draw_jr():
    brad = turtle.Turtle()
    brad.shape("square")
    brad.color("green")
    brad.speed(10)

    brad.forward(100)
    brad.right(180)
    brad.forward(50)
    brad.left(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(50)
    brad.backward(50)

    brad.color("blue")

    brad.right(180)
    brad.forward(70)
    
    brad.color("green")

    brad.showturtle()
    brad.left(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(60)
    brad.right(90)
    brad.forward(50)
    brad.right(90)
    brad.forward(60)
    brad.left(130)
    brad.forward(60)
    
def draw_square(some_turtle):
    for i in range(1, 5):
        some_turtle.forward(100)
        some_turtle.right(90)
              

#def draw_angie():
#    angie = turtle.Turtle()
#    angie.shape("arrow")
#    angie.color("red")
#    angie.circle(100)
#
#def draw_bert():
#    bert = turtle.Turtle()
#    bert.shape("circle")
#    bert.color("yellow")
#    bert.forward(100)
#    bert.right(120)
#    bert.forward(100)
#    bert.right(120)
#    bert.forward(100)

draw_window()
