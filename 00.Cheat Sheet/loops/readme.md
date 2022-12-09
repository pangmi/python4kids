## LOOPS
  #### `while` Loop
  This is a loop that will keep repeating itself until the while condition becomes false.
  ```python
  n = 1
  while n < 100:
      n += 1
  ```

  #### `for` Loop
  For loops give you more control than while loops. You can loop through anything that is iterable. e.g. a range, a list, a dictionary or tuple.
  ```python
  all_fruits = ["apple", "banana", "orange"]
  for fruit in all_fruits:
      print(fruit)
  ```

  #### _ in a `for` Loop
  If the value your for loop is iterating through, e.g. the number in the range, or the item in the list is not needed, you can replace it with an underscore.
  ```python
  for _ in range(100):
      # Do something 100 times.
      print("Repeating 100 times")
  ```

  #### `break`
  This keyword allows you to break free of the loop. You can use it in a `for` or `while` loop.
  ```python
  scores = [34, 67, 99, 105]
  for s in scores:
      if s > 100:
          print("Invalid")
          break
      print(s)
  ```

  #### `continue`
  This keyword allows you to skip this iteration of the loop and go to the next. The loop will still continue, but it will start from the top.
  ```python
  n = 0
  while n < 100:
      n += 1
      if n % 2 == 0:
          continue
      print(n)
      # Prints all the odd numbers
  ```

  #### Infinite Loops
  Sometimes, the condition you are checking to see if the loop should continue never becomes false. In this case, the loop will continue for eternity (or until your computer stops it). This is more common with while loops.
  ```python
  while 5 > 1:
      print("I'm a survivor")
  ```
  
