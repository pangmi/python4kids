#### Class Content
  - Learn how to print out text
  - Learn to write comments in your program
  - Learn to escape characters in text
  - Learn to make computer speak

#### Sample code
  - Print out text and write comments
    ``` Python
    # This program demonstrates the output
    print("Hello World")
    print("Hello Sun")
    print("Hello Moon")
    
    # Escape characters
    print("\"A Penny Saved is a Penny Earned\" Benjamin Franklin")
    print('\'A Penny Saved is a Penny Earned\' Benjamin Franklin')
    
    # You can avoid escaping quote characters
    print("'A Penny Saved is a Penny Earned' Benjamin Franklin")
    print('"A Penny Saved is a Penny Earned" Benjamin Franklin')    
    ```

  - More escaping characters in print
    ``` Python
    print("\"")
    print('\'')
    print("\\")
    print("\tHello")
    print("First line\nNew line")
    print("\tWhat is\tyour\nname?")
    ```

  - Make your computer speak
    ``` Python
    import pyttsx3
    
    engine = pyttsx3.init()
    
    engine.say("Hello")
    engine.say("Good Bye.")
    
    engine.runAndWait()
    ```

#### Homework
  First of all, for each of the programs you create, please write a comment line which includes your name and current date at the top of your program like below:
  ``` Python
  # Felix Zuo - 2022-11-27
  ```

  1. Write a program that prints the names of your 5 favorite superheroes. ***Each name should be on its own line***.
  1. Use the `print()` function to print out an upside down triangle with asterisks like the one below
     ``` Python
     ***********
      *********
       *******
        *****
         ***
          *
     ```
  1. Use the `print()` function to output the rectangle below. 
     - Each line should be indented by one tab character
     - Can you modify you program so that you can output the rectangle with just one `print()` method?
     ``` Python
        \\\\
        \\\\
        \\\\
        \\\\
        \\\\
     ```
  1. Use the `print()` method to output the text below. ***Don’t forget to output the double quotes***
     ``` Python
     "Tell me and I forget. Teach me and I remember. Involve me and I learn." - Benjamin Franklin
     ```

  1. Write a program to make the computer recite the following poem:
     ``` Python
     Star light, star bright,
     The first star I see tonight;
     I wish I may, I wish I might,
     Have the wish I wish tonight.
     ```
  
  1. (*Not that challenging* from [edabit](https://edabit.com/challenge/)) Write a function `stutter(word)` that stutters a word as if someone is struggling to read it. The first two letters are repeated twice with an ellipsis `...` and space after each, and then the word is pronounced with a question mark `?`.
     - Assume all input is at least two characters long.
     - For example:
       ``` Python
       stutter("incredible") ➞ "in... in... incredible?"
       stutter("enthusiastic") ➞ "en... en... enthusiastic?"
       stutter("outstanding") ➞ "ou... ou... outstanding?"
       ```
  
  
