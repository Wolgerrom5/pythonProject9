for i in range(100, 1000):
    if i % 17 == 0:
        print(i, end=' ')

print('\nВсего:', len([i for i in range(100, 1000) if i % 17 == 0]))
