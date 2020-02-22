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
# 8. Visualize end result [Betre 2/21/20]
# 9. Store and compare endstates
# 10. Run again with seed states

# Next Steps: Add magnetization evaluation, plot for every step to quantify equilibration

# Import Statements
import numpy as np
import random as r
import matplotlib.pyplot as plt

# Initial Conditions
array_size = 30
z = 4                   # lattice coordination number (is this ever not 4?)
beta = 4                # not sure what value this should take (10 makes the exponential way to small
J = 1
N_sweeps = 20
model = np.empty([array_size,array_size]) #lattice that stores spin values


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
    A_values = np.empty([2]) # just need z/2 = 2 values
    for i in range(2):
        A_values[i] = np.exp(-beta*2*J*(i+1)) #
       # see bottom of page 50
    return A_values


def flip_spin(i,j):
    ## Returns an array with one flipped node
    if model[i, j] == 1:
        model[i, j] = -1
    else:
        model[i, j] = 1

def find_Neighbor_Spins(flip_i,flip_j): #gives the 4 neighbor spins
    sL = model[flip_i,(flip_j-1)% array_size] # left
    sR = model[flip_i,(flip_j + 1) % array_size] # right
    sT = model[(flip_i + 1) % array_size,flip_j] # top
    sB = model[(flip_i - 1) % array_size,flip_j] # bottom
    return np.array([sL,sR,sT,sB])
    

def accept(delE_,sumS_):
    ind = np.absolute(int(sumS_/2))-1
#    print(' ind ', ind)
    rrand = r.random()
    if delE_ <= 0:
#        print(' Accepted: delE = ', delE_)
        return True
    elif A_dict[ind] > rrand: # i.e. rrand < e^(-beta*J*delE)
#         print('Accepted: delE = ' + str(delE_) +' A_value = ' + str(A_dict[delE_]) + ' rrand = ' + str(rrand))
        return True
    else:
        # print('Rejected: delE = ' + str(delE_) + ' A_value = ' + str(A_dict[delE_]) + ' rrand = ' + str(rrand))
        return False


def step():
    flip_i = r.randint(0, array_size - 1)
    flip_j = r.randint(0, array_size - 1)

    nbrSum = find_Neighbor_Spins(flip_i,flip_j)
#    print("i,j ",flip_i,flip_j)
#    print(" neighbor spins ",nbrSum)
    sum_S_neighbors = np.sum(nbrSum)
    delE = 2.0*J*sum_S_neighbors*model[flip_i,flip_j]
#    print("delE ",delE," sum_S_neighbors ",sum_S_neighbors)
    if accept(delE, sum_S_neighbors):
        flip_spin(flip_i,flip_j)
    
    return


# Initialize
n_steps = N_sweeps * array_size**2
#print("n_steps ",n_steps)
initial_model = np.copy(model)
model = random_array()

plt.matshow(model)

# Setup
A_dict = A_ratios()
print("exp(-beta E) values ",A_dict)

# # Testing delE function
# for test in range(20):
#     flip_i = r.randint(0, array_size - 1)
#     flip_j = r.randint(0, array_size - 1)
#     print('Flipping (' + str(flip_i) + ',' + str(flip_j) + ')')
#     print(delE())


# Main
for n in range(n_steps):
    if n%(array_size**2) == 0:
        print(' Now are sweep ',n)
    step()
    

plt.matshow(model)
plt.show()
