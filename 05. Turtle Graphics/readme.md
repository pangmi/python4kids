## Turtle Graphics

[Turtle graphics](https://docs.python.org/3.1/library/turtle.html) is a built-in Python library that enables users to create pictures and shapes by providing them with a virtual canvas. The onscreen pen that you use for drawing is called the turtle and this is what gives the library its name.

#### 1. Pixels and Coordinates

![image](https://user-images.githubusercontent.com/36340668/209741255-bdf03bf4-1e98-4dc5-8e68-52eb2faeb380.png)

#### 2. Setting Turtle Speed
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

#### 3. Keep Turtle Window Open in PyCharm
When running [Turtle graphics](https://docs.python.org/3.1/library/turtle.html) on PyCharm, you need to call `turtle.done()` at the end of the program to prevent the Turtle window from disappearing.

#### 4. Basic Operations
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

#### 5. Getting Input
- Pop up a dialog window for input of a string 
  ```python
  turtle.textinput(title, prompt)
  ```
     
- Pop up a dialog window for input of a number 
  ```
  turtle.numinput(title, prompt, default=None, minval=None, maxval=None)
  ```

#### 6. Filling Shapes with Color
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

### Homework
First of all, for each of the programs you create, please write a comment line which includes your name and current date at the top of your program like below:
```python
# Felix Zuo - 2022-11-27
```

1. Go over the following sections in [Python Cheat Sheet](https://github.com/pangmi/python4kids/blob/main/00.Cheat%20Sheet/readme.md)
   - [Tuples](https://github.com/pangmi/python4kids/blob/main/00.Cheat%20Sheet/tuple/readme.md)
   - [Conditionals](https://github.com/pangmi/python4kids/blob/main/00.Cheat%20Sheet/conditionals/readme.md)
   - [Loops](https://github.com/pangmi/python4kids/blob/main/00.Cheat%20Sheet/loops/readme.md)
   
1. Write a program with `turtle` graphics to create an 800x600 pixel window and then draw a green 300 x 200 rectangle using the `goto()` or `setpos()` function. The top-left corner of the rectangle should be (-150, 150)
   - ***hint***: you also may need to user `penup()` / `pendown()`
   
1. Write a program with `turtle` graphics to create an 800x600 pixel window and then draw a red 300 x 300 square using the `forward()`, `left()` and `right()` functions. The top-left corner of the rectangle should be (-100, 100)
   - ***hint***: you also may need to user `penup()` / `pendown()`

1. Write a program with `turtle` graphics to create a simple rosette like below:

    ![image](https://user-images.githubusercontent.com/36340668/210025974-7c230460-ba6c-4bd9-923a-cbea7f63a872.png)

1. Write a program with `turtle` graphics to create an emoji like below:

    ![image](https://user-images.githubusercontent.com/36340668/210026018-fd2b2382-70b3-4c94-8cd4-d8606f4e4beb.png)

1. **Distance Between Two Points**
   
   Create a function `get_distance(p1, p2)` to find the distance between two points on a coordinate plane. 
    ![image](https://user-images.githubusercontent.com/36340668/210028411-697449eb-60a3-4040-bdb3-ca24541779cc.png)
   
   ***Examples***
   ```python
   get_distance((-2, 1), (4, 3))                    # 6.325
   get_distance((0, 0), (1, 1))                     # 1.414
   get_distance((10, -5), (8, 16))                  # 21.095
   get_distance((14239, -11222), (-12301, 12888))   # 35856.153
   ```
   - The points `p1` and `p2` are tuples. See [Tuples](https://github.com/pangmi/python4kids/blob/main/00.Cheat%20Sheet/tuple/readme.md) on how to access them
   - You need to round up calculated distance up to 3 decimal place.

1. ** Sum of Digits**

   Create a function `sum_digits(n)` that takes a number and returns the sum of its digits.
   
   ***Examples***
   ```python
   sum_digits(5)          # 5
   sum_digits(123)        # 6 (1 + 2 + 3)
   sum_digits(456)        # 15 (4 + 5 + 6)
   sum_digits(8972)       # 26 (8 + 9 + 7 + 2)
   sum_digits(1445566)    # 31 (1 + 4 + 4 + 5 + 5 + 6 + 6)
   sum_digits(123456789)  # 45 (1 + 2 + 3 + ... + 9)   
   ```

1. **Same Parity?**
   
   Create a function `parity_analysis(n)` that takes a number as input and returns `True` if the sum of its digits has the same parity as the entire number. Otherwise, return `False`.
   
   ***Examples***
   ```python
   parity_analysis(243)         # True as 243 is odd and so is 9 (2 + 4 + 3)
   parity_analysis(12)          # False as 12 is even but 3 is odd (1 + 2)
   parity_analysis(182)         # False as 182 is even but 11 is odd (1 + 8 + 2)
   parity_analysis(3453)        # True as 3453 is odd and 15 is odd (3 + 4 + 5 + 3)
   parity_analysis(3)           # True as 3 is odd and 3 is odd (3)
   parity_analysis(123456789)   # True   
   ```
   - Parity is whether a number is even or odd. If the sum of the digits is even and the number itself is even, return `True`. The same goes if the number is odd and so is the sum of its digits.
   - Single digits will obviously have the same parities

