## Tuples
  A tuple is an ordered collection of items that can ***NOT*** be modified. It is usually indicated by parentheses.
  
  If you try to modify an element in a tuple, you’ll get an error. Tuples are useful when you have a collection of items that shouldn’t change throughout the life of your program.

  - Elements in a tuple can be accessed using indexes
  ```python
  elementary_grades = (2, 3, 4, 5, 6)
  
  grade = elementary_grades[0]      # 2
  grade = elementary_grades[-1]     # 6
  
  grades = elementary_grades[:2]    # (2, 3)
  ```
  
  - You can loop through a tuple using a `for` loop
  ```python
  elementary_grades = (2, 3, 4, 5, 6)
  for grade in elementary_grades:
      print(f"Welcome to grade {grade}!")
  ```

  - Unpack Tuples
  ```python
  fruits = ("apple", "banana", "cherry")
  (green, yellow, red) = fruits
  print(green)
  print(yellow)
  print(red)

  fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
  (green, yellow, *red) = fruits
  
  fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
  (green, *tropic, red) = fruits
  ```
