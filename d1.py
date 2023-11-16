d1 = {'kirill':'89110271345', 'ivan':'3245235234', 'pavel':'3453453'}

d2 = {
    'fedor':'32423423',
    'stepan':'23564252',
    'nikolay':'67474574',
    'kirill':'1111111111'
}

d1.update(d2)
print(d1)
d1['saveliy'] = '32426252'
print(d1)


#print(d1.items())
#print(d1.keys())
#print(d1.values())
#print(d1['kirill'])
#print(d1['sergey'])
#try:
#    name = input('Введите имя: ')
#    print(f'Телефон абонента {name} - {d1[name]}')
#except KeyError:
#    print(f'Телефон абонента {name} - не найден')

#name = input('Введите имя: ')
#name = name.lower()
#print(name)
#print(f'Телефон абонента {name} - {d1.get(name,"не найден")}')


