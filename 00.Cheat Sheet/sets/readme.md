## SET
  Sets are used to store multiple items in a single variable.
  - Set items are unordered, unchangeable, and do not allow duplicate values
  - You can remove items and add new items
  
  ```python
  # create a set
  fruits = {"apple", "banana", "cherry"}
  print(fruits)
  # {'apple', 'cherry', 'banana'}
  
  
  # duplicate values will be ignored
  fruits = {"apple", "banana", "cherry", "apple"}
  print(fruits)
  # {'apple', 'cherry', 'banana'}


  # access items in a loop
  fruits = {"apple", "banana", "cherry"}
  for x in fruits:
      print(x)
  
  # check if item exists in the set
  fruits = {"apple", "banana", "cherry"}
  x = "banana"
  if x in fruits:
      print(f"{x} is in the set")
  
  
  # add an item to a set
  fruits = {"apple", "banana", "cherry"}
  fruits.add("orange")
  
  # join two sets
  color = {"apple", "banana", "cherry"}
  tropical = {"pineapple", "mango", "papaya"}
  fruits = color.union(tropical)
  print(fruits)
  # {'apple', 'cherry', 'pineapple', 'banana', 'mango', 'papaya'}
  
  
  # remove an item in a set
  fruits = {"apple", "banana", "cherry"}
  fruits.remove("banana")
  print(fruits)
  
  ```
