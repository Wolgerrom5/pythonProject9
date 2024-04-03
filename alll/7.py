number = int(input("Введите число: "))

power = 5
result = 2 ** power

while result < number:
    power += 1
    result *= 2

if number == result:
      print("Верно")
else:
       print("Неверно")
