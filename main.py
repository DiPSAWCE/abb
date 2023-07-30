"""
Name: Banele
Surname: Mjayezi
Date: 26/07/2023
Subject: BPCP
"""
import math
# Declare input variables

x = 0
y = 0

# Prompt user
direction: str = input("Enter Direction.(UP = U, Down = D, Left = L, Right = R. ")
Number_Steps: int = int(input("Enter Number of steps? "))




if direction == 'U':
    y1 = y + Number_Steps

if direction == "D":
    y2 = y - Number_Steps

if direction == "L":
    x2 = x - Number_Steps

if direction == "R":
    x1 = x + Number_Steps

else:
    print("Please enter correct direction! ")

# output
y_Total = y2 + y1
x_Total = x2 + x1

Distance: float = math.sqrt((x2 - x1) ^ 2 + (y2 - y1) ^ 2)

print(x_Total, y_Total, Distance)




