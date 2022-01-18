# Copyright 2022 Davydov Nikolay (NNDavydov)

import matplotlib.pyplot as plt

from extremum_search.one_criteria.annealing_simulation import *

# Начальные параметры
params = {
    'a': 2,
    'b': 6,
    't_max': 10000,
    't_min': 0.1,
    'coef': 0.95
}


def func(x):
    return 5 * np.cos(x) + x + x ** 0.5


def func2(x):
    return np.sin(5 * x) * func(x)


print(annealing_simulation_algorithm(params['a'], params['b'], params['t_max'], params['t_min'], params['coef'], func))
print(annealing_simulation_algorithm(params['a'], params['b'], params['t_max'], params['t_min'], params['coef'], func2))

# создаем график f(x)
X = np.arange(params['a'], params['b'], 0.01)
y = func(X)
plt.plot(X, y)
plt.show()

# создаем график f(x)*sin(5x)
y = func2(X)
plt.plot(X, y)
plt.show()
