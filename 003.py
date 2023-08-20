# person1 = {"치킨", "피자", "자장면"}
# person2 = {"국밥", "고기", "피자"}
# person3 = {"피자", "백반", "찌개"}
# for i in person1:
#     for j in person2:
#         for k in person3:
#             if i==j==k:
#                 print("공통음식:", i)
            
# for i in person1:
#     if i in person2 and i in person3:
#         print("공통음식:", i)
        
        
        
# for i in person1:
#     for j in person2:
#         if i==j:
#             for k in person3:
#                 if i==k:
#                     print("공통음식:", i)
                    
# for i in person1:
#     if len(person2) < len(person3):
#         for i in person2:
#             if i==j:
#                 for k in person3:
#                     if i==k:
#                         print("공통음식:",i)
#     else:
#         for j in person3:
#             if i==j:
#                 for k in person2:
#                     if i==k:
#                         print("공통음식:",i)

#100이하의 소수(약수가 1과 자기자신)으로 이루어진 1차원 리스트 컴프리헨션으로 만들기
# t3 = [i for i in range(1,101) if(i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0 and i!=1) or (i==2 or i==3 or i==5 or i==7)]
# print(t3)

# t3_1=[]
# for i in range(2,101):
#     if (i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0) or (i==2 or i==3 or i==5 or i==7):
#         t3_1.append(i)
# print(t3_1)
# t3_2=[]
# for i in range(2,101):
#     for j in range(2,i):
#         if i%j==0:
#             break
#         elif i-1==j:
#             t3_2.append(i)
# print(t3_2)
# t3_3=[]
# for i in range(2,101):
#     isPrime = True
#     for j in range(2,i):
#         if i%j==0:
#             isPrime = False
#             break
#     if isPrime==True:
#             t3_3.append(i)
# print(t3_3)

# t3_4=[i for i in range(2,101) if all(i%j!=0 for j in range(2,i))]
# print(t3_4)

#----------#

#all함수, any함수
#여러 개의 조건 or 값이 있는 리스트, 튜플, set ... 값의 조건에 따라 True or False 리턴하는 함수

#all함수 -> 모든 값이 True일 때, True
#any함수 -> 하나라도 True이면, Treu

# num=[i+1 for i in range(10)]
# lst = [x for x in num if x%2==0]
# print(lst)
# num2 = all(x%2 == 0 for x in num)
# print(num2)
# num3 = all(x%2 == 0 for x in lst)
# print(num3)

# num2 = any(x==5 for x in num)
# print(num2)
# num3 = any(x==5 for x in lst)
# print(num3)

#----------#

# for i in range(5):
#     print(' ')
#     for j in range(5):
#         print("*", end = "")

# for i in range(5):
#     print('')
#     for j in range(5):
#         if i>=j:
#             print("*", end="")
#         else:
#             print(" ",end="" )

# for i in range(5):
#     print('')
#     for j in range(5):
#         if i==j:
#             print("*", end="")
#         else:
#             print(" ", end="")

# for i in range(5):
#     print('')
#     for j in range(5):
#         if i+j<=4:
#             print("*", end="")
#         else:
#             print(" ", end="")

# for i in range(5):
#     print('')
#     for j in range(5):
#         if i<=j:
#             print("*", end="")
#         else:
#             print(" ", end="")

# a1 = [["*" for i in range(5)] for j in range(5)]
# print(a1)
# a2 = [["*" for i in range(j+1)] for j in range(5)]
#     #  ["*"*(i+1) for i in range(5)]
# print(a2)
# a3 = [" "*i+"*" for i in range(5)]
# print(a3)
# a4 = [["*" for i in range(5-j)] for j in range(5)]
#     #  ["*"*(5-i)for i in range(5)]
# print(a4)
# a5 = [" "*i+"*"*(5-i) for i in range(5)]
# print(a5)

#----------#

# list = [1,2,3,1,4,2,1]

# def allindex(a,b):
#     c=[]
#     for i in range(len(a)):
#         if a[i]==b:
#             c.append(i)
#     print(c)

# allindex(list, 1)    

#----------#

