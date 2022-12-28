# Print "You are a child" if 12 or younger
# Print "You are a teenage" if age is 13 to 17
# Print "You are an adult" if age is 18 to 64
# Print "You are a senior adult" if age is 65 or older

myAge = int(input("Enter your age: "))
if myAge <= 12:
    print("You are a child")
elif 13 <= myAge <= 17:
    print("You are a teenage")
elif 18 <= myAge <= 64:
    print("You are an adult")
else:
    print("You are a senior adult")
