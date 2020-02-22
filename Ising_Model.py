## Ising Model Monte Carlo Simulation

## Evatt Salinger, Dr. Kassahun Betre, Josh Vasquez
# 1. Make Spin Array [Evatt 2/19/20]
# 3. Store Acceptance values [Evatt 2/20/20]
# 2. Choose temperature (just beta? [Evatt 2/19/20])
# 3. Set initial state
# 4. Flip spin -> New array [Evatt 2/19/20]
# 5. Calculate Energy difference [Evatt 2/19/20]
# 6. Acceptance Test [Evatt 2/20/20]
# 7. Repeat 3-5 for some number of sweeps [Evatt 2/19/20]
# 8. Visualize end result
# 9. Store and compare endstates
# 10. Run again with seed states

# Next Steps: Add magnetization evaluation, plot for every step to quantify equilibration

# Import Statements
import numpy as np
import random as r
import matplotlib.pyplot as pp

# Initial Conditions
array_size = 5
z = 4                   # lattice coordination number (is this ever not 4?)
beta = 1                # not sure what value this should take (10 makes the exponential way to small
J = 1
n_sweeps = 10

# Functions
def random_array():
    ## Creates an array with random spins
    seed_array = np.empty([array_size,array_size])
    for i in range(array_size):
        for j in range(array_size):
            seed_array[i,j] = r.choice([-1,1])
    return seed_array


def A_ratios():
    ## Creates a dictionary of acceptance ratios for every possible delE
    A_values = {}
    max_delE_ = 2 * J * z
    delE_ = -max_delE_
    while delE_ <= max_delE_:
        if delE_ > 0:
            A_values[delE_] = np.exp(-beta * delE_)
        else:
            A_values[delE_] = 1
        delE_ += 4 * J                  # see bottom of page 50
    return A_values


def flip_spin(model_):
    ## Returns an array with one flipped node
    if model_[flip_i, flip_j] == 1:
        model_[flip_i, flip_j] = -1
    else:
        model_[flip_i, flip_j] = 1


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

def accept(delE_):
    rrand = r.random()
    if delE_ <= 0:
        # print('Accepted: delE = ' + str(delE_))
        return True
    elif A_dict[delE_] > rrand:
        # print('Accepted: delE = ' + str(delE_) +' A_value = ' + str(A_dict[delE_]) + ' rrand = ' + str(rrand))
        return True
    else:
        # print('Rejected: delE = ' + str(delE_) + ' A_value = ' + str(A_dict[delE_]) + ' rrand = ' + str(rrand))
        return False


# Initialize
N_steps = n_sweeps * array_size ** 2
model = random_array()

# Setup
A_dict = A_ratios()
initial_model = np.copy(model)
model_list = [np.copy(model)]
mag_list = [np.sum(model)]
N_list = [i for i in range(N_steps)]

# # Testing delE function
# for test in range(20):
#     flip_i = r.randint(0, array_size - 1)
#     flip_j = r.randint(0, array_size - 1)
#     print('Flipping (' + str(flip_i) + ',' + str(flip_j) + ')')
#     print(delE())


# Main
for N in N_list[1:]:
    flip_i = r.randint(0, array_size - 1)
    flip_j = r.randint(0, array_size - 1)
    if accept(delE()):
        flip_spin(model)
        mag_list.append(mag_list[N-1] + 2 * model[flip_i,flip_j])
    else:
        mag_list.append(mag_list[N-1])
    model_list.append(np.copy(model))

print(len(N_list),len(mag_list))

pp.plot(N_list, mag_list)
pp.show()