import random
import numpy as np

def formating(A):
    for row in A:
        print(" ".join(map(str,row)))

def task1():
    my_array = np.arange(10, 70, 2)
    print("Первое задание:")
    print(my_array)
    return my_array

def task2(my_array):
    A = my_array.reshape(6, 5)
    A = A.T
    print()
    print("Второе задание:")
    formating(A)
    return A

def task3(A):
    new_mat = (A *2.5)
    ran_line = random.randint(0, new_mat.shape[0]-1)
    new_mat[ran_line] -= 5
    print()
    print("Третье задание:")
    formating(new_mat)

def task4():
    B = np.random.uniform(0, 10, (6, 3))
    print()
    print("Четвёртое задание:")
    formating(B)
    return B

def task5(A, B):
    a = np.sum(A, axis = 1)
    b = np.sum(B, axis = 0)
    print()
    print("Пятое задание:")
    print("Размер вектора a:", a.shape)
    print("Размер вектора b:", b.shape)

def task6(A, B):
    mat_multi = np.dot(A, B)
    print()
    print("Шестое задание:")
    formating(mat_multi)

def task7(A, B):
    A = np.delete(A, 2, 1)
    B = np.hstack([B, np.random.uniform(10, 20, size=(6, 3))])
    print()
    print("Седьмое задание:")
    print("Полученная матрица A:")
    formating(A)
    print("Полученная матрица B:")
    formating(B)
    return A, B
def task8(A, B):
    det_A = np.linalg.det(A)
    det_B = np.linalg.det(B)
    print()
    print("Восьмое задание:")
    if det_A != 0:
        inv_A = np.linalg.inv(A)
        print("Обратная матрица для A:")
        formating(inv_A)
    else: 
        inv_B = np.linalg.inv(B)
        print("Обратная матрица для B:")
        formating(inv_B)


my_array = task1()
A = task2(my_array)
task3(A)
B = task4()
task5(A, B)
task6(A, B)
A, B = task7(A, B)
task8(A, B)
