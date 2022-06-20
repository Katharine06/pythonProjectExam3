# Напишите функцию, которая проверяет: является ли слово палиндромом
def palindrom(a):
    if a[::-1] == a[::1]:
        return True
    else:
        return False
print(palindrom(input('Введите слово: ')))