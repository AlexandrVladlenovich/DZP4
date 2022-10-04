import math
def pi():
    pi = math.atan(1) * 4
    accuracy = str(input("Введите точность числа π до 15-го знака после запятой (например 0.001): "))
    value = len(accuracy[2::])
    print(round(pi, value))
pi()