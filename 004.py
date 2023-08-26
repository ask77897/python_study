# example = [[1, 2, 3], [4, [5, 6]], 7, [8,9]]
#숙제 - 위 리스트를 [1,2,3,4,5,6,7,8,9] 로 출력 
# print(len(example))
# def flatten(data):
#     flat_lst = []
#     for i in range(len(data)):
#         if i == 0:
#             for j in range(len(data[i])):
#                 flat_lst.append(data[i][j])
#                 return
#         if len(data) == 1:
#             for j in range(len(data[i])):
#                 if j == 0:
#                     flat_lst.append(data[i][j])
#                 if j == 1:
#                     for k in range(len(data[i][j])):
#                         flat_lst.append(data[i][j][k])
#         if len(data) == 2:
#             flat_lst.append(data[i])
#         if len(data) == 3:
#             for j in range(len(data[i])):
#                 flat_lst.append(data[i][j])
#     print(flat_lst)
    # for i in range(len(data)):
    #     if type(i) == list:
    #         for j in range(len(data[i])):
    #             if type(j) == list:
    #                 for k in range(len(data[i][j])):
    #                     flat_lst.append(data[i][j][k])
    #             else:
    #                 flat_lst.append(data[i][j])
    #     else:
    #         flat_lst.append(data[i])
    # print(flat_lst)
          
# print(flatten(example)) #[1,2,3,4,5,6,7,8,9]

#----------#

#람다(lambda)는 익명 함수를 생성하는 키워드다.
#코드를 짧게 만드는데 사용됨
#함수를 만들때, 간단한 함수를 만든다. 매개변수, return, def... 과정들이 너무 번거롭기 때문에

#lambda arguments: expression
# def add(x, y):
#     return x+y
# add_lambda = lambda x, y: x+y
#lambda 람다 키워드
#arguments 매개변수 x, y
#expression 표현식 x+y

# print(add(3,4))
# print(add_lambda(3,4))

#----------#

# map 함수 -> 파이썬 내장 함수
#주어진 함수를 반복 가능한(iterable) 객체의 각 원소에 적용하고, 결과를 반환한다.
#리스트 컴프리헨션

#map(function, iterable) -> 원래 객체의 각 원소에 해당 함수를 적용한 결과
# def square(x):
#     return x*x
    
# lst = [1,2,3,4,5]
# square_lst = map(square,lst)
# lst = list(square_lst)

# lst = [1,2,3,4,5]
# square_lst = map(lambda x : x*x, lst)
# lst = list(square_lst)
# print(lst)

# a = [1,2,3,4,5,6,7,8,9,10]
# for i in range(len(a)):
#     if a[i]%2 == 0:
#         a[i] = 0
# print(a)

# def f(x):
#     if x%2 ==0:
#         return 0
#     else:
#         return x

# for i in range(len(a)):
#     a[i] = f(a[i])
# print(a)

# a = [1,2,3,4,5,6,7,8,9,10]
# print(list(map(f,a)))
# print(list(map(lambda x:0 if x%2==0 else x, a)))

#----------#

# filter 함수 -> 파이썬 내장 함수
#주어진 함수를 반복 가능한(iterable) 객체의 결과가 참인 원소들만 반환한다.

#filter(function, iterable)
# def is_even(x): #retrun 값이 boolean
#     return x%2 ==0
# lst = [1,2,3,4,5]

# even_lst = filter(is_even, lst)
# even_lst = filter(lambda x: x%2 == 1, lst)

# print(list(even_lst))

#----------#

# numbers = [12, 32, 55, 12, 32, 4, 86, 50]
#60보다 크면 합격 50~60 대기, 50보다 작으면 불합격
# print(list(map(lambda x:"합격" if x>60 else "대기" if 50<=x else "불합격", numbers)))

# files = ["memo.txt", "1.jpg", "32.png", "23.jpg", "223.jpg"]
#리스트에서 확장자가 jpg인것만 골라내 리스트를 만드세요
# print(list(filter(lambda x: x.find(".jpg") != -1, files)))
# print(list(filter(lambda x: '.jpg' in x, files)))
# for i in files:
#     if ".jpg" in i:
#         print(i)

