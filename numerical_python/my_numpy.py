import numpy as np

# creating arrays and basic attributes lesson 2
# arr105 = np.array([1,2,3,4])
# print(arr105)

# print(arr105.size, arr105.ndim, arr105.shape, arr105.dtype)

# .size means totoll number of elements in table 
# .ndim means dimensions
# .shape menas rows and columns in numbers
# .dtype means data type

# arr104 = np.array([[1,2,3,4,5],[1,2,3,4,5]])
# print(arr104.size, arr104.shape)

# arr103 = np.array([[1],[2],[3],[4]])
# print(arr103.shape)

# quick factory funcions lesson 3

# arr102 = np.ones((4,3))
# print(arr102)

# arr101 = np.arange(0, 20, 3)
# print(arr101)

# arr100 = np.linspace(0,2,10)
# print(arr100)

# np.random.seed(1) # digit
# arr99 = np.random.rand(3,5)
# print(arr99)

# indexing and slicing 1d and 2d lesson 4

# arr88 = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17])
# print(arr88[0],arr88[-1],arr88[3:11])

# arr87 = np.array([
#     [1,2,3,4,5],
#     [6,7,8,9,10],
#     [11,12,13,14,15]
# ])
# print(arr87[2,4], arr87[0], arr87[:,1])

# slicing retruns a view not a copy

# col_slic = arr87[:,1:4]
# col_slic[1,1] = 55        
# print(arr87)

# fancy indexing returns a copy not a view

# col_idx = arr87[[0,2],[2,2]]
# col_idx[1] = 66
# print(arr87)
# print(col_idx)

# arr86 = arr87[:,3] =0
# print(arr87)

# elements wise operations lesson 5

# a = np.array([1, 2, 3])
# b = np.array([10, 20, 30])
# print(a+b, a*2, b - 1)

# print(np.dot(a,b))

# c = np.array([[1, 2, 3],
#               [4, 5, 6]])

# print(c.sum())
# print(c.sum(axis=0))
# print(c.sum(axis=1))
# print(c.mean(), c.max(), c.min())


#Lesson 6 — Reshape, flatten, transpose, stacking

# a = np.arange(9)
# print(a)
# b = a.reshape(3,3)
# print(b)
# c = b.T
# print(c)
# d = b.flatten()
# print(d)

# C = np.arange(12).reshape(3, -1)  # -1 computed as 4 -> shape 3x4

# print(C)

# e = np.array([1,2,3])
# f = np.array([4,5,6])
# g = np.concatenate([e,f])
# print(g)
# h = np.vstack([e,f])
# i = np.hstack([e.reshape(3,1),f.reshape(3,1)])
# print(h)
# print(i)

#Lesson 7 — Broadcasting (rules & examples)

# x = np.array([[1,2,3,4],[5,6,7,8]])
# y = x + 10
# print(y)
# v = np.array([10, 20, 30, 40])   # shape (3,)
# print(x + v)
# col = np.array([[100], [200]])   # shape (2,1)
# print(x + col) 

# Lesson 8 — Random numbers (seed, rand, randint, normal)

# np.random.seed(42)           # reproducible randomness
# print(np.random.rand(2,3))   # uniform [0, 1)
# print(np.random.randn(3))    # standard normal (mean 0, var 1)
# print(np.random.randint(0, 10, size=(6,)))  # integers in [0,10)


# arr = np.arange(20)
# np.random.shuffle(arr)
# print(arr)

# Lesson 9 — Linear algebra basics (dot, matmul, inverse, solve, norms)

v1 = np.array([1,2,3])
v2 = np.array([4,5,6])
print(np.dot(v1, v2)) 

a = np.array([[3,1],
              [1,2]])
b = np.array([[2,0],
              [1,2]])
print(a @ b) 







#   poetry run python my_numpy.py