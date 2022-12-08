## LIST METHODS
  #### Adding Lists Together
  You can extend a list with another list by using the extend keyword, or the + symbol.
  ```python
  list1 = [1, 2, 3]
  list2 = [9, 8, 7]
  new_list = list1 + list2
  list1 += list2
  ```

  #### Adding an Item to a List
  If you just want to add a single item to a list, you need to use the `.append()` method.
  ```python
  all_fruits = ["apple", "banana", "orange"]
  all_fruits.append("pear")
  ```

  #### List Index
  To get hold of a particular item from a list you can use its index number. This number can also be negative, if you want to start counting from the end of the
list.
  ```python
  letters = ["apple", "banana", "orange"]
  letters[0]    # "apple"
  letters[-1]   # "orange"
  ```

  #### List Slicing
  Using the list index and the colon symbol, you can slice up a list to get only the portion you want. Start is included, but end is not.
  ```python
  # list[start:end]
  states = ['CA', 'CO', 'CT', 'DE', 'FL', 'GA']
  result = states[2:4]    # result is ['CT', 'DE']
  
  # Omit the first index and the slice starts with the first item in the list
  result = states[:2]    # result is ['CA', 'CO']
  ```

  #### Looping List
  - Use a `for` loop to loop through all items in a list
    ```python
    countries = ['CAN', 'CHL', 'IND', 'AUS']
    for country in countries:
        print(f"I'm flying to {country}.")
    ```
  
  - Loop through part of a list using a slice
    ```python
    for country in countries[:2]:
      print(f"I've been to {country}.")
    ```

  #### List Comprehension
  A list comprehension is a compact way of defining a list in one line.
  - Syntax
    ```python
    newlist = [expression for item in iterable if condition == True]
    ```
  - Example
    ```python
    fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
    newlist = [x.title() for x in fruits if x != "cherry"]

    print(newlist)
    # Result: ['Apple', 'Banana', 'Kiwi', 'Mango']    
    ```
