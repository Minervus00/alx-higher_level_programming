#!C:/Users/LENOVO/AppData/Local/Programs/Python/Python39/python.exe
Rectangle = __import__('2-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print("--")

my_rectangle.width = 10
my_rectangle.height = 0
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))
