## Make Decisions
- To make a decision, we use boolean variables or expressions that result in `True` or `False`
- Then we have the program run different code based on the `True`/`False` value

##### Booolean variables
```python
python_is_cool = True
english_is_fun = False
```

##### Boolean expressions
```python
myAge = 38
isAdult = myAge >= 18
isChild = myAge < 18
```

##### Conditional Statements and Boolean Operators
- See [Conditional Cheat Sheet](https://github.com/pangmi/python4kids/blob/20e3a265250b51cc9ec40593f0f445365bf5f6e0/00.Cheat%20Sheet/conditionals/readme.md)

##### Examples
- Display Different Messages for Different Ages
  ```python
  # Print "You are a child" if 12 or younger
  # Print "You are a teenage" if age is 13 to 17
  # Print "You are an adult" if age is 18 to 64
  # Print "You are a senior adult" if age is 65 or older

  myAge = int(input("Enter your age: "))
  if myAge <= 12:
      print("You are a child")
  elif 13 <= myAge <= 17:
      print("You are a teenage")
  elif 18 <= myAge <= 64:
      print("You are an adult")
  else:
      print("You are a senior adult")
  ```

- Park Admission Calculator
  ```python
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

  ```

