import scipy
import math 
import scipy.misc
import sympy as smp
from scipy.optimize import minimize

def f(x):
    return math.tan(x) / math.sin(x)

def task1():
    print("Первое задание.")
    print(scipy.misc.derivative(f, 0.5, n=1))
    print(scipy.misc.derivative(f, 0.5, n=2))

def task2():
    print()
    print("Второе задание.")
    x = smp.Symbol('x')
    f = smp.tan(x) / smp.sin(x)
    print(f.diff(x))

def task3():
    print()
    print("Третье задание.")
    integral = scipy.integrate.quad(f, 0.0, 1.0)
    print(integral)    

def task4():
    print()
    print("Четвёртое задание.")
    x = smp.Symbol('x')
    f = smp.tan(x) / smp.sin(x)
    print(f.integrate(x))

# Определяем функцию цели
def objective(x):
    return (x[0] - 4) + (x[1] - 3)**2 + (x[2] - 2)**3 + (x[3]-1)**4

# Определяем функцию ограничения
def constraint(x):
    return x[0] + 2*x[1] + 3*x[2] + 4*x[3]

def task5():
    print()
    print("Пятое задание.")
    # Начальное приближение
    x0 = [1, 1, 1, 1]

    # Определяем ограничение (>= 0)
    constraint_obj = {'type': 'ineq', 'fun': constraint}

    # Решаем задачу оптимизации
    result = minimize(objective, x0, constraints=constraint_obj)

    # Выводим оптимальное значение и решение
    optimal_value = -result.fun
    optimal_solution = result.x
    print("Оптимальное значение:", optimal_value)
    print("Оптимальное решение:", optimal_solution)


task1()
task2()
task3()
task4()
task5()