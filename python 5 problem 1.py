import random
num_dice = int(input("How many dice to roll: "))
total_sum = 0

for _ in range(num_dice):

    die_roll = random.randint(1, 6)

    total_sum += die_roll
print(f"The sum of the dice rolls is: {total_sum}")