import turtle as t
t.speed("fastest")
t.pensize(2)
t.penup()
t.goto(-200,-200)
t.pendown()
t.seth(0)
length=400
while(length !=0):
    t.fd(length)
    t.left(90)
    length=length-1.5
t.hideturtle   
t.done()
 


     
