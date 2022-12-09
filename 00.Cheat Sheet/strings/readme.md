## STRING OPERATIONS
  
  #### String Concatenation
  - You can concatenate 2 or more strings to create a new string with `+`
  - You can repeatedly concatenate the same string with `*`
  ``` Python
  greeting = "Hello " + "Angela"
  # greeting is "Hello Angela"
  
  name = "Felix"
  greeting = "Hello " + name + "!"
  # greeting is "Hello Felix!"
  
  two_greetings = "Hello" * 2
  print(two_greetings)
  # HelloHello
  
  n = 4
  four_greetings = "Hello" * n
  print(four_greetings)
  # HelloHelloHelloHello
  ```
      
  #### Escaping a String
  Because the double quote is special, it denotes a string, if you want to use it in a string, you need to escape it with a `\`
  ``` Python
  speech = "She said: \"Hi\""
  print(speech)
  # prints: She said: "Hi"
  ```
  
  #### More Escaping in a String
  ```python
  print("\"")
  print('\'')
  print("\\")
  print("\tHello")
  print("First line\nNew line")
  print("\tWhat is\tyour\nname?")
  ```
   
  #### F-Strings
  You can insert a variable into a string using f-strings. The syntax is simple, just insert the variable in-between a set of curly braces `{}`.
  ``` Python
  days = 365
  print(f"There are {days} in a year")
  ```

  #### String Methods
  To change the case of a string, use the methods `title()`, `upper()` and `lower()`.
  ```python
  name = "alice in wonderland"
  print(name.title())             # Alice In Wonderland
  print(name.upper())             # ALICE IN WONDERLAND
  print(name.lower())             # alice in wonderland
  ```
  
  To remove extra whitespace from strings, use method `lstrip()`, `rstrip()` and `strip()`
  ```python
  name = ' jordan '
  print(name.lstrip())             # 'jordan '
  print(name.rstrip())             # ' jordan'
  print(name.strip())              # 'jordan'
  ```

  #### String Length
  Use `len()` function to get string length
  ```python
  s = "Hello, World!"
  print(len(s))
  ```
  
  #### String Index
  You can access a character in a string with index (***Remember***: index starts at 0)
  ```python
  # Get the character at position 1 which is 'e'
  s = "Hello, World!"
  print(s[1])
  ```
  
  #### Loop a String
  You can loop through the characters in a string with a `for` loop.
  ```python
  # Loop through letters in string 'Hello, World!'
  str = "Hello, World!"
  for x in str:
      print(x)
  ```
   
  #### String Slicing
  You can get a part of string by slice syntax (Specify the start index and the end index which are separated by a colon).
  ```python
  # Get the characters from position 2 to position 5 (not included)
  str = "Hello, World!"
  print(str[2:5])       # 'llo'
  ```
 
  
  
