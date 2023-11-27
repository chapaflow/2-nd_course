import numpy as np
from scipy import linalg, stats

def print_mat(m):
    for i in m:
        for z in i:
            print(f'{round(z,2)}\t',end=' ')
        print()
def print_list(m):
    a=''
    for i in m:
        a=a+str(i)+" "
    print(a)

def task1():
    print("Первое задание:")
    mat = np.array([[2., 0., -1., 25.],
                     [-6., 28., -7.4, 0.], 
                     [1., -5., 13., 2.8], 
                     [0., 4., 3., 1.7]])
    return mat
mat = task1()
print_mat(mat)

def task2(mat):
    print("Второе задание: ")
    L, U, P = linalg.lu(mat)
    print("L: ")
    print_mat(L)
    print("U: ")
    print_mat(U)
    print("P: ")
    print_mat(P)
    return L, U, P
L, U, P = task2(mat)

def task3():
    print("Третье задание: ")
    print("Определтиль L: ")
    print(L.diagonal().prod())
    print("Определитель U: ")
    print(U.diagonal().prod())
    print("Определитель P: ")
    print(np.linalg.det(np.linalg.inv(P)))
task3()

def task4():
    print("Четвёртое задание: ")
    print("Первая выборка: ")
    selection1 = stats.uniform.rvs(size=100)
    print_list(selection1)
    print("Вторая выборка: ")
    selection2 = stats.norm.rvs(size=100)
    print_list(selection2)
    return selection1, selection2
selection1, selection2 = task4()

def task5(selection1, selection2):
    print("Пятое задание: ")
    print("Среднее: ")
    print(np.mean(selection1))
    print(np.mean(selection2))
    print("Мода: ")
    print(stats.mode(selection1, keepdims=True))
    print(stats.mode(selection2, keepdims=True))
    print("Медиана: ")
    print(np.median(selection1))
    print(np.median(selection2))
    print("Минимальное: ")
    print(min(selection1))
    print(min(selection2))
    print("Максимальное: ")
    print(max(selection1))
    print(max(selection2))
    print("Стандартное отклонение: ")
    print(np.std(selection1))
    print(np.std(selection2))
task5(selection1, selection2)

def task6(selection1, selection2):
    print("Шестое задание: ")
    print(stats.chisquare(selection1))
    print(stats.chisquare(selection2))
task6(selection1, selection2)
