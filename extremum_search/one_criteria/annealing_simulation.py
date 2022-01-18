# Copyright 2022 Davydov Nikolay (NNDavydov)

import numpy as np

'''
Поиск экстремума функции методом имитации отжига

Включает:
 1) алгоритм поиска экстремума методом имитации отжига
'''


def annealing_simulation_algorithm(a, b, t_max, t_min, coef, function):
    '''
    Алгоритм имитации отжига для поиска минимума функции function
    на итервале [a, b], с параметрами температуры t_max и  t_min
    :param a: начало интервала функции
    :param b: конец интервала
    :param t_max: заданная максимальная температура
    :param t_min: заданная минимальная температура
    :param coef: коеффициент уменьшения температуры
    :param function: функции f(x)
    :return: минимум функции f(x)
    '''
    x_min = np.random.uniform(a, b)
    f_min = function(x_min)

    while t_max > t_min:
        x = np.random.uniform(a, b)
        f_i = function(x)
        df = f_i - f_min
        if df <= 0:
            x_min = x
            f_min = function(x_min)
        else:
            p = np.exp(-df / t_max) * 100
            if p >= np.random.uniform(0, 100):
                x_min = x
                f_min = function(x_min)

        t_max *= coef

    return x_min
