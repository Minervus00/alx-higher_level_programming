#!C:/Users/LENOVO/AppData/Local/Programs/Python/Python39/python.exe
MyClass = __import__('8-class_1').MyClass
class_to_json = __import__('8-class_to_json').class_to_json

m = MyClass("John")
m.win()
print(type(m))
print(m)

mj = class_to_json(m)
print(type(mj))
print(mj)
