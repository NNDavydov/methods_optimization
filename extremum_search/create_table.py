# Copyright 2022 Davydov Nikolay (NNDavydov)
import pandas as pd


def create_table_excel(name_table, data):
    '''
    Функция создания таблицы в Excel с именем name_table и параметрами data
    :param name_table: название таблицы
    :param data: словарь из название столбца и значений в его ячейках
    :return:
    '''
    pd.set_option('display.max_rows', None)
    table_values = pd.DataFrame(data=data)
    table_values.to_excel(name_table, index=False)
