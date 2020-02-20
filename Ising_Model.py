## Ising Model Monte Carlo Simulation

## Evatt Salinger, Dr. Kassahun Betre, Josh Vasquez
# 1. Make Spin Array [Evatt 2/19/20]
# 3. Store Acceptance values (skipped for now)
# 2. Choose temperature (just beta? [Evatt 2/19/20])
# 3. Set initial state
# 4. Flip spin -> New array [Evatt 2/19/20]
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
z = 4                   # lattice coordination number (is this ever not 4?)
beta = 10
J = 1

# Functions
def random_array():
    ## Creates an array with random spins
    seed_array = np.empty([array_size,array_size])
    for i in range(array_size):
        for j in range(array_size):
            seed_array[i,j] = r.choice([-1,1])
    return seed_array


def A_values():
    return


def flip_spin(model_):
    ## Returns an array with one flipped node
    if model_[flip_i,flip_j] == 1:
        model_[flip_i,flip_j] = -1
    else:
        model_[flip_i,flip_j] = 1
    return model_


def delE():
    ## Calculates the difference between the current state and the next state
    # Periodic Boundries: determines the nearest neighbors, wrapping around to the other side if i or j is an edge
    if flip_i == 0:
        nn_i = [array_size - 1,1]
    elif flip_i == array_size - 1:
        nn_i = [flip_i - 1,0]
    else:
        nn_i = [flip_i - 1, flip_i + 1]

    if flip_j == 0:
        nn_j = [array_size - 1,1]
    elif flip_j == array_size - 1:
        nn_j = [flip_j - 1,0]
    else:
        nn_j = [flip_j - 1, flip_j + 1]

    # sums the 4 nearest neighbors above, below, left, and right (need to test that these are good numbers)
    diff = 0
    for n_i in nn_i:
        diff += model[n_i, flip_j]
    for n_j in nn_j:
        diff += model[flip_i, n_j]
    diff = diff * 2 * J * model[flip_i, flip_j]
    return diff

def accept():
    return


def step():
    return


# Initialize
model = random_array()

# Setup

# Testing delE function
for test in range(20):
    flip_i = r.randint(0, array_size - 1)
    flip_j = r.randint(0, array_size - 1)
    print('Flipping (' + str(flip_i) + ',' + str(flip_j) + ')')
    print(delE())

# only have to actually flip if accepted
flipped = flip_spin(np.copy(model))  # This np.copy is very important. Otherwise the original model is changed as well

# Main

