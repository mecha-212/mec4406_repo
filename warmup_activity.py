# MEC4406 Robotics and Machine Vision

# Into to Python Task

#VARIABLES
name = "Matthew Boag"
favNumber = 4

#PART 1
# Print my name
print(name)

# Count up to the square of the favorite number
for i in range(1, favNumber**2 + 1):
    print(i)

#PART 3
# Define the Engineers class
class Engineers:
    skill = "problem solver"

    def __init__(self, name, type, experience):
        self.name = name
        self.type = type
        self.experience = experience

# Create two different engineers (objects)
engineer1 = Engineers("Tobias Low", "Mechatronic", 12)
engineer2 = Engineers("Jason Brown", "Electronic and Computer System", 13)

# Print out their attributes
print(f"Engineer 1: Name: {engineer1.name}, Type: {engineer1.type}, Years of Experience: {engineer1.experience}, Skill: {Engineers.skill}")
print(f"Engineer 2: Name: {engineer2.name}, Type: {engineer2.type}, Years of Experience: {engineer2.experience}, Skill: {Engineers.skill}")

#PART 3A
# My name
print(name[::-1])