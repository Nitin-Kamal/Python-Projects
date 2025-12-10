import turtle
sprite = turtle.Turtle()
sprite.color('white')
sprite.shape('circle')
sprite.pensize(3)
sprite.pencolor('purple')
sprite.speed(0)
sprite.setposition(0, 0)
quit = ''
side1 = 90
side2 = 0
side3 = 270
side4 = 180
i = 0
side11 = 5
side22 = 5
side33 = 5
side44 = 5
while i < 100:
    i = i + 1
    print(i)
    if i == 18:
        side11 = side11 - 1
        side22 = side22 - 1
        side33 = side33 - 1
        side44 = side44 - 1
    if i == 62:
        side11 = side11 - 2
        side22 = side22 - 2
        side33 = side33 - 2
        side44 = side44 - 2
    side1 = side1 + side11
    side2 = side2 + side22
    side3 = side3 + side33
    side4 = side4 + side44
    sprite.setheading(0)
    sprite.left(side1)
    sprite.forward(100)
    sprite.right(30)
    sprite.forward(100)
    sprite.penup()
    sprite.setposition(0, 0)
    sprite.setheading(side1)
    sprite.pendown()
    sprite.right(30)
    sprite.forward(100)
    sprite.left(30)
    sprite.forward(100)
    sprite.penup()
    sprite.setposition(0, 0)
    sprite.setheading(side2)
    sprite.pendown()
    sprite.forward(100)
    sprite.right(30)
    sprite.forward(100)
    sprite.penup()
    sprite.setposition(0, 0)
    sprite.setheading(side2)
    sprite.right(30)
    sprite.pendown()
    sprite.forward(100)
    sprite.left(30)
    sprite.forward(100)
    sprite.penup()
    sprite.setposition(0, 0)
    sprite.pendown()
    sprite.setheading(side3)
    sprite.forward(100)
    sprite.right(30)
    sprite.forward(100)
    sprite.penup()
    sprite.setposition(0, 0)
    sprite.setheading(side3)
    sprite.right(30)
    sprite.pendown()
    sprite.forward(100)
    sprite.left(30)
    sprite.forward(100)
    sprite.penup()
    sprite.setposition(0, 0)
    sprite.pendown()
    sprite.setheading(side4)
    sprite.forward(100)
    sprite.right(30)
    sprite.forward(100)
    sprite.penup()
    sprite.setposition(0, 0)
    sprite.setheading(side4)
    sprite.right(30)
    sprite.pendown()
    sprite.forward(100)
    sprite.left(30)
    sprite.forward(100)
    sprite.penup()
    sprite.setposition(0, 0)
    sprite.pendown()



turtle.mainloop()