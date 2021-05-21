import numpy as np


# Shape -> rows, columns
# Size -> Total elements in array
# ndim -> number of dimnesions
# nbytes-> no. of bytes used to save data
# dtype -> data type of array

def code_1():
    arr1=np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
    print(arr1)
    print(arr1.size)
    print(arr1.shape)
    print(arr1.ndim)
    print(arr1.nbytes)
    print(arr1.dtype)









if __name__ == '__main__':
    code_1()
