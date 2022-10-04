#!C:/Users/LENOVO/AppData/Local/Programs/Python/Python39/python.exe
""" 2-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(3, 5, 1)
    r1_dictionary = r1.to_dictionary()
    print(r1_dictionary.get('oo'))
    r2 = Rectangle.create(**r1_dictionary)
    print(r1)
    print(r2)
    print(r1 is r2)
    print(r1 == r2)
