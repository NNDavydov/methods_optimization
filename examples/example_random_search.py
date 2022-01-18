# Copyright 2022 Davydov Nikolay (NNDavydov)

import matplotlib.pyplot as plt

from extremum_search.one_criteria.random import *

# Начальные параметры
params = {
    'a': -3.5,
    'b': 3.5,
    'p': 0.99,
    'q': 0.005
}


# унимодальная функция
def func(x):
    return (1 - x) ** 2 + np.exp(x)


# мультимодальная функция
def func2(x):
    return func(x) * np.sin(5 * x)


print(random_search(func, params['a'], params['b'], params['p'], params['q']))
print(random_search(func2, params['a'], params['b'], params['p'], params['q']))

# создаем график f(x)
X = np.arange(params['a'], params['b'], 0.01)
y = func(X)
plt.plot(X, y)
plt.show()

# создаем график f(x)*sin(5x)
y = func2(X)
plt.plot(X, y)
plt.show()
