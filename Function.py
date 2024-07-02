
'''
def get_grade(marks,subject="Unknown"):

    print("Subject = ",subject)

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

get_grade(75)
get_grade(marks=35,subject="maths")

'''

def my_form(**param):
    if 'name' not in param:
        print("Error")
    else:
        print("Hello",param['name'])

my_form(name="sunil",height=176,city="colombo")
my_form(name="kasun",height=182)

