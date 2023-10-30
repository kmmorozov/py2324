#print(10 / 0) - ZeroDivisionError
#print(a) - NameError
#int('gndfklgdfklgj') - ValueError
#print('2344'*'234234') - TypeError

try:
    a = int('kirill')

except ZeroDivisionError:
    print('на 0 делить нельзя! ')
except NameError:
    print('переменная не задана')
except ValueError:
    print('невозможно привести к числу')
except TypeError:
    print('Ошибка типа данных')
except:
    print('Произошла ошибка!!!')
