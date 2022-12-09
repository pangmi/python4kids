## BUILT IN FUNCTIONS
  #### `range`
  Often you will want to generate a range of numbers. You can specify the start, end and step. Start is included, but end is excluded:\
  start <= range < end
  ```python
  # range(start, end, step)
  for i in range(6, 0, -2):
      print(i)
  
  # result: 6, 4, 2
  # 0 is not included.
  ```

  #### Randomization
  The random functions come from the `random` module which needs to be imported. In this case, the start and end are both included\
  start <= randint <= end
  ```python
  import random
  
  # randint(start, end)
  n = random.randint(2, 5)
  # n can be 2, 3, 4 or 5.
  
  colors = ["red", "yellow", "blue", "green", "orange", "purple", "white", "gray"]
  pen_color = random.choice(colors)  
  ```

  #### `round`
  This does a mathematical round. So 3.1 becomes 3, 4.5 becomes 5 and 5.8 becomes 6.
  ```python
  round(4.6)
  # result 5
  ```

  #### `abs`
  This returns the absolute value.
  ```python
  abs(-4.6)
  # result 4.6
  ```
