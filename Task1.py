# Напишите функцию, которая будет принимать номер кредитной карты
# и показывать только последние 4 цифры. Остальные цифры должны заменяться звездочками
def card_hide(card):
    return '*' * len(card[:-4]) + card[-4:]
print(card_hide(input('Введите номер карты: ')))