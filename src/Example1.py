import time
import calendar

print(time.time())
print(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))

print(calendar.isleap(2018))
print(calendar.isleap(2016))
print(calendar.leapdays(2000,2016))
print(calendar.month(2018,2))

print("********************************************************")


def test(arg):
    print("inside function : ", arg)


def test2(arg1, arg2):
    print("inside function : ", arg1, arg2)


test3 = lambda arg1, arg2: print("inside lambda", arg1, arg2)
test("Hello Amaya")
test(23)
test2(arg2="Arvind", arg1="Hello")
test3("Hello","Pakuye")

print("********************************************************")


class User:

    __name = "Arvind"
    __age = 32

    def __init__(self, name, age):
        print("Loading constructor")
        self.__name = name
        self.__age = age

    def print(self):
        print("Printing user : "+self.__name, self.__age)

    def __del__(self):
        print("destroying objects ..")


user = User("Priyanka", 23)
user.print()


class Employee(User):
    __empId = 23

    def __init__(self, empId):
        self.__empId = empId

    def print(self):
        print("Overridden method" , self.__empId)

    def __del__(self):
        print("Destroying Employee Object")


employee = Employee(234)
employee.print()


