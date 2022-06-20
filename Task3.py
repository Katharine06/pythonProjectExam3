# Создайте класс Tomato
#Создайте статическое свойство states, которое будет содержать все стадии созревания помидора
#Создайте метод init(), внутри которого будут определены два динамических protected свойства:
# 1) _index - передается параметром и 2) _state - принимает первое значение из словаря states
#Создайте метод grow(), который будет переводить томат на следующую стадию созревания
#Создайте метод is_ripe(), который будет проверять, что томат созрел (достиг последней стадии созревания)
class Tomato:
    states = {1:'Рост', 2:'Цветение', 3:'Зеленые плоды', 4:'Красные плоды'}
    def __init__(self, index):
        self._index = index
        self._state = 1
    def qrow(self):
        self._change_state()
    def is_ripe(self):
        if self._state == 4:
            return True
        return False
    def _change_state(self):
        if self._state < 4:
            self._state += 1
        print(f'Tomato {self._index} is {Tomato.states[self._state]}')

# Создайте класс TomatoBush
# Определите метод init(), который будет принимать в качестве параметра количество томатов и на его основе
# будет создавать список объектов класса Tomato. Данный список будет храниться внутри динамического свойства tomatoes.
# Создайте метод grow_all(), который будет переводить все объекты из списка томатов на следующий этап созревания
# Создайте метод all_are_ripe(), который будет возвращать True, если все томаты из списка стали спелыми
# Создайте метод give_away_all(), который будет чистить список томатов после сбора урожая

class TomatoBush:
    def __init__(self, number):
        self.tomatoes = [Tomato(index) for index in range(1, number)]
    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.qrow()
    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])
    def give_away_all(self):
        self.tomatoes = []

# Класс Gardener
# Создайте класс Gardener
# Создайте метод init(), внутри которого будут определены два динамических свойства:
# 1) name - передается параметром, является публичным и 2) _plant - принимает объект класса Tomato, является protected
# Создайте метод work(), который заставляет садовника работать, что позволяет растению становиться более зрелым
# Создайте метод harvest(), который проверяет, все ли плоды созрели. Если все - садовник собирает урожай.
# Если нет - метод печатает предупреждение.
# Создайте статический метод knowledge_base(), который выведет в консоль справку по садоводству.

class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant
    def work(self):
        print('Садовник работает')
        self._plant.grow_all()
        print('Садовник закончил работу')
    def harvest(self):
        print('Садовник собирает урожай')
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('Сбор урожая завершен')
        else:
            print('Растение еще не созрело')
    @staticmethod
    def knowledge_base():
        print('Справка по садовоству')

# Тесты (основной код):
# Вызовите справку по садоводству
# Создайте объекты классов TomatoBush и Gardener
# Используя объект класса Gardener, поухаживайте за кустом с помидорами
# Попробуйте собрать урожай
# Если томаты еще не дозрели, продолжайте ухаживать за ними
# Соберите урожай

if __name__ == '__main__':
    Gardener.knowledge_base()
    great_tomato_bush = TomatoBush(4)
    gardener = Gardener('Emilio', great_tomato_bush)
    gardener.work()
    gardener.work()
    gardener.harvest()
    gardener.work()
    gardener.harvest()