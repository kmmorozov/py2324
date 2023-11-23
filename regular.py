import re
#stroka = 'Privet menya zovut Kirill, mne 38 let, moi telefon 89110271345, a pohta kmmorozov@gmail.com rabochiy telefon 2345678'

#result = re.match(r'Privet menya zovut Kirill',stroka)

#print(result)
#print(result.group(0))
#print(result.start())
#print(result.end())
#######################################################################
#result = re.search(r'telefon', stroka)
#print(result)
#print(result.group(0))

#result = re.split(r'moi',stroka)
#print(result)


#result = re.findall(r'telefon', stroka)
#print(result)

stroka = 'Privet menya zovut Kirill, mne 38 let, moi telefon 89110271345 , a pohta kmmorozov@gmail.com moi index 12345678 rabochiy telefon 2345678'

#phones = re.findall(r'\d{7,11}',stroka)
phones = re.findall(r'\b\d\d\d\d\d\d\d\b|\b\d\d\d\d\d\d\d\d\d\d\d\b',stroka)
print(phones)
emails = re.findall(r'\w+@\w+.\w+',stroka)
print(emails)



