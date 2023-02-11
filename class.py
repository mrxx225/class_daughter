class Math:
    a: int
    b: int

    def __init__(self, a, b):
        self.a, self.b = a, b

    def addition(self, a, b):
        return a + b

    def multiplication(self, a, b):
        return a *b

    def division(self, a, b ):
        try:
            return a / b
        except ZeroDivisionError:
            pass

    def subtraction(self, a , b):
        return a - b

    def proceed(self, a, b, operation):
        match operation:
            case 1: return self.multiplication(a, b)
            case 2: return self.division(a, b)
            case 3: return self.addition(a , b)
            case 4: return self.subtraction(a,b)
            case _: return "Операция не определена"

# a = int(input("Введите а: "))
# b = int(input("Введите в: "))
c = Math(0,0)

operation = int(input("Введите желаемое действие:\n1. Умножение\n2. деление\n3. Сложение\n4. Вычитание\n" ))
a = int(input("Введите а: "))
b = int(input("Введите в: "))
print(c.proceed(a, b, operation))

# print(c.addition(a, b))
# print(c.subtraction(a,b))
# print(c.division(a,b))
# print(c.multiplication(a,b))