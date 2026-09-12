import turtle

k = turtle.getscreen()
turtle.getscreen()
turtle.shape("turtle")

#Square
turtle.penup()
turtle.goto(-700,400) 

turtle.pendown()

for i in range(4):
    turtle.forward(100)
    turtle.right(90)

# rectangle
turtle.penup()
turtle.goto(-500,400)

turtle.pendown()

for i in range(2):
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    
# Triangle
turtle.penup()
turtle.goto(-200,300)

turtle.pendown()

for i in range(3):
    turtle.forward(120)
    turtle.left(120)
    
# Pentagon
turtle.penup()
turtle.goto(20,290)

turtle.pendown()

for i in range(5):
    turtle.forward(80)
    turtle.left(72)
    
# Hexagon
turtle. penup()
turtle.goto(300,280)

turtle.pendown()

for i in range(6):
    turtle.left(60)
    turtle.forward(80)
    
# Circle
turtle.penup()
turtle.goto(450,280)

turtle.pendown()

for i in range(175):
    turtle.forward(2)
    turtle.left(2)
    
turtle.mainloop()


