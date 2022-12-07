## MATHS
  #### Arithmetic Operators
  You can do mathematical calculations with Python with the following operators.
  ```python
  3 + 2   # Add
  4 - 1   # Subtract
  2 * 3   # Multiply
  5 / 2   # Divide
  5 ** 2  # Exponent
  ```
      
  #### The += Operator
  This is a convenient way to modify a variable. It takes the existing value in a variable and adds to it. You can also use any of the other mathematical operators e.g. `-=` or `*=`
  ```python
  my_number = 6
  my_number += 2
  my_number *= 2
  my_number -= 1
  my_number /= 3
  ```
  
  #### The Modulo (`%`) Operator
  Often you'll want to know what is the remainder after a division. e.g. 4 ÷ 2 = 2 with no remainder, but 5 ÷ 2 = 2 with 1 remainder. The modulo does not give you the result of the division, just the remainder. It can be really helpful in certain situations, e.g. figuring out if a number is odd or even.
  ```python
  5 % 2
  # result is 1
  ```
  
  #### Functions
  - The `round()` function rounds a float to the given number of decimal places. Passing `round()` a negative argument results in multiples of 10
    ```python
    round(3.1415926, 2)
    # result is 3.14
    
    round(1234, -2)
    # result is 1200
    ```
  
  - The `abs()` function returns the absolute value of a number
    ```python
    abs(-5)
    # result is 5
    ```
  
  - The `bin()`, `oct()`, and `hex()` functions convert base-10 numbers to base-2, base-8, and base-16 numbers
    ```python
    bin(20)
    # result is '0b10100'
    
    oct(20)
    # result is '0o24'
    
    hex(20)
    # result is '0x14'
    ```

  #### Math Library
  The math library provides a number of functions for operations like taking square roots, using trigonometric functions, and working with mathematical constants.
  ```python
  import math
  
  math.sqrt(9)
  # result is 3.0
  
  PI = math.pi
  # PI is 3.141592653589793
  
  math.sin(PI/2)
  # result is 1.0
  
  math.log(100, 10)
  # result is 2.0
  ```
