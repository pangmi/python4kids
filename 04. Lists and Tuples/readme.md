## Lists
  - Lists hold a collection or ordered sequence of data
  - Lists can be modified to have values added or removed
  - Each value in a list is called an item or element
  - Lists are mutable (changeable)
  - List can be joined to form a new list

  ##### Declare a List
  ```python
  my_numbers = [1, 2, 3, 4, 5, 6]
  my_colors = ["red", "blue", "green"]
  my_list = [1, "Two", 3.12, True]
  print(my_numbers)
  ```

  ##### Access Items in a List
  ```python
  print(my_colors[0])
  print(my_colors[1])
  ```

  ##### Change Values of Items in a List
  ```python
  fruits = ["apple", "banana", "grapes"]
  fruits[1] = "strawberry"
  print(fruits)               # would print ['apple', 'strawberry', 'grapes']
  ```

  ##### Get Number of Items in a List
  ```python
  colors = ["red", "blue", "green", "purple", "orange"]
  even_numbers = [2, 4, 6]
  print(len(colors))
  print(len(even_numbers))
  ```

  ##### Add Items to a List
  ```python
  colors = ["white", "yellow"]
  colors.append("red")
  colors.append("blue")
  colors.append("green")
  print(colors)               # would print ['white', 'yellow', 'red', 'blue', 'green']
  ```

  ##### Join Lists
  ```python
  sedans = ["Toyota Camry", "Honda Accord", "Nissan Sentra"]
  trucks = ["Toyota Tundra", "Ford F-150", "Chevy Silverado"]
  vehicles = sedans + trucks
  print(vehicles)
  ```

  ##### Multiply Lists
  ```python
  colors = ["red", "blue", "green"]
  many_colors = colors*2
  print(many_colors)
  ```

  ##### Remove Items from List by Value
  ```python
  favorite_foods = ["hamburger", "ice cream", "coconut", "apple"]
  favorite_foods.remove("coconut")
  ```
  
  ##### Remove Items from List by Index
  ```python
  planets = ["sun", "mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune", "pluto"]
  del planets[0]
  del planets[8]
  print(planets)
  ```

  ##### Counting Items in a List
  ```python
  names = ["Noe", "Jame", "Sally", "Noe", "Sally", "Noe"]
  noe_count = names.count("Noe")
  james_count = names.count("James")
  print(f"Noe appears {noe_count} times")
  print(f"James appears {james_count} times")
  ```  
  
## Tuples
  - Tuples hold a collection or order sequence of values
  - Tuples cannot be modified to have data added or removed
  - Each value in a tuple is called an item or element
  - Tuples are immutable (Can't change)
  - Tuples can be joined to form new tuples
  - `Tuple` is similar to `List` except
    - We declare tuple with parenthesis
    - Tuples cannot be modified after they are created. Lists can be changed
    - Tuples use less memory
  
  ```python
  fruits = ('apple', 'orange', 'banana', 'grapes')
  print(fruits)
  print(fruits[1])

  vegetables = ('carrot', 'lettuce', 'onions')
  foods = fruits + vegetables
  print(foods)

  fruits2 = fruits * 2
  print(fruits2)

  print(len(fruits2))
  print(fruits2.count('apple'))
  ```

#### Homework
First of all, for each of the programs you create, please write a comment line which includes your name and current date at the top of your program like below:
```python
# Felix Zuo - 2022-11-27
```

1. Go over the following sections in [Python Cheat Sheet](https://github.com/pangmi/python4kids/blob/main/00.Cheat%20Sheet/readme.md)
   - [List](https://github.com/pangmi/python4kids/tree/main/00.Cheat%20Sheet/list/readme.md)
   - [Tuples](https://github.com/pangmi/python4kids/blob/main/00.Cheat%20Sheet/tuple/readme.md)

1. Write a program which will
   - create a string list with variable name `hero_characters`. The list should contain at least 3 of your favorite hero names. Create the list and all the names in it in one line of code.
   - create another list named `villain_characters`. Create this list as an empty list, and then add the names of at least 3 villain characters to it in separate lines of code.
   - create a 3rd list named `all_characters` that contains `hero_characters` and `villain_characters` joined together
   - print the second item in your `hero_characters` list 
   - print the last item in your `villain_characters` list
   - finally, print `hero_characters`, `villain_characters`, and `all_characters`

1. Write a program which will
   - create a tuple with variable name `hero_characters`. The tuple should contain at least 3 of your favorite hero names.
   - create another tuple named `villain_characters`. This tuple should contain at least 3 villain names.
   - create a 3rd tuple named `all_characters` that contains `hero_characters` and `villain_characters` joined together
   - print the second item in your `hero_characters` tuple 
   - print the last item in your `villain_characters` tuple
   - finally, print `hero_characters`, `villain_characters`, and `all_characters`

1. **Temperature Conversion Celsius to Fahrenheit**

   Create a function `temp_conversion_c2f(c)` that takes a temperature input in Celsius and converts it to Fahrenheit.
   
   ***Examples***
   ```python
   temp_conversion_c2f(0)       # 32.0
   temp_conversion_c2f(20)      # 68.0
   temp_conversion_c2f(30)      # 86.0
   temp_conversion_c2f(40)      # 104.0
   temp_conversion_c2f(43.3)    # 109.9
   temp_conversion_c2f(100)     # 212.0
   ```
   - The formula to calculate the temperature in Fahrenheit from Celsius is: `F = C*9/5 +32`
   - You need to round up calculated temperatures up to 1 decimal place.

1. **Temperature Conversion Fahrenheit to Celsius**

   Create a function `temp_conversion_f2c(c)` that takes a temperature input in Fahrenheit and converts it to Celsius.
   
   ***Examples***
   ```python
   temp_conversion_f2c(32)      # 0.0
   temp_conversion_f2c(212)     # 100.0
   temp_conversion_f2c(68)      # 20.0
   temp_conversion_f2c(90)      # 32.2
   temp_conversion_f2c(110)     # 43.3
   ```
   - The formula to calculate the temperature in Celsius from Fahrenheit is: `C = (F-32)*5/9`
   - You need to round up calculated temperatures up to 1 decimal place.

1. **Basic Calculator**

   Create a function `calculator(a, operator, b)` that takes two numbers and a mathematical operator `+ - / *` and will perform a calculation with the given numbers.
   
   ***Examples***
   ```python
   calculator(2, "+", 2)        # 4
   calculator(65, "*", 3)       # 195
   calculator(10, '-', 7)       # 3
   calculator(2, '*', 16)       # 32
   calculator(2, '-', 2)        # 0
   calculator(15, '+', 26)      # 41
   calculator(96, '/', 6)       # 16   
   ```

1. **Factorial**

   Create a function `factorial(n)` that takes an integer and returns the factorial of that integer.
   
   ***Examples***
   ```python
   factorial(3)     # 6
   factorial(5)     # 120
   factorial(13)    # 6227020800
   ```

