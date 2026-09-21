import time
import random

fastest_time = None

for attempt in range(1, 6):
    print("Attempt", attempt)
    print("Get ready...")

    # Wait for a random amount of time between 2 and 5 seconds
    wait_time = random.uniform(2, 5)
    time.sleep(wait_time)

    # Record the time when GO appears
    print("GO!")
    start_time = time.monotonic()

    # Wait for the player to press Enter
    input()

    # Record the time when Enter is pressed
    end_time = time.monotonic()

    # Calculate reaction time
    reaction_time = end_time - start_time

    print("Your reactime time:", round(reaction_time, 3), "seconds")
    print()

    # Check if this is the fastest time
    if fastest_time is None or reaction_time < fastest_time: fastest_time = reaction_time

print("Game over!")
print("Your fastest reaction time:", round(fastest_time, 3), "seconds")