N = int(input("Введите значение N: "))

total_volume = 0
side_length = 1

while total_volume + side_length ** 3 <= N:
    total_volume += side_length ** 3
    print(side_length ** 3, end=" ")
    side_length += 1
