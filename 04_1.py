# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE -> 6A1F2D7C1A17E


with open('in.txt', 'r') as file:
    text_input = file.readline()

def encode(text: str):
    encoding = '' 
    prev_char = '' 
    count = 1

    for char in text:
        if char != prev_char:
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    encoding += str(count) + prev_char
    return encoding

with open('out.txt', 'w') as file:
    file.write(encode(text_input))



