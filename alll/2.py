string = input("Введите строку: ")
output_string = ""
for i in range(2, len(string), 3):
    output_string += string[i]
print(output_string)


