## 1. BASICS
  #### Print
  Prints a string into the console.
  ``` Python
  print("Hello World")
  ```
  
  #### Input
  Prints a string into the console, and asks the user for a string input.
  ``` Python
  input("What's your name? ")
  ```
  
  #### Comments
  Adding a # symbol in font of text lets you make comments on a line of code. The computer will ignore your comments.
  ``` Python
  #This is a comment
  print("This is code")
  ```
  
  #### Variables
  A variable give a name to a piece of data. Like a box with a label, it tells you what's inside the box.
  ``` Python
  my_name = "Angela"
  my_age = 12
  ```
  
  #### The += Operator
  This is a convient way of saying: "take the previous value and add to it."
  ``` Python
  my_age = 12
  my_age += 4
  # my_age is now 16
  ```

## 2. DATA TYPES
  #### Integers
  Integers are whole numbers.
  ``` Python
  my_number = 354
  ```
  
  #### Floating Point Numbers
  Floats are numbers with decimal places. When you do a calculation that results in a fraction e.g. 4 ÷ 3 the result will always be a floating point number.
  ``` Python
  my_float = 3.14159
  ```
  
  #### Strings
  A string is just a string of characters. It should be surrounded by double quotes.
  ``` Python
  my_string = "Hello"
  ```
  
  #### String Concatenation
  You can add strings to string to create a new string. This is called concatenation.It results in a new string.
  ``` Python
  "Hello" + "Angela"
  # becomes "HelloAngela"
  ```
      
  #### Escaping a String
  Because the double quote is special, it denotes a string, if you want to use it in a string, you need to escape it with a "\"
  ``` Python
  speech = "She said: \"Hi\""
  print(speech)
  # prints: She said: "Hi"
  ```
   
  #### F-Strings
  You can insert a variable into a string using f-strings. The syntax is simple, just insert the variable in-between a set of curly braces {}.
  ``` Python
  days = 365
  print(f"There are {days} in a year")
  ```
      
  #### Converting Data Types
  You can convert a variable from one data type to another.\
  Converting to float:\
  `float()`\
  Converting to int:\
  `int()`\
  Converting to string:\
  `str()`
  
  ``` Python
  n = 354
  new_n = float(n)
  print(new_n)      # result 354.0
  ```
      
  #### Checking Data Types
  You can use the `type()` function to check what is the data type of a particular variable.
  ``` Python
  n = 3.14159
  type(n)      #result float
  ```

## 3. MATHS
  #### Arithmetic Operators
  You can do mathematical calculations with Python as long as you know the right operators.
  ``` Python
  3+2   #Add
  4-1   #Subtract
  2*3   #Multiply
  5/2   #Divide
  5**2  #Exponent
  ```
      
  #### The += Operator
  This is a convenient way to modify a variable. It takes the existing value in a variable and adds to it. You can also use any of the other mathematical operators e.g. -= or *=
  ``` Python
  my_number = 6
  my_number += 2
  my_number *= 2
  my_number -= 1
  my_number /= 3
  ```
