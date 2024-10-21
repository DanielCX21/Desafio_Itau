import numpy as np

Z = np.array([[1,2,6],
              [3,1,2],
              [5,4,9]],dtype=float)

tol = 1

sub = Z[tol:,tol:]

print(Z)

print(sub)
