import turtle
turtle.bgcolor('white')
turtle.speed(300)
turtle.pensize(4)

def draw_star_enby(x, y, side_length, angle):
   yp_pen = side_length/50
   blk_pen = side_length/33.333
   x1 = side_length/33.333
   y1 = side_length/-28.57
   x2 = side_length/66.666
   y2 = side_length/-60
   turtle.up()
   turtle.goto(x,y)
   turtle.left(angle)
   turtle.down()
   turtle.pensize(yp_pen)
   turtle.pencolor('yellow')
   for i in range (5):
     turtle.forward(side_length)
     turtle.right(144)
   turtle.penup
   turtle.goto(x+x1,y+y1)
   turtle.pendown
   turtle.pencolor('blueviolet')
   for i in range (5):
     turtle.forward(side_length)
     turtle.right(144)
   turtle.penup
   turtle.goto(x+x2,y+y2)
   turtle.pendown
   turtle.pencolor('black')
   turtle.pensize(blk_pen)
   for i in range (5):
     turtle.forward(side_length)
     turtle.right(144) 
   turtle.penup()
   turtle.goto(x,y)
   turtle.right(angle)
   turtle.pensize(5)

def draw_star_omni (x, y, side_length, angle):
   wdth = side_length/50
   step = wdth+wdth/40
   turtle.up()
   turtle.goto(x,y)
   turtle.left(angle)
   turtle.pensize(wdth)
   turtle.forward(side_length)
   turtle.right(144)
   turtle.down()
   turtle.pensize(wdth)
   for i in range (2):
      turtle.pencolor('pink')
      turtle.forward(side_length)
      turtle.right(90)
      turtle.forward(step)
      turtle.left(90)
      turtle.pencolor('hotpink')
      turtle.back(side_length)
      turtle.forward(side_length)
      turtle.right(144)
   for i in range (2):
      turtle.pencolor('cornflowerblue')
      turtle.forward(side_length)
      turtle.right(90)
      turtle.forward(step)
      turtle.left(90)
      turtle.pencolor('royalblue')
      turtle.back(side_length)
      turtle.forward(side_length)
      turtle.right(144)
   turtle.pencolor('indigo')
   turtle.pensize(wdth*2)
   turtle.forward(side_length)
   turtle.right(144)
   turtle.penup()
   turtle.goto(x,y)
   turtle.right(angle)
   turtle.pensize(5)

def draw_star_gf (x, y, side_length, angle):
   
   wdth = side_length/25
   turtle.up()
   turtle.goto(x,y)
   turtle.left(angle)
   turtle.pensize(wdth)
   turtle.down()
   turtle.pensize(wdth)
   turtle.pencolor('black')
   turtle.forward(side_length)
   turtle.right(144)
   turtle.pencolor('blue')
   turtle.forward(side_length)
   turtle.right(144)
   turtle.pencolor('hotpink')
   turtle.forward(side_length)
   turtle.right(144)
   turtle.pencolor('gainsboro')
   turtle.forward(side_length)
   turtle.right(144)
   turtle.pencolor('mediumorchid')
   turtle.forward(side_length)
   turtle.right(144)
   turtle.penup()
   turtle.goto(x,y)
   turtle.right(angle)
   turtle.pensize(5)
   turtle.pencolor('black')





def draw_star(x, y, side_length, angle):
  turtle.pencolor('black')
  turtle.up()
  turtle.goto(x,y)
  turtle.left(angle)
  turtle.down()
  for i in range (5):
    turtle.forward(side_length)
    turtle.right(144)
  turtle.right(angle)

## Star A (-296,190,340,10) ##
draw_star_enby (-296,190,340,10)


## Star B (51,271,153.88,15)##
turtle.up()
turtle.goto(51,271)
turtle.left(15)
turtle.down()
for i in range (5):
    turtle.forward(153.88)
    turtle.right(144)
turtle.right(15)

## Star C (38,118.5,131,-11.3)##
draw_star_gf (38,118.5,131,-11.3)

## Star E ##
turtle.up()
turtle.goto(-303,-59)
turtle.left(7.87)
turtle.down()
for i in range (5):
    turtle.forward(127)
    turtle.right(144)
turtle.right(10)

turtle.exitonclick()
