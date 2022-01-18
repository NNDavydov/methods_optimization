# Copyright 2022 Davydov Nikolay (NNDavydov)

import numpy as np
from sortedcontainers import SortedDict

'''
Генетический алгоритм для нахождения минимального 
значения функции от двух переменных на заданных интревалах
'''


class GeneticAlgorithm:
    def __init__(self):
        self.function = None
        self.x1 = None
        self.x2 = None
        self.y1 = None
        self.y2 = None

    def genetic_algorithm(self, function, x1, x2, y1, y2, n):
        '''
           Функция, выполняющая генетический алгоритм

           :param function: функция приспособленности
           :param x1: минимальное значение для области определения для аргумента x
           :param x2: максимальное значение для области определения для аргумента x
           :param y1: минимальное значение для области определения для аргумента y
           :param y2: максимальное значение для области определения для аргумента y
           :param n: количество итераций
           :return:
           '''
        self.function = function
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

        self.generation = SortedDict()
        for i in range(4):
            point = self._generate_xy()
            fit = self.function(point[0], point[1])
            self.generation.update({fit: point})

        for i in range(n):
            self._crossover()
            self._mutation()
            self.generation = self._selection()
            print(f'{i + 1}: {list(self.generation.items())}, fit_avg = {self._average_fit(self.generation)}')

        return list(self.generation.keys())[-1]

    @staticmethod
    def _average_fit(generation):
        '''
        Подсчет среднего значения фитнес-функции
        '''
        fits = list(generation)
        return sum(fits) / len(fits)

    def _selection(self):
        '''
        Выборка 4 лучших особей из мутировавшего поколения родителей + потомков
        :return: новое поколение
        '''
        new_generation = SortedDict()
        items = list(self.generation.items())[-4:]
        for item in items:
            new_generation.update({item[0]: item[1]})
        return new_generation

    def _crossover(self):
        '''
        Скрещевание лучших родителей generation
        В качестве потомков выбрать результат
        скрещивания лучшего решения со вторым и третьим
        в порядке убывания значений функции приспособленности
        с последующей случайной мутацией обоих генов
        '''
        points = list(self.generation.values())
        new_points = list()
        new_points.append([points[-1][0], points[-2][1]])
        new_points.append([points[-2][0], points[-1][1]])
        new_points.append([points[-1][0], points[-3][1]])
        new_points.append([points[-3][0], points[-1][1]])

        for point in new_points:
            fit = self.function(point[0], point[1])
            self.generation.update({fit: point})

    def _mutation(self):
        '''
        Функция которая вызывает мутирование у поколения generation
        Каждая точка подвержена мутации с вероятностью 25%
        '''
        for fit in self.generation:
            probability = np.random.uniform(0, 1)
            if probability < 0.25:
                new_point = self._mutation_point(self.generation[fit])
                new_fit = self.function(new_point[0], new_point[1])
                self.generation.pop(fit)
                self.generation.update({new_fit: new_point})

    @staticmethod
    def _mutation_point(point):
        '''
        Функция вызывает мутирование точки
        Случайно выбирает бит в числе который изменяется
        в данном случае выбирается от 1 до 17
        :param point: координаты точки
        :return: новые координаты
        '''
        x = int(point[0] * 100000)
        y = int(point[1] * 100000)
        mask = np.random.randint(1, 17)
        new_x = (x ^ (2 ** mask)) / 100000
        new_y = (y ^ (2 ** mask)) / 100000
        if new_x > 0:
            new_x %= 2
        else:
            new_x %= -2
        if new_y > 0:
            new_y %= 2
        else:
            new_y %= -2
        return [new_x, new_y]

    def _generate_xy(self):
        '''
        Функция генерирует точку с координатами (x, y)
        в области определения (x1, x2)(y1, y2)
        :return: список координаты x и y
        '''
        x_ = np.random.uniform(self.x1, self.x2)
        y_ = np.random.uniform(self.y1, self.y2)
        return [x_, y_]
