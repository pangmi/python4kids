### Class Summary
  - Learn about variables
  - Learn about `input()`

#### 1. Variables
  - A variable give a name to a piece of data
  - A variable is like a label for a box in memory that holds a value
  - A computer's memory is made up of billions of boxes or locations that store data
  - A variable can reference different values while a program is running
    ```python
    myText = "Clara"
    print(myText)
    
    myText = "Felix"
    ```

#### 2. Variable Naming Rules
  - A variable name must start with a letter or the underscore character `_`
  - A variable name cannot start with a number
  - A variable name can only contain alphanumeric characters (A-Z, a-z, 0-9) or the underscore `_`
  - Variable names are case-sensitive
    ```python
    # The following code would create three separate variables
    myText = "abc"
    MYText = "abc"
    mytext = "abc" 
    ```

#### 3. Variable data types
  - Primitive Types
    - Whole number (integer)
    - Text (string)
    - Decimal number (float)
    - Boolean (True / False)
      ```python
      # Examples of variable data types
      myText = "Hello"        # a string variable
      cookieCount = 5         # an integer or whole number
      Pi = 3.14               # a decimal number also called a floating point number
      codingIsCool = True     # a boolean
      ```
  - Variable can hold complex data types called objects
    ```python
    # engine is a complex variable called an object
    engine = pyttsx3.init()
    engine.say("Hello")
    ```

#### Example 4 - Working with variables
  ```python
  firstName = "Matt"
  lastName = "Damon"

  firstName = "Jane"
  FirstPlayer = "Jane"
  numberOfPlayers = 2
  pi = 3.14
  isTodaySunny = True

  print(firstName)
  print(lastName)
  ```

#### Example 5 - Getting keyboard input
  ```python
  firstName = input("Type your first name and then press ENTER: ")
  lastName = input("Type your last name and then press ENTER: ")
  
  print(firstName)
  print(lastName)
  ```

#### Example 5 Continued - Format output with variables (F String)
  ```python
  firstName = input("Type your first name and then press ENTER: ")
  lastName = input("Type your last name and then press ENTER: ")
  
  outputText = f"Hello, your name is {firstName} {lastName}"
  print(outputText)
  ```

#### Example 6 - Starting a word game
  ```python
  # Jane {verb1} to the {place1} and bought a {noun1}
  verb1 = input("Enter a verb: ")
  place1 = input("Enter a place: ")
  noun1 = input("Enter a noun: ")
  print(f"Jane {verb1} to the {place1} and bought a {noun1}")
  ```

#### Example 7 - Starting a word game 2
  ```python
  import pyttsx3
  
  engine = pyttsx3.init()
  
  verb1 = input("Enter a verb: ")
  place1 = input("Enter a place: ")
  noun1 = input("Enter a noun: ")
  
  voices = engine.getProperty("voices")
  engine.setProperty("voice", voices[0].id)
  
  print(f"Jane {verb1} to the {place1} and bought a {noun1}")
  engine.say(f"Jane {verb1} to the {place1} and bought a {noun1}")
  
  engine.runAndWait()
  ```

#### Homework
  First of all, for each of the programs you create, please write a comment line which includes your name and current date at the top of your program like below:
  ```python
  # Felix Zuo - 2022-11-27
  ```
  1. Go over [Python Cheat Sheet](https://github.com/pangmi/python4kids/blob/main/00.Cheat%20Sheet/readme.md)
  1. Take the following short story and create a program that will prompt the user for the underlined words and replace them with what the user entered.
     > It was a <ins>adjective1</ins> summer day and <ins>personName</ins> was very hot. <ins>personName</ins> decided to <ins>verb1</ins> to the swimming pool. At the pool, the people <ins>verb2</ins>, <ins>verb3</ins>, <ins>verb4</ins> in the water. At the end of the day everyone left and went to the <ins>placeName</ins>

     - Have your program write the story with the underlined words replaced to the Shell window.
     - Also, have the computer read the story out loud with the replaced words.
     
     ***HINT***: You will need a variable for each underlined word
     
     Example Output:
     > It was a <ins>beautiful</ins> summer day and <ins>Julio</ins> was very hot. <ins>Julio</ins> decided to <ins>run</ins> to the swimming pool. At the pool, the people <ins>jumped</ins>, <ins>skipped</ins>, <ins>played</ins> in the water. At the end of the day everyone left and went to the <ins>store</ins>

  1. Create a function `dis` that takes two arguments: the original `price` and the `discount` percentage as integers and returns the final price after the discount.
     - Examples:
       ```python
       dis(1500, 50) ➞ 750
       dis(89, 20) ➞ 71.2
       dis(100, 75) ➞ 25
       ```

  1. Create a function `circle_or_square` that, given the radius of a circle and the area of a square, return `True` if the circumference of the circle is greater than the square's perimeter and `False` if the square's perimeter is greater than the circumference of the circle.
     - Examples:
       ```python
       circle_or_square(16, 625) ➞ True
       circle_or_square(5, 100) ➞ False
       circle_or_square(8, 144) ➞ True
       ```

  1. A number `N` is said to be a ***Curzon*** Number if `2**N + 1` is divisible by `2*N + 1`.
  
     Given a non-negative integer num, create a function `is_curzon` that returns True if num is a ***Curzon*** number, or False otherwise.
     - Examples:
       ```python
       is_curzon(5) ➞ True
       # 2 ** 5 + 1 = 33
       # 2 * 5 + 1 = 11
       # 33 is a multiple of 11
       
       is_curzon(10) ➞ False
       # 2 ** 10 + 1 = 1025
       # 2 * 10 + 1 = 21
       # 1025 is not a multiple of 21
       
       is_curzon(14) ➞ True
       # 2 ** 14 + 1 = 16385
       # 2 * 14 + 1 = 29
       # 16385 is a multiple of 29
       ```

1. Luke Skywalker has family and friends. Help him remind them who is who. Create a function that, given a name, returns the relation of that person to Luke.
   Person | Relation
   ------ | --------
   Darth Vader | father
   Leia	| sister
   Han	| brother in law
   R2D2 |	droid
   
   If the name is not in the table above, return "I'm a stranger"
   
   - Examples:
     ```python
     relation_to_luke("Darth Vader") ➞ "Luke, I am your father."
     relation_to_luke("Leia")        ➞ "Luke, I am your sister."
     
     relation_to_luke("Andor")       ➞ "I'm a stranger."
     ```
   

