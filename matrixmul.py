import numpy as np

a = np.zeros((3,3))
b = np.zeros((3,3))

for i in range (3):
    for j in range(3):
        a[i][j] = int(input(f"Enter the value of a{i+1}{j+1}: "))

for i in range (3):
    for j in range(3):
        b[i][j] = int(input(f"Enter the value of b{i+1}{j+1}: "))

c = a*b 

for i in range (3):
    for j in range(3):
        print(c[i][j], end=" ")
    print()