import sys
import hashlib


login = input("Введтье логин:")
passwd = input("Введите пароль: ")

h_passwd = hashlib.sha256(passwd.encode()).hexdigest()
print(h_passwd)

if login == "kirill" and h_passwd == 'c71df59dfc22b2cfb4c2b54a01479fb8c070668db53fcad55f42639bb33af3d3':
    print('work')
else:
    print("Ошибка ввода пароля")
    sys.exit(0)