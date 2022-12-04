#PythonChallenge6.py - Simple Word Game
import pyttsx3

engine = pyttsx3.init()

print("Enter an adjective:")
adjective1 = input()

print("Enter a person's name:")
personName = input()

print("Enter a verb:")
verb1 = input()

print("Enter a verb:")
verb2 = input()

print("Enter a verb:")
verb3 = input()

print("Enter a verb:")
verb4 = input()

print("Enter a place name:")
placeName = input()

line1 = f"It was a {adjective1} summer day and {personName} was very"
line2 = f"hot. {personName} decided to {verb1} to the swimming pool. At"
line3 = f"the pool, the people {verb2}, {verb3}, {verb4} in the "
line4 = f"water. At the end of the day everyone left and went to the {placeName}"

fullStory = f"{line1} {line2} {line3} {line4}"

print(fullStory)
engine.say(fullStory)

engine.runAndWait()
