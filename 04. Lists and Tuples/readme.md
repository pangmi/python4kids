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
