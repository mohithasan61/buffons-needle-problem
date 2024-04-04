import random
from math import sin
import time

# Constants
L, G = 1, 2 # Length of the needle and spacing between the lines
PI = 3.14159265358979323846264338

print(f"\n{"-"*15}\nWelcome...\nTo continute, input any natural number and press enter.\nTo break the loop, enter 0.\n{"-"*15}\n")

# Main loop for running experiments
while True:
    power = (int(input("Number of experiments = 10^"))) # Prompt user for the power of 10 to determine the number of experiments
    times = 10**power
    if (times == 1): break # Exit loop if input is 0
    start = time.time() # Start timing the experiments
    hits = 0

    # Dictionary to store experiment data
    list = {
        "Times": times,
        "Attempt": [],
        "Hits": [],
        "Value": [],
        "Average": 0,
        "Required": "",
    }

    # Run 5 consecutive experiments
    for q in range(0, 5):
        hits = 0

        # Simulate needle drops and count hits
        for i in range(0, times):
            # Generate random coordinates and angle for needle drop
            x = random.randint(0, (50*(10**4)+1))/(10**4)
            y = random.randint(0, (50*(10**4)+1))/(10**4)
            t = random.randint(0, (int(((PI/2)*(10**10)))+1))/(10**10)

            # Calculate distance of needle from nearest line
            d = (y - int(y/G)*G)
            if (d>(G/2)): d = (G - d)

            # Check if needle intersects with line
            k = (1/2)*sin(t)
            if (d <= k): hits += 1

        # Estimate value of π based on experiment results
        value = (2*times*L) / (hits*G)
        list["Hits"].append(hits)
        list["Value"].append(value)
        list["Attempt"].append(q+1)

    # Calculate average value
    average = (list["Value"][0] + list["Value"][1] + list["Value"][2] + list["Value"][3] + list["Value"][4])/5
    list["Average"] = average
    end = time.time() # End timing and calculate execution time
    required = end - start
    list["Required"] = f"{required}s"

    # Print experiment data
    print(list, "\n")
