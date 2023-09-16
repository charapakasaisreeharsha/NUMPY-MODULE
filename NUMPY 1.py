import numpy as np

# functions  of numpy

# create an array from list
list1=[3,4,5,6]
array0=np.array(list1)
print(array0)

# create an array using np.zeros()

array1=np.zeros(8)
array2=np.ones(8)
print(array1)
print(array2)

# create an array with np.arange() / it is a function returns an array with values within specfic intervals

array3=np.arange(5)  # creates 0 to 4 five values
array4=np.arange(1,10,2)  # creates array of range 1-10 by step 2 means skips every two numbers

print("array3 -->",array3)
print("array4--->",array4)

# create an array with np.random.rand() / it is a function is used to create an array of a random numbers

array5=np.random.rand(7)
print(array5)

# create an Empty numpy array

array6=np.empty(4)
print(array6)   # The values stored in the array are arbitrary and have no significance.

# N-Dimensional array or N-D array for two and multiple dimensional creations
# 2D array
array7 = np.array([[1,2,3,4],
                 [2,3,4,5]])
print(array7)
# 3D array
array8=np.array([[1,2,3,4],
                 [1,2,3,4],
                 [1,3,4,5]])
print(array8)
# create  N-D array from scratch
# with N-P zeros()
array9=np.zeros((2,4))  # 2D array
array10=np.zeros((2,3,4))  # 3D array
print("2D matrix",array9)
print("3D matrix",array10)
# np.full() --> array fill with specific value
array11=np.full((6,6),6)
print(array11)
# array with np.random.rand()
array12=np.random.rand(3,3)
print(array12)

# IN numpy attributes are properties which gives information about arrays size and shape
''' ndim--> returns no of dimensions of array
size--> return n of elements in the array
dtype--> return the data type of elements in array
shape--> return the size of the array in each dimension
itemsize--> returns the size (in bytes) of each elements in the array
data--> returns the buffer containing actual elements of the array in memory'''
array13 = np.array([[1,2,3,4],
                  [2,3,4,2,]])
print(array13.ndim)
print(array13.size)
print(array13.shape)
print(array13.dtype)
# ..... you can access the function by .function you want


