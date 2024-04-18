import datetime
import json
import functools

from datetime import date
import calendar
import re

import re
import functools

from math import pi

from itertools import cycle


class Todo:
    def __init__(self):
        self.things = []

    def add(self, *args):
        """ метод, принимающий название дела и его приоритет (целое число) и добавляющий данное дело в список дел в виде кортежа:
(<название дела>, <приоритет>)"""
        self.things.append(args)

    def get_by_priority(self, n):
        """ метод, принимающий в качестве аргумента целое число n и возвращающий список названий дел, имеющих приоритет n"""
        return [i[0] for i in self.things if n == i[1]]

    def get_low_priority(self):
        """метод, возвращающий список названий дел, имеющих самый низкий приоритет """
        if self.things:
            low = min(self.things, key=lambda x: x[1])[1]
            return [i[0] for i in self.things if i[1] == low]
        else:
            return []

    def get_high_priority(self):
        """ метод, возвращающий список названий дел, имеющих самый высокий приоритет """
        if self.things:
            hight = max(self.things, key=lambda x: x[1])[1]
            return [i[0] for i in self.things if i[1]==hight]
        else:
            return []


todo = Todo()

todos = [
    'Выбрать хостинг для своего сайта',
    'Записаться к стоматологу',
    'Записаться на курсы английского',
    'Навести порядок на кухне',
    'Подготовить одежду к лету',
    'Подготовиться к выступлению в понедельник',
    'Помыть машину',
    'Пропылесосить ковры',
    'Свозить Кемаля к ветеринару',
    'Сходить в парикмахерскую',
    'Посетить выставку камней'
]

priorities = [4, 1, 2, 5, 2, 5, 5, 3, 3, 3, 4]
for t, p in zip(todos, priorities):
    todo.add(t, p)

print(todo.get_by_priority(3))
print(todo.get_low_priority())
print(todo.get_high_priority())