import numpy as np

my_list1 = [1,2,3,4]
my_array1 = np.array(my_list1)

print(my_array1)

my_list2 = [11,12,13,44]
my_lists = [my_list1, my_list2]
my_array2 = np.array(my_lists)

print(my_array2)
print(my_array2.shape)

z_array = np.zeros(5)
print(z_array.dtype)   #float
np.ones([5,5])

print(np.eye(5))  # identity matrix

print(np.arange(5, 50, 2))

print (5/2)

arr1 = np.array([[1,2,3,4],[8,9,10,11]])

print (arr1)
print(arr1 * arr1)
print( arr1 - arr1)
print ( 1 / arr1)
print ( arr1 ** 3)

arr9 = np.arange(0,11)
print(arr9[8])
print(arr9[1:5])
arr9[0:4] = 100
print(arr9)
arr9 = np.arange(0,11)
slice_of_arr = arr9[0:6]
slice_of_arr[:] = 99
print(arr9)    # array [] doesn't get copies
arr_copy = arr9.copy()
arr_copy[1] =1
print(arr9, arr_copy)

arr_2d = np.array([[1,2,3], [20, 25, 30], [6,12,18]])
print(arr_2d[1])
print(arr_2d[1][2])
print(arr_2d[0:,1:2])
print(arr_2d[:2,1:])     # rows: everything up to 2 (excluding 2), 
                         # cols: 1 and everything after

arr2d = np.zeros((10,10))
print (arr2d.shape[1])
arr_length = arr2d.shape[1]
for i in range(arr_length):
    arr2d[i]=i
print(arr2d[[2,4,6,8]])    # fancy indexing, no order to the indexes
print ('------------------------')
print (arr2d)
print ('------------------------')
print (arr2d.T)
print ('------------------------')
print(np.dot(arr2d.T, arr2d))   # dot product
print ('------------------------')

arr3d = np.arange(50).reshape((5,5,2))
print(arr3d, arr3d.transpose(1,0,2))
print ('------------------------')
print (arr2d.swapaxes(0,1))
arr = np.array([[1,2,3]])
print(arr)
print(arr.swapaxes(0,1))

# universal functions
arr = np.arange(11)
print (np.sqrt(arr))
print (np.exp(arr))
print ('------------------------')
A = np.random.randn(10)
B = np.random.randn(10)
print(np.add(A,B) )
print(np.maximum(A,B))