#EXTRA (INTERNET PROBLEM)
from turtle import *
 
bgcolor('black')
speed(0)
hideturtle()
for i in range(200):
     color('purple')
     circle(i)
     color("blue")
     circle(i*0.9)
     left(3)
     backward(5)
done()
