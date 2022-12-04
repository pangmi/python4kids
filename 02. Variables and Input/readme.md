### Class Summary
  - Learn about variables
  - Learn about `input()`

#### 1. Variables
  - A variable give a name to a piece of data
  - A variable is like a label for a box in memory that holds a value
  - A computer's memory is made up of billions of boxes or locations that store data
  - A variable can reference different values while a program is running
    ``` Python
    myText = "Clara"
    print(myText)
    
    myText = "Felix"
    ```

#### 2. Variable Naming Rules
  - A variable name must start with a letter or the underscore character `_`
  - A variable name cannot start with a number
  - A variable name can only contain alphanumeric characters (A-Z, a-z, 0-9) or the underscore `_`
  - Variable names are case-sensitive
    ``` Python
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
      ``` Python
      # Examples of variable data types
      myText = "Hello"        # a string variable
      cookieCount = 5         # an integer or whole number
      Pi = 3.14               # a decimal number also called a floating point number
      codingIsCool = True     # a boolean
      ```
  - Variable can hold complex data types called objects
    ``` Python
    # engine is a complex variable called an object
    engine = pyttsx3.init()
    engine.say("Hello")
    ```

#### Example 4 - Working with variables
  ``` Python
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
  ``` Python
  firstName = input("Type your first name and then press ENTER: ")
  lastName = input("Type your last name and then press ENTER: ")
  
  print(firstName)
  print(lastName)
  ```

#### Example 5 Continued - Format output with variables (F String)
  ``` Python
  firstName = input("Type your first name and then press ENTER: ")
  lastName = input("Type your last name and then press ENTER: ")
  
  outputText = f"Hello, your name is {firstName} {lastName}"
  print(outputText)
  ```

#### Example 6 - Starting a word game
  ``` Python
  # Jane {verb1} to the {place1} and bought a {noun1}
  verb1 = input("Enter a verb: ")
  place1 = input("Enter a place: ")
  noun1 = input("Enter a noun: ")
  print(f"Jane {verb1} to the {place1} and bought a {noun1}")
  ```

#### Example 7 - Starting a word game 2
  ``` Python
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
  ``` Python
  # Felix Zuo - 2022-11-27
  ```

  1. Take the following short story and create a program that will prompt the user for the underlined words and replace them with what the user entered.
     > It was a <ins>adjective1</ins> summer day and <ins>personName</ins> was very hot. <ins>personName</ins> decided to <ins>verb1</ins> to the swimming pool. At the pool, the people <ins>verb2</ins>, <ins>verb3</ins>, <ins>verb4</ins> in the water. At the end of the day everyone left and went to the <ins>placeName</ins>

     Example Output:
     > It was a <ins>beautiful</ins> summer day and <ins>Julio</ins> was very hot. <ins>Julio</ins> decided to <ins>run</ins> to the swimming pool. At the pool, the people <ins>jumped</ins>, <ins>skipped</ins>, <ins>played</ins> in the water. At the end of the day everyone left and went to the <ins>store</ins>

  1. (*Not that challenging* from [edabit](https://edabit.com/challenge/)) Write a function `stutter(word)` that stutters a word as if someone is struggling to read it. The first two letters are repeated twice with an ellipsis `...` and space after each, and then the word is pronounced with a question mark `?`.
     - Assume all input is at least two characters long.
     - For example:
       ``` Python
       stutter("incredible") ➞ "in... in... incredible?"
       stutter("enthusiastic") ➞ "en... en... enthusiastic?"
       stutter("outstanding") ➞ "ou... ou... outstanding?"
       ```
  
  
