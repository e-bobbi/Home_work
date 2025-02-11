def task_1() -> None:
# Создаем пять переменных с разными типами данных
    var_int = 42          # int
    var_float = 3.14      # float
    var_str = "Привет!"   # str
    var_list = [1, 2, 3]  # list
    var_bool = True       # bool

# Выводим тип данных каждой переменной
    print(type(var_int))
    print(type(var_float))
    print(type(var_str))
    print(type(var_list))
    print(type(var_bool))

# Вызываем функцию
task_1()

def task_2() -> None:
    # Список значений
    a = [1, 2, 3, 5, 8, 13, 21]

    # Вывод первых трех элементов списка
    print(a[0:3])


# Вызов функции
task_2()

# Эта последовательность чисел называется последовательностью Фибоначчи.
# В последовательности Фибоначчи каждый следующий элемент равен сумме двух предыдущих.


def task_3(number: int) -> int:
    return number ** 2

print(task_3(5))

# Аннотации: Использованы аннотации типов для аргументов и возвращаемого значения:
#   number: int: Аргумент number имеет тип int.
#   -> int: Возвращаемое значение также имеет тип int.
