print("Добро пожаловать, введите целые числа и произведите с ними математические действия сложения, вычитания, умножения или деления")
a=int(input("Введите первое число"))
b=int(input("Введите второе число"))

operator=input("Какую математическу операцию будем производить? +,-,* или /?")
try:
    if operator == "+":
    print(int(a)+int(b))
    elif operator == "-":
    print((int(a)-int(b)))
    elif operator == "*":
    print(int(a)*int(b))
    elif operator == "/":
    print(int(a)/int(b))
except ZeroDivisionError:
    print("Произошло деление на ноль, в тру математике - это бесконечноcть")
    else:
print("Ошибка, проверьте введенные данные")