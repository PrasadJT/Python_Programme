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



x = {
    "a":['Hello','Hi','Good morning'],
    "b":['Bye','Good night']
}

y = x['a']
y.append('Good afternoon')
print(y)
print(x)

'''

#Set...
'''
x = {"Hello","World","Hello","1","1"}

x.add("World")
x.add("World")#hash function

x.remove('1')

print(x)


#x = {'A','B'}
#y = x['A']
#print(y)

x = {"Hello","World","Hello","1","1"}
#y = {"x","y"}
#z = x.union(y)
#z = x | y
#print(z)

y = {"1","2"}
z = x - y
print(z)



#Tuples..

John = ("Jhon",176,"Sri Lanka","Germany")

print(type(John))
print(John)

name = John[0]
print(name)
print(John[1])

print(John.count("Jhon"))



x = (1,"Jhon",176)

index,name,height = x
print(type(x),x)
print(index,name,height)


x = ['a','b','c','d']

#slicing
y = x[2:4]
y = x[2:]
y = x[:2]
y = x[:-1]
y = x[:7]



print(y)
print(len(y)) #lenght

'''

x = "HELLO WORLD"
y = x[0:-1]

print(x[6])
print(y)

