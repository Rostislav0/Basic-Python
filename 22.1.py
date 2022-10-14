import numpy as np
A1 = np.array((
    [3, 4, 5, 4]
))
A2 = np.array((
    [1, 2, 3, 3]
))
print(np.dot(A1, A2))
print(A1.astype(str))
print(A1.sum())
print("mean:", A1.mean())
print(f"sin A1 {np.sin(A1)}")
print(np.arange(8, 5, -0.2))
print(np.linspace(1, 20, 20))
