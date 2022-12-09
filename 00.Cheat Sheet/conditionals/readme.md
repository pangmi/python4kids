## CONDITIONALS
  #### `if`
  This is the basic syntax to test if a condition is true. If so, the indented code will be executed, if not it will be skipped.
  ```python
  n = 5
  if n > 2:
      print("Larger than 2")
  ```

  #### `else`
  This is a way to specify some code that will be executed if a condition is false.
  ```python
  age = 18
  if age > 16:
      print("Can drive")
  else:
      print("Don't drive")
  ```

  #### `elif`
  In addition to the initial If statement condition, you can add extra conditions to test if the first condition is false.\
  Once an elif condition is true, the rest of the elif conditions are no longer checked and are skipped.
  ```python
  weather = "sunny"
  if weather == "rain":
      print("bring umbrella")
  elif weather == "sunny":
      print("bring sunglasses")
  elif weather == "snow":
      print("bring gloves")
  else:
      print("may be good for outdoor activities")
  ```

  #### `and`
  This expects both conditions either side of the `and` to be true.
  ```python
  s = 58
  if s > 50 and s < 60:
      print("Your grade is C")
  ```

  #### `or`
  This expects either of the conditions either side of the `or` to be true. Basically, both conditions cannot be false.
  ```python
  age = 12
  if age < 16 or age > 200:
      print("Can't drive")
  ```

  #### `not`
  This will flip the original result of the condition. e.g. if it was true then it's now false.
  ```python
  if not 3 > 1:
      print("something")    # Will not be printed.
  ```

  #### Comparison operators
  These mathematical comparison operators allow you to refine your conditional checks.
  ```python
  >       Greater than
  <       Lesser than
  >=      Greater than or equal to
  <=      Lesser than or equal to
  ==      Is equal to
  !=      Is not equal to
  ```
  
