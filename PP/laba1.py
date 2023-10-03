import random
import numpy as np

def formating(A):
    for line in A:
        for elements in line:
            print(f"{elements}\t", end=' ')
    print()

def task1():
    my_array = np.arange(10, 70, 2)
    print("Первое задание.")
    for i in range (0, my_array.shape[0]):
        print(f"{my_array[i]}", end=' ')
    return my_array

def task2(my_array):
    A = my_array.reshape(6, 5)
    A = A.T
    print()
    print("Второе задание.")
    formating(A)
    return A

def task3(A):
    new_mat = (A *2.5)
    ran_line = random.randint(0, new_mat.shape[0]-1)
    new_mat[ran_line] -= 5
    print()
    print("Третье задание.")
    formating(new_mat)

def task4():
    B = np.random.uniform(0, 10, (6, 3))
    print()
    print("Четвёртое задание.")
    formating(B)
    return B

def task5(A, B):
    a = np.sum(A, axis = 1)
    b = np.sum(B, axis = 0)
    print()
    print("Пятое задание.")
    print("Размер вектора a:", a.shape)
    print("Размер вектора b:", b.shape)

def task6(A, B):
    mat_multi = np.dot(A, B)
    print()
    print("Шестое задание.")
    formating(mat_multi)

def task7(A, B):
    A = np.delete(A, 2, 1)
    B = np.hstack([B, np.random.uniform(10, 20, size=(6, 3))])
    print()
    print("Седьмое задание.")
    print("Полученная матрица A:")
    formating(A)
    print("Полученная матрица B:")
    formating(B)
    return A, B

def task8(A, B):
    det_A = np.linalg.det(A)
    det_B = np.linalg.det(B)
    print()
    print("Восьмое задание.")
    if det_A != 0:
        inv_A = np.linalg.inv(A)
        print("Обратная матрица для A:")
        formating(inv_A)
    else: 
        inv_B = np.linalg.inv(B)
        print("Обратная матрица для B:")
        formating(inv_B)

def task9(A, B):
    A = np.linalg.matrix_power(A, 6)
    B = np.linalg.matrix_power(B, 14)
    print()
    print("Девяятое задание.")
    print("Результат возведения в степень матрицы A:")
    formating(A)
    print("Результат возведения в степень матрицы B:")
    formating(B)

def task10(A, B):
    print()
    print("Десятое задание.")
    print("Решение системы линейных уравнений:")
    vals = [[2., 0., -1., 25.], [-6., 28., -7.4, 0.], [1., -5., 13., 2.8], [0., 4., 3., 1.7]]
    ans = [6.7, -4., 16., 8.]
    solving = np.linalg.solve(vals, ans)
    for i in range (0, solving.shape[0]):
        print(f"{solving[i]}", end= ' ')

my_array = task1()
A = task2(my_array)
task3(A)
B = task4()
task5(A, B)
task6(A, B)
A, B = task7(A, B)
task8(A, B)
task9(A, B)
task10(A, B)
