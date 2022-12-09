## Dictionaries
  A dictionary is a set of items; each item consists of a key and a value. You define a dictionary using braces.

  ```python
  capitals = {
      'AK': 'Juneau',
      'AL': 'Montgomery',
      'AZ': 'Phoenix'
  }
  
  # Get value by the key 
  c1 = capitals['AK']         # c1: 'Juneau'
  
  # Get value with get() method
  c2 = capitals.get('AK')     # c2: 'Juneau'
  
  # Add items to an existing dictionary by placing the new key in brackets and providing the value
  capitals['AR'] = 'Little Rock'
  
  # Remove items from a dictionary using the del keyword
  del capitals['AR']
  
  # Loop keys 
  for state in capitals:
      print(f"State: {state}")
      
  # State: AK
  # State: AL
  # State: AZ
  
  # Loop values 
  for capital in capitals.values():
      print(f"Capital: {capital}")
      
  # Capital: Juneau
  # Capital: Montgomery
  # Capital: Phoenix
  
  # To work with both keys and values, use the items() method
  for state, capital in capitals.items():
      print(f"{capital}, {state}")
  
  # Juneau, AK
  # Montgomery, AL
  # Phoenix, AZ
  ```
