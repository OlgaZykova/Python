# #4. Реализуйте базовый класс Car. У данного класса должны быть следующие
# атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних
# классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс
# метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    is_police = False

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        print('Машина поехала!')

    def stop(self):
        print('Машина остановилась!')

    def turn(self, direction):
        print(f'Машина поехала в направлении: {direction}')

    def show_speed(self):
        print(f'Текущая скорость автомобиля: {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Ваша текущая скорость составляет {self.speed}кмч и превышает допустимую скорость в 60кмч!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Ваша текущая скорость составляет {self.speed}кмч и превышает допустимую скорость в 40кмч!')


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name)
        self.is_police = True


my_police_car = PoliceCar(30, 'black', 'Ford')
print(f'Значение атрибута is_police, определяемое в классе Police_car: {my_police_car.is_police}')

my_sport_car = SportCar(110, 'red', 'Ferrari')
my_sport_car.go()

my_town_car = TownCar(65, 'blue', 'Smart')
my_town_car.show_speed()
my_town_car.turn('Right')

my_work_car = WorkCar(45, 'green', 'Matiz')
my_work_car.show_speed()
my_work_car.stop()
