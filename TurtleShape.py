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
    turtle.forward(100)
    turtle.left(120)
    

turtle.mainloop()


