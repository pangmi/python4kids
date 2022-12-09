## CLASSES & OBJECTS

#### Creating Class
A `class` represents a `type` in the real world. It encapsulates data and actions in one place. Basically a `class` conatains the following two parts:
  - Attributes (properties, data memebers)
  - Methods (functions, actions)
  ```python
  class Robot:
      def __init__(self, name, color, height, purpose):
          # Attributes
          self.name = name
          self.color = color
          self.height = height
          self.purpose = purpose

      # Methods
      def greet(self):
          print("Hello, my name is", self.name)

      def request_work(self):
          print(F"{self.name} wants to work.")
      
      def do_math(self, n1, n2, operator):
          if operator == "add":
              return n1 + n2
          elif operator == "substract":
              return n1 - n2
          elif operator == "multiply":
              return n1 * n2
          else:
              return 0          
  ```
  - `__init__` is a special method called ***constructor***. It is always called when the class is being initiated.
  - The `self` parameter is a reference to the current instance of the class, and is used to access attributes that belongs to the class.

#### Using Class 
To use class attributes and methods, you must make instances, or objects, from the class
  ```python
  # create instance 1 and call its attributes and methods
  r1 = Robot("Bot", "Red", 60, "Do homework")
  print(f"Robot {r1.name} is created.")
  r1.greet()
  r1.request_work()

  # create instance 2 and call its methods
  r2 = Robot("R2D2", "Teal", 30, "Repair and fight")
  r2.greet()
  result = r2.do_math(30, 45, "add")
  print(result)
  ```

#### Class Inheritance
When you create a new class, you can inherit the methods and properties of another class.
```python
class Animal:
    def breathe(self):
        print("breathing")

class Fish(Animal):
    def breathe(self):
        super().breathe()
        print("underwater")

nemo = Fish()
nemo.breathe()
# Result:
#   breathing
#   underwater
```

