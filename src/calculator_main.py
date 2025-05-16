from src.operations import add
from src.operations import subtract
from src.operations import multiply
from src.operations import divide
from src.operations import power


def calculate():
    operation = input("Выберите операцию (+, -, *, /, **): ")
    try:
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        if operation == "+":
            print(add(a, b))
        elif operation == "-":
            print(subtract(a, b))
        elif operation == "*":
            print(multiply(a, b))
        elif operation == "/":
            print(divide(a, b))
        elif operation == "**":
            print(power(a, b))
        else:
            print("Неизвестная операция")
    except ValueError:
            print("Ошибка при введении числа")

while True:
    calculate()
    if input("Хотите выполнить еще одну операцию? (да\нет): ").lower() != "да":
        break
