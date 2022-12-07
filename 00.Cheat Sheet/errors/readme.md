## ERRORS
  #### Syntax Error
  Syntax errors happen when your code does not make any sense to the computer. This can happen because you've misspelt something or there's too many brackets or
a missing comma.
  ``` Python
  print(12 + 4))
    File "<stdin>", line 1
      print(12 + 4))
                   ^
  SyntaxError: unmatched ')'
  ```
  
  #### Name Error
  This happens when there is a variable with a name that the computer  does not recognise. It's usually because you've misspelt the name of a variable you created earlier.\
  ***Note***: variable names are case sensitive!
  ``` Python
  my_number = 4
  my_Number + 2
  Traceback (most recent call last): File "<stdin>", line 1,
  NameError: name 'my_Number' is not defined
  ```
  
  #### Zero Division Error
  This happens when you try to divide by zero. This is something that is mathematically impossible so Python will also complain.
  ``` Python
  5 % 0
  Traceback (most recent call last): File "<stdin>", line 1,
  ZeroDivisionError: integer division or modulo by zero
  ```
