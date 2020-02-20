## Ising Model Monte Carlo Simulation

## Evatt Salinger, Dr. Kassahun Betre, Josh Vasquez
# 1. Make Spin Array [Evatt 2/19]
# 3. Store Acceptance values
# 2. Choose temperature
# 3. Set initial state
# 4. Flip spin -> New state
# 5. Calculate Energy difference
# 6. Acceptance Test
# 7. Repeat 3-5 for some number of sweeps
# 8. Visualize end result
# 9. Store and compare endstates
# 10. Run again with seed states

# Import Statements
import numpy as np
import random as r

# Initial Conditions
array_size = 5


# Functions
def random_array():
    seed_array = np.empty([array_size,array_size])
    for i in range(array_size):
        for j in range(array_size):
            seed_array[i,j] = r.choice([-1,1])
    return seed_array


def delE():
    return


def accept():
    return


def flip_spin():
    return


def step():
    return


# Initialize
model = random_array()

# Setup

# Main
