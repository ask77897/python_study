#숙제 - 아래 리스트를 [1,2,3,4,5,6,7,8,9] 로 출력 
# example = [[1, 2, 3], [4, [5, 6]], 7, [8,9]]
# def flatten(data):
#     flat_lst = []
#     for i in data:
#         if type(i) ==list:
#             flat_lst += flatten(i)
#         else:
#             flat_lst.append(i)
#     return flat_lst
# print(flatten(example))
#숙제 - in, find('.jpg') 사용하지 않고 위 문제 해결해보기
# files = ["memo.txt", "1.jpg", "32.png", "23.jpg", "223.jpg"]
# str = "jpgpgjgpjpgjgpjgpjgpjpgjpjgp" # 몇개의 jpg가 들어가 있는지
# print(str.split("jpg"))
# print(str.split("gpjgpj"))
# cnt=0
# for i in range(len(str)-2):
#     if str[i] =="j":
#         if str[i+1] == "p":
#             if str[i+2] == "g":
#                cnt+=1
# print(cnt)
#숙제 람다식으로 바꿔보기
# lst = []
# for i in range(len(str)):
#     if str[i] =="j" and str[i+1]=="p" and str[i+2]=="g": #if str[i]+str[i+1]+str[i+2] == "jpg"
#         lst.append(str[i:i+3])
# print(len(lst))

# print(list(filter(lambda x: str[x]+str[x+1]+str[x+2] == 'jpg', range(len(str)-2))))
# print(list(filter(lambda x: ".jpg" == x[len(x)-4:], files)))
# files_lst = []
# for i in files:
#     for j in range(len(i)):
#         if (i[j]=="."):
#             if i[j+1:]=="jpg":
#                 files_lst.append(i)
#                 break
#숙제 - "gpjgpj" 가 있는지 겹치는것 불가 ex"gpjgpjgpj" = 1개
# str = "gpjgpjgpjgpjgpjgpjgpjgpjgpj"
# print(list(filter(lambda x: str[x]+str[x+1]+str[x+2]+str[x+3]+str[x+4]+str[x+5] == 'gpjgpj', range(len(str)-5))))

#----------#

# class Dog:    
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age
#     def sayHello(self, name, age):
#         print("멍멍: ", name, "왈왈: ", age)
#     def ageCal(self):
#         print("사람 나이로 환산하면 ", (24+(self._age-2)*4), "세 입니다.")
#     def compAge(self, personAge):
#         return (24+ (self._age-2) * 4) > personAge
#     def printR(self, person):
#         if (24+(self._age-2)*4>person.age):
#             print(self._name, "의 나이가 ", person.name, "보다 많습니다.")
#         else:
#             print(self._name, "의 나이가 ", person.name, "보다 적습니다.")

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
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

#----------#

# class Animal:
#     def __init__(self):
#         self.hungry = 0
#     def eat(self):
#         self.hungry -= 10
#         print("밥먹음", self.hungry)
#     def walk(self):
#         self.hungry += 10
#         print("산책", self.hungry)
        
# class Dog(Animal):
#     def __init__(self):
#         super().__init__()
#     def sound(self):
#         print("멍멍")
#     def eat(self):
#         super().eat()
#         print("왈왈")

# class Student:
#     def __init__(self, name="학생", studentnumber=0, grade=0):
#         self._name = name
#         self._studentnumber = studentnumber
#         self._grade = grade
#     def getName(self):
#         return self._name
#     def getGrade(self):
#         return self._grade
#     def info(self):
#         return "이름: ", self._name,", 학년: ",self._grade, ", 학번: ", self._studentnumber
    
# class Student20(Student):
#     gradeNumber = 20
#     number = 1
#     def __init__(self):
#         super().__init__(studentnumber=str(Student20.gradeNumber) +"0"+ str(Student20.number), grade=4)
#         self.student = Student20.number
#         self.zero = "000"
#         Student20.number += 1
#     def zeroset(self):
#         num = self.student
        
#         while ((num//10) > 0):
#             self.zero = self.zero[0: len(self.zero)-1]
#             num//=10
#         return self.zero
#     def info(self):
#         super().info()
#         return "이름: ", str(super().getName()), "학년: ", str(super().getGrade()), "학번: ", str(Student20.gradeNumber) + str(self.zeroset())+str(self.student)

