'''
x = [12,434,565,77]
z = [0,10,20,30,40]

y = x + z
print (y)


print(x)

#y = x[0]
#print(y)


#x[0] = 569
#print(x)

#x.append(100)
#print(x)

#x.insert(2, 500)
#print(x)

#x.remove(12)
#print(x)
#x.pop(2)
#print(x)

#x.remove(12)
#print(x)

print (10 in y)
'''

#Dictionaries
'''
x = {'1000':'Colombo',"12500":"Panadura"}
x['1200'] = "Moratuwa"
print(x)

print(x.keys())

print(x.values())

y = x['1000']
print(y)

x[0]="Zero"
print(x.keys())
print(x.values())
print(x)

x['Cities'] = {1: '6876', 78: "8656" }

y = x['Cities']
print(y)
print(x)


x = {1: 'A', 2:'B'}
y = x[1]
y = x.get(3, 0)
print(y)

#del x[2]
#print(x)

x.clear()
print(x)

'''

x = {
    "a":['Hello','Hi','Good morning'],
    "b":['Bye','Good night']
}

y = x['a']
y.append('Good afternoon')
print(y)
print(x)