import pymysql
connection = pymysql.connect(host='nadejnei.net', user='student', password='1q2w#E$R', database='test', port=33306)
cursor = connection.cursor()
cursor.execute('select * from telsprav')
data = cursor.fetchall()

f = open('users2alex.txt', 'w')

#print(data)



for elem in data:
    #print(elem)
    name = elem[0]
    surname = elem[1]
    sex = elem[2]
    phone = elem[3]
    user = f'{phone};{sex};{surname};{name}'
    f.write(user+'\n')

f.close()