# student1 = Student20()
# student2 = Student20()
# student3 = Student20()
# student4 = Student20()
# student5 = Student20()
# student6 = Student20()
# student7 = Student20()
# student8 = Student20()
# student9 = Student20()
# student10 = Student20()
# print(student1.info())
# print(student2.info())
# print(student3.info())
# print(student4.info())
# print(student5.info())
# print(student6.info())
# print(student7.info())
# print(student8.info())
# print(student9.info())
# print(student10.info())

#----------#

#Account - (ATM Account, BankAccount, CreditAccount)
#ATM = 현금 입출금
#Bank = 예금 이자(최저 금액 이상 이자)
#Credit = 결제 (한도 초과)

# class Account:
#     def __init__(self, name, account, balance = 0):
#         self._name = name
#         self._account = account
#         self._balance = balance

#     def getBalance(self):
#         return self._balance

#     def setBalance(self, balance):
#         self._balance = balance

# class AtmAccount(Account):
#     def __init__(self, name, account, balance=0, cash=0):
#         super().__init__(name, account, balance)
#         self._cash = cash

#     def deposit(self, cash):
#         self._cash += cash
#         self.setBalance(self.getBalance() + cash)

#     def withdraw(self, cash):
#         if self.getBalance() < cash:
#             print("잔액이 부족합니다. 출금할 수 없습니다.")
#         else :
#             check = input("1. 5만원권을 최대로, 2. 선택, 3. 1만원을 최대로")

#             if check == 1:
#                 c5 = cash // 50000
#                 cash -= c5*50000
#                 print(f"출금을 완료되었습니다. 5만원권 {c5}장 과 만원권 {cash//10000}장을 받아가세요.")

#             elif check == 2:
#                 c1 = input("5만원권의 장수와 1만원권의 장수를 순서대로 입력해주세요.") # 5 10
#                 c = c1.split(' ')
#                 print(f"출금을 완료되었습니다. 5만원권 {c[0]}장 과 만원권 {c[1]}장을 받아가세요.")

#             elif check == 3:
#                 m = cash // 10000
#                 print(f"출금을 완료되었습니다. 만원권 {m}장을 받아가세요.")

#     class BankAccount(Account):
#         def __init__(self, name, account, balance=0):
#             super().__init__(name, account, balance)

#         def interest(self):
#             return super()._balance * 0.05 / 12

#     class creditAccount(Account):
#         def __init__(self, name, account, balance=0, pay=0, limit=10000000):
#             super().__init__(name, account, balance)
#             self._pay = pay
#             self._limit = limit

#         def payment(self, pay):
#             if self._limit < self._pay + pay:
#                 print("결제할 수 없습니다. 한도초과입니다.")

#             else :
#                 self._pay += pay
#                 print("결제가 완료되었습니다. {}원이 결제되었습니다.".format(pay))

#----------#

# from abc import * # * -> 전부 다 라는 의미
# from abc import ABC, abstractmethod
#Abstract Base Class -> abc
# class Animal(metaclass=ABCMeta):
#     @abstractmethod
#     def eat(self):
#         pass
# class Dog(ABC):
#     @abstractmethod
#     def walk(self):
#         pass
#     def eat(self):
#         print("우걱우걱")
# class Golden(Dog):
#     @abstractmethod
#     def walk(self):
#         print("터벅터벅")

#인터페이스 왜 없나?? 
#다중 상속이 가능 -> 인터페이스가 필요없다.

# class Cat(ABC, Animal):
#     @abstractmethod
#     def sound(self):
#         pass

#----------#

#음식(추상클래스)-(피자,햄버거,김밥)
# from abc import *
# from abc import ABC, abstractmethod

# class Food(metaclass=ABCMeta):
#     def __init__(self, name) -> None:
#         self.name = name
#     @abstractmethod
#     def food(self):
#         pass
# class Pizza(Food):
#     def __init__(self, name, topping, crust):
#         super().__init__(name)
#         self._topping = topping
#         self._crust = crust
#     def food(self):
#         print("페퍼로니피자입니다.")
# class Burger(Food):
#     def __init__(self, name, patty):
#         super().__init__(name)
#         self.patty = patty
#     def food(self):
#         print("페퍼로니버거입니다.")
# class Gimbop(Food):
#     def __init__(self, name, inside):
#         super().__init__(name)
#         self.inside = inside
#     def food(self):
#         print("페퍼로니김밥입니다.")


