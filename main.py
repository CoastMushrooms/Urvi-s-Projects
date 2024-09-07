# Author: Urvi A
# Program Name: Create Your Own Store
# Description: The purpose of this project is to simulate a store experience
# Date: 01/04/22
# Version: 1.0

# random is imported for use if numbers don't match 
import random

# welcoming to store
print("Welcome to OceanMart"
# \n used to more create spaces between the lines
      "\n\nThe best place to buy water; whenever you need it!"
      "\n\nWe Ensure You Get The Best Water"
      "\n\nPlease use numbers for your response.")

# blank variables that will be used later in the program
userOrder = ""
userOrder2 = ""
price = ""

# input variable for first order with all options
order = str(input("\nFirstly choose the temperature of the water which include:\n"
                  #"" marks used to create additional lines
                  "1. Room Temperature\n"
                  "2. Warm\n"
                  "3. Cool\n"
                  "Enter your order here: "))

# input variable for second order with all options
order2 = str(input("\nSecondly choose the type of water which include:\n"
                   "1. Tap\n"
                   "2. Mineral\n"
                   "3. Spring/Glacier\n"
                   "4. Distilled\n"
                   "5. Sparkling\n"
                   "Enter your order here: "))

# if/else statements to select order
if order == "1":
    # blank variable redefined
    userOrder = "Room Temperature"
elif order == "2":
    userOrder = "Warm"
elif order == "3":
    userOrder = "Cool"
else:
    print("\nThe temperature will be randomized.")
  # importance of random import introduced
  # randint is used because only one number is needed
    order = random.randint(1, 3)
  # selections by program for order made
    if order == 1:
        userOrder = "Room Temperature"
    elif order == 2:
        userOrder = "Warm"
    elif order == 3:
        userOrder = "Cool"

# types of water are able to be selected from
if order2 == "1":
  # blank variables redefined
    userOrder2 = "Tap Water"
    price = "0.50"
elif order2 == "2":
    userOrder2 = "Mineral Water"
    price = "1.50"
elif order2 == "3":
    userOrder2 = "Spring/Glacier Water"
    price = "1.50"
elif order2 == "4":
    userOrder2 = "Distilled Water"
    price = "1.50"
elif order2 == "5":
    userOrder2 = "Sparkling Water"
    price = "1"
else:
    print("\nThe water type will be randomized.")
    order = random.randint(1, 4)
    if order == 1:
        userOrder = "Tap Water"
        price = "0.50"
    elif order == 2:
        userOrder = "Mineral Water"
        price = "1.50"
    elif order == 3:
        userOrder = "Spring/Glacier Water"
        price = "1"
    elif order == 4:
        userOrder = "Distilled Water"
        price = "1.50"
    elif order == 5:
        userOrder = "Sparkling Water"
        price = "1"

# order is printed for user to witness along with order
# + marks are used to attach different types of statements
print("\nYour order is: " + userOrder + " " + userOrder2)
print("\nThe cost of your order is $" + price)