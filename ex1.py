# Напишите программу, которая получает целое число и возвращает его двоичное,
# восьмеричное строковое представление. ✔ Функции bin и oct используйте для проверки своего
# результата, а не для решения.

n = int(input('Введите целое число: '))
baze = int(input('Введите основание системы счисления: '))
res = ''

if baze == 2:
    print(bin(n)[2:])
elif baze == 8:
    print(oct(n)[2:])
while n > 0:
    res = str(n % baze) + res
    n = n // baze
print(res)
