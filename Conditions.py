'''
x = 10

if x >= 150:
    print("You're selected!")
else:
    print("You're not selected!")
'''
'''
marks = 75

if marks > 50:
    result = "Pass"
else:
    result = "Fail"
print(result)
'''

#0-35 W
#35-55 S
#55-65 C
#65-75 B
#75-100 A
'''
marks = 85

if marks >= 0 and marks < 35:
    print("W")
else:
    if marks >= 35 and marks < 55:
        print("S")
    else:
        if marks >= 55 and marks < 65:
            print("C")
        else:
            if marks >= 65 and marks < 75:
                print("B")
            else:
                if marks >= 75 and marks <= 100:
                    print("A")
                else:
                    print("Invalid Marks")  

'''
'''
marks = 74

if marks >= 0 and marks < 35:
    print("W")
elif marks >= 35 and marks < 55:
    print("S")
elif marks >=55 and marks < 65:
    print("C")
elif marks >=65 and marks < 75:
    print("B")
elif marks >=75 and marks <= 100:
    print("A")
else:
    print("Invalid")
'''
'''

marks = -74

if marks < 0 or marks > 100:
    print("Invalid")
    exit()

if marks >= 0 and marks < 35:
    print("W")
elif marks < 55:
    print("S")
elif marks < 65:
    print("C")
elif marks < 75:
    print("B")
elif marks <= 100:
    print("A")

'''
'''
height = 176

if height > 150:
    job = ("Security")
else:
    job = ("Labor")
print(job)
'''

'''
#ternary
height = 140
msg = "Your job is " + "Security" if height > 150 else "Labor"
print(msg)
'''

#for Loop...
'''
x = [12,23,567,123,88]

index = 0

for item in x:

    y = x[index]
    print(index,y)
    index += 1
'''

'''
x = [12,23,567,123,88]

for item in enumerate(x):
    index = item[0]
    value = item[1]

    print(index,value)
    #print(type(item),item)
'''
'''
x = [12,23,567,123,88]

for index, value in enumerate(x):
    print(index,value)

'''
'''
for item in range(0,10):
    print(item)

'''
'''
x = [12,23,567,123,88]

r = range(0,10)
print(type(r))

for item in r:
    print(item)
'''
'''
x = [12,23,567,123,88]
r = range(0,len(x))
print(type(r))
for item in r :
    print(x[item])

'''

#while loop...
'''
x = [-12, -23, -567, -123, -8]

count = 0

while count < 10:
    print("Count",count)
    count += 1 

'''
'''
x = [-12, -23, -567, -123, -8]

count = 0

while True:
    
    if count >= 10:
        break

    print("Count",count)
    count += 1 

x = [12, 23, 567, 123, 8]

count = 0

for i in x:
    if i % 2 == 0:
        continue
    print(i)
    print(i ** 2)

while True:
    print("Index", count)

    if count == len(x) -1:
        break

    i = x[count]
    if i % 2 == 0:
        count += 1
        continue
    print(i)
    print(i ** 2)

    count += 1

    '''
'''
x = [12,23,567,123,88]

total = 0

for i in x:
    total += i

print("total",total)
print("Avg",total/len(x))
'''

'''
x = [12,23,567,123,88,599]

max = x[0]
min = x[0]

for i in x:
    if max < i:
        max = i
    if min > i:
        min = i

print("Max",max)
print("Min",min)

'''
'''
x = [12,23,567,123,88,599]

count = 0
total = 0 

while count < len(x):
    item = x[count]

    total += item
    count += 1

print("Total",total)
print("Avg",total/len(x))
'''
'''
x = [12,23,567,123,88,599]

count = 0
total = 0 

min = max = x[0]

while count < len(x):
    item = x[count]

    if item > max:
        max = item
    
    if item < min:
        min = item



    count += 1

print("Max",max)
print("Min",min)

'''

#Iteration...
'''
d = {
    "kasun":176,
    "Saman":167,
    "Ruwan":159,
    "Siri":160
}

for name in d:
    height = d[name]
    print(name,height)

'''
'''
d = {
    "kasun":176,
    "Saman":167,
    "Ruwan":159,
    "Siri":160
}

#for name in d.items():
  #  print(type(name))
    #print(name)

for name,height in d.items():
    print(name,height)

'''
d = {
    "kasun"
    "Saman"
    "Ruwan"
    "Siri"
}

for name in d:
    print(name)