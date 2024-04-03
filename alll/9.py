import math

N, K, R = map(int, input().split())
day = 1
current_length = N

while current_length < R:
    current_length += current_length * K / 100
    day += 1

print(day)
