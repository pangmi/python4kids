#### Class Summary

An **expression** is a combination of values, variables, operators, and function calls to calculate a result value.\
**Operators** are symbols that tell our programs to perform a calculation on the operands.\
**Operands** are the values that are used in the calculation.

In the line below `2 + 3` is an expression. 2 and 3 are operands and the `+` is the operator telling the computer to perform addition.
```python
2 + 3
```

There can be more than one operator in an expression.
```python
2 + 3*4     # produces a result of 14
```

- Click [here](https://github.com/pangmi/python4kids/tree/main/00.Cheat%20Sheet/maths#arithmetic-operators) to learn about math operators.
- Operators are applied in a certain order. Click [here](https://github.com/pangmi/python4kids/tree/main/00.Cheat%20Sheet/maths#operator-precedence) to learn about operator precedence.
- Click [here](https://github.com/pangmi/python4kids/tree/main/00.Cheat%20Sheet/strings#string-concatenation) to learn about string operators / concatenation.

#### Homework
First of all, for each of the programs you create, please write a comment line which includes your name and current date at the top of your program like below:
```python
# Felix Zuo - 2022-11-27
```

1. Go over the following sections in [Python Cheat Sheet](https://github.com/pangmi/python4kids/blob/main/00.Cheat%20Sheet/readme.md)
   - [String](https://github.com/pangmi/python4kids/tree/main/00.Cheat%20Sheet/strings/readme.md)
   - [List](https://github.com/pangmi/python4kids/tree/main/00.Cheat%20Sheet/list/readme.md)
   - [Conditionals](https://github.com/pangmi/python4kids/tree/main/00.Cheat%20Sheet/conditionals/readme.md)
   - [Loops](https://github.com/pangmi/python4kids/tree/main/00.Cheat%20Sheet/loops/readme.md)
   - [Functions](https://github.com/pangmi/python4kids/blob/main/00.Cheat%20Sheet/functions/readme.md)
1. Write a program to calculate area of rectangle. You will need to ask the user to enter the width and height, and then print out the area like below.
   ```python
   Area = 24
   ```
1. Write a program to calculate area of triangle. You will need to ask the user to enter the base length and height, and then print out the area like below.
   ```python
   Area = 25
   ```
1. Use either a program or Python console to determine the result or final value of the following expressions.
   ```python
   3 + 2*4 - 1
   (3 + 2)*4 - 1 
   14 / 3
   14 // 3
   14 % 3 
   4**2
   2**3**4
   245.34 + 945.55
   246.10498237 / 4323
   ```
   
   If the following code executes. What is in the variable d at the end?
   ```python
   a = 1000
   b = 50
   c = a / b + 2
   d = c * 10 % 5
   d = d + 1
   ```
1. Calculate your age in dog years. Write a program that asks for your age in human years. Store the age in a variable, calculate your age in dog years, and print out your age in dog years as below:
   ```python
   Your age in dog years = 21
   ```
   - 1 human year equals 7 dog years.
   - For example, if I am 3, then my age in dog years would be 21

1. **Sums Up** 

   Create a function 'sums(nums)` that takes an array of numbers, and returns the sum of all the numbers 
   
   ***Examples***
   ```python
   sums([1, 5, 6, 3])                  ➞  15
   sums([16, 3.5, 6])                  ➞  25.5
   sums([16, 30, 22.8, 4])             ➞  72.8
   sums([52, 22, 20, 30])              ➞  124
   sums([10, 12, 32, 4.9, 5, 6, 71])   ➞  140.9
   ```

1. **End COVID**

   Create a function `end_covid(recovers, new_cases, active_cases)` that takes the number of daily average recovered cases `recovers`, daily average `new_cases`, current `active_cases`, and returns the number of days it will take to reach zero cases.
   
   ***Examples***
   ```python
   end_covid(4000, 2000, 77000)     ➞ 39
   end_covid(3000, 2000, 50699)     ➞ 51
   end_covid(30000, 25000, 390205)  ➞ 79
   ```
   - The number of people who recover per day `recovers` will always be greater than daily `new_cases`
   - You need to round up the number of days needed



