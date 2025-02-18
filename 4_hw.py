class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Создаем 3 объекта

rect1 = Rectangle(7, 8)
rect2 = Rectangle(2, 5)
rect3 = Rectangle(3, 8)


# Выводим площадь и периметр для каждого объекта

print(f"Rectangle 1: Area = {rect1.area()}, Perimeter = {rect1.perimeter()}")
print(f"Rectangle 2: Area = {rect2.area()}, Perimeter = {rect2.perimeter()}")
print(f"Rectangle 3: Area = {rect3.area()}, Perimeter = {rect3.perimeter()}")



class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        result = self.a + self.b
        print(f"Addition: {result}")

    def multiplication(self):
        result = self.a * self.b
        print(f"Multiplication: {result}")

    def division(self):
        if self.b != 0:
            result = self.a / self.b
            print(f"Division: {result}")
        else:
            print("Error: Division by zero")

    def subtraction(self):
        result = self.a - self.b
        print(f"Subtraction: {result}")

math = Math(10, 5)

math.addition()
math.multiplication()
math.division()
math.subtraction()

class SidebarButton:
    def __init__(self, text):
        self.text = text
        self.type = "Кнопка"
        self.locator = ""

    def click(self):
        return f"Клик по кнопке {self.text}"

# Создаем объекты для каждой кнопки
text_box_button = SidebarButton("Текстовое поле")
check_box_button = SidebarButton("Установите флажок")
radio_button_button = SidebarButton("Кнопка переключения")
web_tables_button = SidebarButton("Веб-таблицы")
buttons_button = SidebarButton("Кнопки")
links_button = SidebarButton("Ссылки")
broken_links_images_button = SidebarButton("Неработающие ссылки - изображения")
upload_and_download_button = SidebarButton("Загружать и скачивать")
dynamic_properties_button = SidebarButton("Динамические свойства")

# Список всех кнопок
buttons = [
    text_box_button,
    check_box_button,
    radio_button_button,
    web_tables_button,
    buttons_button,
    links_button,
    broken_links_images_button,
    upload_and_download_button,
    dynamic_properties_button
]
# Выводим текст каждой кнопки
print("Тексты кнопок:")
for button in buttons:
    print(button.text)

# Вызываем метод "Клик" для каждой кнопки
print("\nКлики по кнопкам:")
for button in buttons:
    print(button.click())

