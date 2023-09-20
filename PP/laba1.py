import numpy as np

def task1():
    my_array = np.arange(10, 70, 2)
    print(my_array)
    return my_array

def task2(my_array):
    A = my_array.reshape(6, 5)
    A = A.T
    print(A)
    return A

print("Первое задание:")
my_array = task1()
print("Второе задание:")
A = task2(my_array)
