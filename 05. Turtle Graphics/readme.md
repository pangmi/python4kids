## Turtle Graphics

[Turtle graphics](https://docs.python.org/3.1/library/turtle.html) is a built-in Python library that enables users to create pictures and shapes by providing them with a virtual canvas. The onscreen pen that you use for drawing is called the turtle and this is what gives the library its name.

#### Pixels and Coordinates

![image](https://user-images.githubusercontent.com/36340668/209741255-bdf03bf4-1e98-4dc5-8e68-52eb2faeb380.png)

#### Setting Turtle Speed
You can change the speed of your turtle using the `speed()` function and passing it a value.
```python
# valid speed values are: "slowest", "slow", "normal", "fast", "fastest"
t.speed("fastest")
t.speed("normal")

# You can also set the speed using a numeric value from 0 to 10. 
t.speed(1)    # slowest
t.speed(6)    # normal
t.speed(10)   # fast
t.speed(0)    # fastest
```

#### Keep Turtle Window Open in PyCharm
When running [Turtle graphics](https://docs.python.org/3.1/library/turtle.html) on PyCharm, you need to call `turtle.done()` at the end of the program to prevent the Turtle window from disappearing.

#### Basic Operations
```python

# first, import turtle library
import turtle

# set screen size and/or starting position
turtle.setup(800, 600)      # or turtle.setup(800, 600, 50, 50)

# set screen color
turtle.bgcolor("gray")

# set screen title
turtle.title("My cool drawings")    

# initialize a variable to access turtle
t = turtle.Pen()

# set pen and outline color
t.pencolor('purple')

# set the line thickness with either of the following
t.width(5)
t.pensize(5)

# set turtle speed
t.speed(0)
t.speed(3)
t.speed("fastest")

# move the turtle
t.forward(100)
t.backward(200)

# turn the turtle
t.right(90)
t.left(90)

# draw a circle
t.circle(150)

# move the turtle to any position with either goto() or setpos()
t.goto(100, 100)
t.goto(-50, -40)
t.setpos(100, 50)

# Move turtle to the origin - coordinates (0,0).
t.home()

# Pull the pen up – no drawing when moving.
t.penup()

# Pull the pen down – drawing when moving.
t.pendown()

# Write text at the current turtle position
t.write("Hello world")
t.write(your_name, font=("Arial", 18, "bold"))

# set turtle shape:
t.shape('turtle')   # arrow, turtle, circle, square, triangle, classic

# set turtle color:
t.color('green')

# set turtle size
t.turtlesize(3, 3, 2)

# hide turtle
t.hideturtle()

# Delete the drawings from the screen. Do not move turtle.
t.clear()

# Delete the drawings and restore its default values.
t.reset()

```

#### Getting Input
- Pop up a dialog window for input of a string 
  ```python
  turtle.textinput(title, prompt)
  ```
     
- Pop up a dialog window for input of a number 
  ```
  turtle.numinput(title, prompt, default=None, minval=None, maxval=None)
  ```

#### Filling Shapes with Color
```python
# 1. set filling color
t.fillcolor("blue")

# 2. begin to fill
t.begin_fill()

# 3. draw a shape
for x in range(3):
    t.forward(200)
    t.left(120)

# 4. end filling
t.end_fill()

```
