'''from turtle import*
clr=["blue","green","yellow","red"]
pensize(3)
for r in range(6):
    for n in clr:
        color(n)
        rt(15)
        for j in range(4):
            fd(100)
            rt(90)'''

from turtle import*
clr=["purple","green","yellow","red"]
pensize(3)
for r in range(4):
    rt(90)
    size=100
    for n in clr:
        color("black",n)
        begin_fill()
        for j in range(4):
            fd(size)
            rt(90)
        end_fill()
        size=size-20
        
