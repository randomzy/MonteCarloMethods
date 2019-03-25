import numpy as np

#right,up,left,down
dir_probabilities = [0.2,0.5,0.1,0.2]
#adjacency list
neighbours = [[2,1,0,0], #0
              [1,1,1,0], #1
              [3,2,0,2], #2
              [3,4,2,3], #3
              [4,5,4,3], #4
              [5,5,5,4]] #5
states = 6
markovMat = np.zeros((6,6))
for i in range(states):
    for j in range(4):
        markovMat[i,neighbours[i][j]] += dir_probabilities[j]
print("Problem 1.1")
print(markovMat)

starting_state = 2
final_state = 4
time1 = 2
time2 = 3
markovMat = np.transpose(markovMat)
Pt1 = np.linalg.matrix_power(markovMat,time1)
Pt2 = np.linalg.matrix_power(markovMat,time2)
print(Pt1[final_state][starting_state])
print(Pt2[final_state][starting_state])

eigenvalues, eigenvectors = np.linalg.eig(markovMat)
for iter in range(states):
    print()
    print("eigenvalue:", eigenvalues[iter])
    print(eigenvectors[:, iter] / sum(eigenvectors[:, iter]))
