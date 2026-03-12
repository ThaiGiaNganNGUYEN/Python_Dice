import random

print("Welcome to the Dice Roller\n")

while True:
    amount = int(input("Enter the amount of dice (1-10): "))
    if (amount > 0 and amount < 10):
        break
    else:
        print("Invalid Input. Try again.")
        
def roll_dice(amount):
    total_sum = 0
    faces = [1, 2, 3, 4, 5, 6]
    for dice in range(amount):
        roll = random.choice(faces)
        print("Dice: ", dice + 1, ":", roll)
        total_sum += roll
    average = total_sum / amount
    print("Total Sum: ", total_sum)
    print("AverageL ", average)
    
roll_dice(amount)
    