# Copyright 2022 Davydov Nikolay (NNDavydov)

import matplotlib.pyplot as plt

from extremum_search.one_criteria.unimodal.direct import *

# Начальные параметры
params = {
    'a': -5,
    'b': 2,
    'epsilon': 0.1
}


def function(x):
    return (1 - x) ** 2 + np.exp(x)


print(passive_search(params['a'], params['b'], params['epsilon'], function))
print(method_fibonacci(params['a'], params['b'], params['epsilon'], function))
print(golden_ratio(params['a'], params['b'], params['epsilon'], function))

# График функции func(x)
X = np.arange(params['a'], params['b'], 0.01)
y = function(X)
plt.plot(X, y)
plt.show()
