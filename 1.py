def get_number(value):
    while True:
        user_input = input(value)
        try:
            number = float(user_input)
            return number
        except ValueError:
            print("Ошибка: вводить нужно числовое значение. Попробуйте еще раз.")

def action_format(action):
    if action != "+" and action != "-" and action != "*" and action != "/":
        print("Выбрано неверное действие, выберите из доступных '+', '-', '*', '/' ")
        action = input("Введите доступное действие: ")
    return action

def write_result(value):
    if value.is_integer():
        return int(value)
    elif value.__float__():
        return float(value)
    else:
        return value

def divide(num_1, num_2):
    while True:
        if num_2 != 0:
            result = num_1 / num_2
            print(f"Результат деления {write_result(num_1)} и {write_result(num_2)} равен {write_result(result)} ")
            return result
        else:
            print("Ошибка: деление на ноль невозможно. Пожалуйста, введите число, отличное от нуля.")
            num_2 = float(input("Введите второе число: "))



def calculate (num_1, num_2, action):
    if action_format(action) == "+":
        result = (num_1 + num_2)
        print(f"Результат сложения {write_result(num_1)} и {write_result(num_2)} равен {write_result(result)} ")
    elif action_format(action) == "-":
        result = (num_1 - num_2)
        print(f"Результат вычитания {write_result(num_1)} и {write_result(num_2)} равен {write_result(result)} ")
    elif action_format(action) == "*":
        result = (num_1 * num_2)
        print(f"Результат умножения {write_result(num_1)} и {write_result(num_2)} равен {write_result(result)} ")
    elif action_format(action) == "/":
        divide(num_1, num_2)







print("Добро пожаловать в калькулятор")
while True:
    num_1 = get_number("Введите первое число: ")
    num_2 = get_number("Введите второе число: ")

    action = input("Введите действие: ")
    calculate(num_1, num_2, action)
    input()
    continue