# Park Admisson Calculator
# Children 2 and under are FREE
# Children age 3 to 12 are $5.00
# People age 13 to 64 are $7.00
# People 65 and older are FREE

import turtle

turtle.setup(800, 600)
turtle.title('Park Admisson Calculator')

t = turtle.Pen()
t.speed("fastest")
t.pencolor("blue")
t.penup()
t.hideturtle()

# get the person's age
age = turtle.numinput("AGE INPUT", "Please enter age:", 12, minval=1, maxval=120)

# calculate their admission
cost = 0.00

# draw the total in my turtle window
if age <= 2 or age >= 65:
    cost = 0.00
elif 3 <= age <= 12:
    cost = 5.00
else:
    cost = 7.00

t.write(f"Your total is ${cost:.2f}", align="center", font=("Courier", "25", "bold"))

turtle.done()