# person1 = ["치킨", "피자", "족발", "삼겹살"]
# person2 = ["김밥", "김치찌개", "삼겹살", "쌈밥"]
# person3 = ["치킨", "김치찌개", "떡볶이", "초밥", "삼겹살", "족발", "햄버거", "보쌈", "한우", "아이스크림"]

# menu1 = any(i in person2 for i in person1)
# print(menu1)
# menu = [menu1 for menu1 in person1 if any(menu1==menu2 for menu2 in person2)]
# print(menu)
# lst = [menu1 for menu1 in menu if any(menu1==menu3 for menu3 in person3)]
# print(lst)

#----------#

#함수, 매개변수
#1. 기본 인자값(default argument values)
#함수에 전달되는 기본 매개변수 기본값을 지정해주는 것
# def func1(pa1 = 1, pa2 = 2, pa3 = 3):
#     return 0

#2. 키워드 인자(keyword argument)
#함수에 전달되는 인자를 키와 값의 형태로 전달하는 것
#순서 상관없이 키값에 일치하는 곳에 값이 전달된다.
# def greeting(name, message = "hello"):
#     print(f"{message}, {name}")
# greeting(message = "안녕", name = "홍길동")
# greeting(name = "김철수")

#3. 가변 인수 리스트(Arbitrary Argument Lists)
#함수에 전달되는 매개변수 앞에 (*)을 붙여서 가변 인수로 지정해주는 것
#인자가 일렬로 나열되서 전달되는데, tuple 형태로 전달이 된다.
# def sum(*args):
#     res = 0
#     for arg in args:
#         res += arg
#     return res
# print(sum(1,2,3))
# print(sum(1,2,3,4,5,6,7,1232353,423464778))

#4. 위치 인자 리스트(positional argument lists)
#함수에 전달되는 매개변수 앞에 (**)을 붙여서 인자 리스트로 지정해주는 것
#만약 함수를 호출했을 경우 키와 값 쌍의 형태로 값이 전달되면, 딕셔너리 형태로 전달된다.
# def greeting2(**kwargs):
#     for name , message in kwargs.items():
#         print(f"{message}, {name}")
# greeting2(Chris = "hello", Bob = "안녕")

#----------#

# def calc(a, *args):
#     sum = 0
#     multi = 1
#     if a == "+":
#         for arg in args:
#             sum += arg
#         print(sum)
#     elif a == "*":
#         for arg in args:
#             multi *= arg
#         print(multi)
# calc("+", 1,2,3,4,5)
# calc("*", 1,2,3,4,5)

#----------#

# 재귀함수
#1. 함수 내부에서 자기 자신 함수를 호출해야 한다.
#2. 재귀를 종료시켜주는 조건문이 존재해야 한다.
# def test(end):
#     if end == 0:
#         return
#     print(end)
#     # end -= 1
#     test(end-1)
# test(5)

# def factorial(n):
#     if n==1:
#         return 1
#     return n*factorial(n-1)
# print(factorial(5))

# def f_sum(n):
#     if n == 0:
#         return n
#     return n + f_sum(n-1)
# print(f_sum(5))

# def f_number(n):
#     if n<10:
#         print(n)
#     else:
#         f_number(n//10)
#         print(n%10)
# f_number(1234)

#두 수 사이의 홀수 전부 출력
#print_odd(1,10) 1 3 5 7 9
# s = int(input("시작 숫자:"))
# e = int(input("끝 숫자:"))
# def print_odd(s, e):
#     if s > e:
#         return
#     if s % 2 != 0:
#         print(s)
#     print_odd(s+1, e)
# print_odd(s, e)

#피보나치 수열 1 1 2 3 5 8 13 21 34 ...
#fibo(6) - 8
# def fibo():
num = int(input("몇 번째 숫자까지?"))
def fibo(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
for i in range(1, num+1):
    print(fibo(i))
    
#10진수 -> 2진수로 변환하기
#binary(10) - 1010
#2 - 10
# def binary(n):
#     if n<2:
#         print(n%2,end = "")
#     else:
#         binary(n//2)
#         print(n%2,end = "")
# binary(13)
    



























