import turtle as t
colorlist=["red","blue","yellow","green","black","grey","white","oriange"]
for i in range(1,8):
    t.penup()
    t.sety(-15*i)
    t.pendown()
    t.pencolor(colorlist[i-1])
    t.circle(15*i)
    
