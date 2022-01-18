# Copyright 2022 Davydov Nikolay (NNDavydov)

import matplotlib.pyplot as plt

from extremum_search.two_criteria.genetic import *

# Начальные параметры
params = {
    'D(x)': np.arange(-1, 1, 0.01),
    'D(y)': np.arange(-1, 1, 0.01),
}


def func(x, y):
    return 1 / np.sqrt(0.01 + x ** 2 + y ** 2)


genetic = GeneticAlgorithm()
print(genetic.genetic_algorithm(func, -1, 1, -1, 1, 100))

# Построение 3d графика
X, Y = np.meshgrid(params['D(x)'], params['D(y)'])
Z = func(X, Y)

fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))
ax.plot_surface(X, Y, Z, cmap=plt.get_cmap('jet'))
plt.show()