#숙제 - in, find('.jpg') 사용하지 않고 위 문제 해결해보기
# files = ["memo.txt", "1.jpg", "32.png", "23.jpg", "223.jpg"]



#리스트 세개의 곱
# lst1 = [1,2,3,4,5]
# lst2 = [1,3,5,7,9]
# lst3 = [2,4,8]
# print(list(map(lambda x, y, z: x*y*z, lst1,lst2,lst3)))
# print(list(map(lambda x : x[0]*x[1]*x[2], zip(lst1,lst2,lst3))))
#1~10 제곱 값 중 홀수만 출력해보기
# a = list(map(lambda x: pow(x,2) , range(1,11)))
# print(a)
# print(list(filter(lambda x: x%2==1, a)))
# print(list(filter(lambda x: x%2==1, map(lambda x: pow(x,2) , range(1,11)))))

#----------#

# class Dog:
#     def __init__(self, name, color):
#         self.hungry = 0
#         self.name = name
#         self.color = color
#     def eat(self):
#         self.hungry-=10
#         print("밥먹음", self.hungry)
#     def walk(self):
#         self.hungry+=10
#         print("산책",self.hungry)
        
# choco = Dog("choco", "black")
# jjong = Dog("jjong", "white")

# choco.eat()
# jjong.eat()
# choco.walk()
# print(choco.hungry)
# print(jjong.hungry)

#계산기 클래스 변수 2개 +-*/ 연산
# class Calc:
#     def __init__(self):
#         self._num1 = 0
#         self._num2 = 0
#         self._expression = ""
#     def set_num1(self, num):
#         self._num1 = num
#     def set_num2(self, num):
#         self._num2 = num    
#     def set_num1(self, exp):
#         self._expression = exp
#     def add(self):
#         return self._num1 + self._num2
#     def substract(self):
#         return self._num1 - self._num2
#     def multiply(self):
#         return self._num1 * self._num2
#     def divide(self):
#         if self._num2 == 0:
#             return print("err")
#         return self._num1 / self._num2
# cal1 = Calc(2,4)
# print(cal1.add())
        
# class Car:
#     Car_cars = 0
#     def __init__(self, name, years, gas):
#         self._name = name
#         self._years = years
#         self._gas = gas
#         Car.Car_cars += 1
#     def get_name(self):
#         return self._name
#     def set_name(self, name):
#         self._name = name
#     def gases(self):
#         if self._gas < 1000:
#             return "소형"
#         elif self._gas<=2000:
#             return "중형"
#         else:
#             return "대형"
#     @classmethod
#     def cars(cls):
#         print("총 등록된 차량은",cls.Car_cars, "대 입니다.")

# car1 = Car("부릉이",90,2000)
# car2 = Car("폭스바겐", 20, 3000)
# Car.cars()
# print(car1.gases())
# print(car2.gases())

# class Dog:
    
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age
#     def sayHello(self, name, age):
#         print("멍멍: ", name, "왈왈: ", age)
#     def ageCal(self):
#         print("사람 나이로 환산하면 ", (24+(self._age-2)*4), "세 입니다.")
#     def compAge(self):
#         return (24+ (self._age-2) * 4) > Person.getAge(Person, person1)
#     def printR(self):
#         if (24+(self._age-2)*4>Person.getAge):
#             print(self._name, "의 나이가 ", Person.getName(Person, person1), "보다 많습니다.")
#         else:
#             print(self._name, "의 나이가 ", Person.getName(Person, person1), "보다 적습니다.")

# class Person:
    
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age
#     def Hello(self, name, age):
#         print("안녕 내 이름은 ", name, ", 나이는 ", age, "살이야")
#     def getAge(self):
#         return self._age
#     def getName(self):
#         return self._name

# dog1 = Dog("백구", 4)
# dog2 = Dog("황구", 2)
# dog1.ageCal()
# dog2.ageCal()
# person1 = Person("Kim", 30)
# person2 = Person("Lee", 26)
# dog1.printR()
# dog2.printR()

