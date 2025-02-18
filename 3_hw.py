def max_number(a, b):
    if a > b:
        print(f"Наибольшее число: {a}")
    else:
        print(f"Наибольшее число: {b}")

max_number(1, 2)

def check_difference(a, b):
    difference = abs(a - b)

    if difference == 135:
        print("Yes")
    else:
        print("No")

check_difference(100, 235)
check_difference(50, 200)


def get_season(month):
    if month in [12, 1, 2]:
        season = 'Зима'
    elif month in [3, 4, 5]:
        season = 'Весна'
    elif month in [6, 7, 8]:
        season = 'Лето'
    elif month in [9, 10, 11]:
        season = 'Осень'
    print(season)

get_season(1)
get_season(3)
get_season(6)
get_season(10)


def check_numbers(a, b, c):
    if a > 10 and b > 10 and c > 10:
        print("Yes")
    else:
        print("No")

check_numbers(15, 20, 30)
check_numbers(5, 15, 25)

