# Weather Alert

import turtle

turtle.setup(800, 600)
turtle.title('Park Admisson Calculator')

t = turtle.Pen()
t.speed("fastest")
t.pencolor("blue")
t.penup()
t.hideturtle()

myfont = ("Arial", "30", "bold")
temp = turtle.numinput("TEMP", "Enter temperature:", 0, minval=0, maxval=120)
wind_speed = turtle.numinput("WIND SPEED", "Wind speed:", 0, minval=0, maxval=120)

if wind_speed is None:
    wind_speed = 0

if temp is None:
    t.write("YOU CANCELLED", align="center", font=myfont)
elif temp <= 32.00:
    t.pencolor("blue")
    t.write("It is FREEZING", align="center", font=myfont)

    if 20.0 < wind_speed < 40.0:
        t.goto(0, -100)
        t.write("Moderate Risk of frost bite", align="center", font=myfont)
    elif wind_speed >= 40.00:
        t.goto(0, -100)
        t.write("Sever Risk of frost bite", align="center", font=myfont)
elif 32.00 < temp < 70.0:
    t.pencolor("blue")
    t.write("It is COLD", align="center", font=myfont)
elif 70.0 <= temp <= 90:
    t.pencolor("red")
    t.write("It is WARM", align="center", font=myfont)
else:
    t.pencolor("red")
    t.write("It is HOT", align="center", font=myfont)

turtle.done()
