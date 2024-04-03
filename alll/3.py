import math

while True:
    num = int(input("Введите число: "))

    if math.isqrt(num) ** 2 == num:
        print("Число является полным квадратом")
        break
    else:
        print("Число не является полным квадратом. Введите другое число.")
