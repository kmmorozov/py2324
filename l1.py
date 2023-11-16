l1 = ['kirill', 'ivan', 'pavel','sergey','sergey']
l2 = ['maria','anna','svetlana']
print(l1)
print(type(l1))

l1.append('sergey')
print(l1)
l1.append(l2)
print(l1)
print(l1[2])
print(l1[4][1])
l1.insert(0,'Alexander')
print(l1)
l1.remove('kirill')
print(l1)
l1.pop(2)
print(l1)
print(l1.index('sergey'))
print(l1.count('sergey'))


