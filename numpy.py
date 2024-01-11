# -*- coding: utf-8 -*-

'''
Create a NumPy ndarray Object
NumPy is used to work with arrays. The array object in NumPy is called ndarray.

We can create a NumPy ndarray object by using the array() function.
'''

import numpy as np

#making an array 1D, we can also set dtype
a=np.array([1,2,3],dtype='int16')
#simple list
a1=[1,2,3]
#2D
b=np.array([[1,2,7,8,9,3],[2,99,44,5,6,7]])
#simple 2D list
b1=[[1,2,3],[5,6,7]]
#getting dimension,size,shape of array
a.ndim
b.shape
a.dtype
#single element size
a.itemesize
#no of elements
a.size
#total memory size of all whole array
a.nbytes
#to access an element
b[1,2]
#access whole row
b[0,:]
b[:,0]
#giving it step b[startindex:endindex:stepsize]
b[0,0:3:2]
#to change one element
a[1]=9
b[1,2]=999
b[:,3]=101
#3D
c=np.array([[[1,2,3],[4,9,8]],[[9,8,9],[3,4,3]]])
# accessing elements and changing
c[0,1,1]
c[:,0,:]=[[2,3,2],[5,7,8]]
#creating arrays
np.zeros((2,4))
np.zeros((2,2,3,5))
np.ones((4,2,4),dtype='int32')
np.full((2,3,4),99)
#to make like another array
np.full_like(c,66)
#making an array from random numbers
np.random.rand(4,2,3)
np.random.randint(7,size=(4,3))
#identity matrix,identity is made of zero and one
np.identity(5)
print(c)

#loading txt data into an array
filedata=np.genfromtxt('ForexML/GBPUSD1d.txt',delimiter=',')
#giving column names
filedata=np.genfromtxt('ForexML/GBPUSD1d.txt',delimiter=',',names='date,bid,ask')

#changing its type
filedata=filedata.astype('int32')
print(filedata[filedata>1])

#iterative way of adding
x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = []

for i, j in zip(x, y):
  z.append(i + j)
print(z)

#the above can be easy with numpy add method

z=np.add(x,y)

print(np.__version__)
print(np.show_config())

#getting help on the funciton
print(np.info(np.add))



















