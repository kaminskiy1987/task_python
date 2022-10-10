# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в
# отдельных текстовых файлах.
#
# Пример: aaaaaaabbbbbbccccccccc => 7a6b9c и 11a3b7c => aaaaaaaaaaabbbccccccc

pathRead1 = 'text5.txt'
eq = ''
with open(pathRead1) as f:
    for line in f.readlines():
       eq+= line

pathRead2 = 'text6.txt'
eq2 = ''
with open(pathRead2) as f2:
    for line in f2.readlines():
       eq2+= line

def rle_encode(s):
    encoding = ''
    i = 0

    while i < len(s):
        count = 1

        while i + 1 < len(s) and s[i] == s[i + 1]:
            count = count + 1
            i = i + 1

        encoding += str(count) + s[i]
        i = i + 1
        
    return encoding


def rle_decode(data):
    decode = ''
    count = ''

    for char in data:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ''

    return decode

enc = rle_encode(eq)
print("rle_encode: ", enc)

pathRead3 = 'text7.txt'
with open(pathRead3, 'w') as f3:
    f3.write(enc)

dec = rle_decode(eq2)
print("rle_decode", dec)

pathRead4 = 'text8.txt'
with open(pathRead4, 'w') as f4:
    f4.write(dec)
