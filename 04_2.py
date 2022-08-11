# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# 6A1F2D7C1A17E -> AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE




with open('in_1.txt', 'r') as file:
    text_input = file.readline()

def decode(text: str):
    decoding = ''
    count = ''
    for char in text:
        if char.isdigit():
            count += char
        else:
            decoding += char * int(count)
            count = ''
    return decoding

print(decode(text_input))

with open('out_1.txt', 'w') as file:
    file.write(decode(text_input))