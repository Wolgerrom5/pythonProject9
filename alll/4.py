num = int(input("Введите целое число X: "))
sum_of_numbers = 0

for i in range(1, num+1):
    sum_of_numbers += i

print(f"Сумма первых {num} натуральных чисел: {sum_of_numbers}")
