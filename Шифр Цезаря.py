def encrypt(n, text):  #функция определяет язык и направление сдвига в Шифре Цезаря
    a = []
    if text[0] in 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюя':
        for i in text:
            if i.islower() == True and i.isalpha() == True:
                if 1072 <= ord(i)+n <= 1103:
                    a += chr(ord(i)+n)
                elif ord(i)+n > 1103:
                    a += chr(ord(i)+n-32)
                elif ord(i)+n < 1072:
                    a += chr(ord(i)+n+32)
            elif i.isupper() == True and i.isalpha() == True:
                if 1040 <= ord(i)+n <= 1071:
                    a += chr(ord(i)+n)
                elif ord(i)+n > 1071:
                    a += chr(ord(i)+n-32)
                elif ord(i)+n < 1040:
                    a += chr(ord(i)+n+32)
            else:
                a += i
    else:
        for i in text:
            if i.islower() == True and i.isalpha() == True:
                if 97 <= ord(i)+n <= 122:
                    a += chr(ord(i)+n)
                elif ord(i)+n > 122:
                    a += chr(ord(i)+n-26)
                elif ord(i)+n < 97:
                    a += chr(ord(i)+n+26)
            elif i.isupper() == True and i.isalpha() == True:
                if 65 <= ord(i)+n <= 90:
                    a += chr(ord(i)+n)
                elif ord(i)+n > 90:
                    a += chr(ord(i)+n-26)
                elif ord(i)+n < 65:
                    a += chr(ord(i)+n+26)
            else:
                a += i
    return ''.join(a)

def list_count(x):
    a, b = 0, []
    for i in x:
        for j in i:
            if j.isalpha() == True:
                a += 1
        b.append(a)
        a = 0
    return b

def encrypt_strat():
    text_list = input().split()
    itog = []
    b = list_count(text_list)
    for i in range(len(text_list)):
        itog += encrypt((b[i]), text_list[i]) + ' '
    print(''.join(itog))

encrypt_strat()

#for i in range(len(text_list)):
    #b += (encrypt(len(text_list[i]), text_list[i]))

#print(b)



#print(encrypt())
a, b = 2, -1

#elif text[0] in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':



#print([int(i) for i in range(ord('a'), ord('z')+1)])
#print([int(i) for i in range(ord('A'), ord('Z')+1)])
