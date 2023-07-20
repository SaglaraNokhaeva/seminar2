import math
from decimal import getcontext, Decimal
from unicodedata import decimal

getcontext().prec = 43
d = float(input('Введите диаметр окружности: '))
print('Площадь круга: ', Decimal(math.pi*(d/2**2)))
print('Длина окружности: ', Decimal(math.pi*d))
