import numpy as np

A = np.array([[11.9, 0.0, 1.8],
              [0.0, 5.3, 1.8],
              [1.0, -1.0, -1.0]])


D = np.diag(np.diag(A))  
L = np.tril(A, -1)       
U = np.triu(A, 1)        

J_gauss_seidel = np.dot(np.linalg.inv(D - L), U)

print("Matriz J (Gauss-Seidel):")
print(J_gauss_seidel)

