import time
import random

fastest_time = None

for attempt in range(1, 6):
    print("attempt", attempt)
    print("get ready...set..")

 # Wait for a random amount of time between 2 and 5 seconds
    wait_time = random.uniform(2, 5)
    time.sleep(wait_time)

 # Record the time when GO appears
    print("GO!")
    start_time = time.monotonic()

 # Wait for the player to press ENTER
    input()

 # Record the time when ENTER is pressed
    end_time = time.monotonic()

 # Calculate reaction time
    reaction_time = end_time - start_time

    print("Your reaction time:", round(reaction_time, 3), "seconds")
    print()

    # Check if this is the fastest time
    if fastest_time is None or reaction_time < fastest_time: fastest_time = reaction_time

print("game over")
print("your fastest reaction time is:", round(fastest_time, 3), "seconds")

