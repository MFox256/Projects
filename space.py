# This is a project I completed to practice boolean expressions and statements.

#Cody is an interplanetary space boxer who is trying to win championship belts for various weight categories on other planets within the solar system.
# This is a program that helps Cody keep track of their target weight.
# Here is the table of conversions.
# 1 =	Venus 	0.91
# 2 =	Mars 	0.38
# 3 =	Jupiter 	2.34
# 4 =	Saturn 	1.06
# 5 =	Uranus 	0.92
# 6 =	Neptune 	1.19

print("I have information for the following planets:\n")

print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")
 
weight = input("What is your weight?")
planet = input("What planet are you on?")

# Write an if statement below:
if planet == 1:
  weight = weight * 0.91
elif planet == 2:
  weight = weight * 0.38
elif planet == 3:
  weight = weight * 2.34
elif planet == 4: 
  weight = weight * 1.06
elif planet == 5:
  weight = weight * 0.92
elif planet == 6:
  weight = weight * 1.9   

print("Your weight:", weight)         
