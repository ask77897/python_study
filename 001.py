# print("hello")

# x = int(input())
# y = int(input())
# print(x+y)
# print(x*y)
# print(x**y)


# a = 11
# b = 5.0

# c = a//b
# d = a%b
# e = a**b
# print(c,d,e)

# score1 = int(input())
# score2 = int(input())
# score3 = int(input())

# print(score1>65 and score2>65 and score3>65)


# print("과일"*3)

# word = "Apple Banana"

# print(len(word))
# print(word.replace("Banana", "Orange"))
# print(word.upper())
# print(word.lower())
# print(word.replace(" ", ""))


# score = int(input())
# if(score>=90):
#     print("축하합니다. 당신은 합격입니다.")
# else:
#     print("아쉽게도 불합격입니다.")
    
    

# for i in range(1,10):
#     print(i)
# for i  in range(0, 10, 2):
#     print(i)
# for i in range(10, 0, -1):
#     print(i)
# for i in range(10):
#     print(i)
#range(1.처음, 2. 끝, 3. 중간)
#1. 어디서부터 시작할래?
#2. 어디까지 할래?
#3. 어떻게 진행할래?
#1,3 생략가능

# num = int(input("몇단을 출력하시겠습니까? :"))
# for i in range(1,10):
#    print(num,"*",i,"=",(num*i))
# for i in range(2,10):
#     print("-----------------",i,"단------------")
#     for j in range(1,10):
#         # print(i,"*",j, "=", (i*j))
#         print("%d X %d = %d" %(i, j, i*j))
#         print()

# num1 = input()
# for i in range(2,10):
#     for j in range(1,10):
#         if num1=="홀수":
#             if i%2==0:
#                 continue
#             elif i%2!=0:
#                 print(f"{i} X {j} = {i*j}")
#         elif num1=="짝수":
#             if i%2!=0:
#                 continue
#             elif i%2==0:
#                 print(f"{i} X {j} = {i*j}")
                
# for i in range(2,10):#홀수단 출력
#     for j in range(1,10):
#         if i%2==0:
#            continue             
#         elif i%2!=0:
#             print(f"{i} X {j} = {i*j}")

# for i in range(2,10):#짝수단 출력
#     for j in range(1,10):
#         if i%2!=0:
#            continue             
#         elif i%2==0: 
#             print(f"{i} X {j} = {i*j}")
        

# num1 = 1
# num2 = 0
# while num1!=0:
#     num1 = int(input("값을 입력하세요.: "))
#     num2 += num1
# print("합계:",num2) 

# num1 = 1
# num2 = 0
# while (True):
#     num1 = int(input("값을 입력하세요.: "))
#     num2 += num1
#     if num1==0:
#         break
# print("합계:",num2) 

#Hello world -> Hell wrld
# str = "Hello World"
# print(str.replace("o", ""))

# lst = list(str)
# print(lst)

# for i in lst:
#     if(i=="o"):
#         continue
#     print(i, end="")
# print()
# del lst[4]
# del lst[6]
# print(lst)

# lst = list(str)
# lst.pop(4)
# lst.pop(6)
# print(lst)

# lst = list(str)
# print(lst[:4]+lst[5:7]+lst[8:])

# str1=""
# for i in lst[:4]+lst[5:7]+lst[8:]:
#     str1 += i
# print(str1)

# lst1 = str.split("o")
# print(lst1)

# lst = list(str)
# lst2 = []
# start = 0
# for i in range(len(lst)):
#     if lst[i] == "o" or i == len(lst)-1:
#         lst2 += lst[start:i]
#         start = i+1
# print(lst2)

# lst = list(str)
# for i in range(len(lst)):
#     if i==len(lst):
#         break
#     if lst[i]=="o":
#         del lst[i]
# print(lst)

# lis = list("helloooo woorld")
# lis2 = list("ooooooooooooooo")
# i = 0
# while(True):
#     if i==len(lis):
#         break
#     if lis[i] == "o":
#         del lis[i]
#     else:
#         i+=1
# print(lis)

# i = 0
# while(True):
#     if i==len(lis2):
#         break
#     if lis2[i] == "o":
#         del lis2[i]
#     else:
#         i+=1
# print(lis2)

# lis = list("helloooo woorld")
# for j in range(len(lis)):
#     for i in range(len(lis)):
#         if lis[i] == "o":
            
            

# x = int(input("찾으려는 값을 입력하세요.:"))
# a = [1, 1, 2, 2, 2, 2, 3, 3]
# cnt = 0
# print(a.count(x))

# for i in range(len(a)):
#     if a[i]==x:
#         cnt+=1
# print(f"{cnt}개 있습니다.")
        
        
# b = [1, 2, 3, 4]
# c = []
# b.reverse()
# print(b)
# print(len(b))
# c = b
# for i in range(len(b)):
#     if c[i]==b[0]:
#         b.insert(len(b),c[i])
#         b.pop(0)
#         print(b)
#     if c[i]==b[0]:
#         b.insert(len(b)-1,c[i])
#         b.pop(0)
#         print(b)
#     if c[i]==b[0]:
#         b.insert(len(b)-2,c[i])
#         b.pop(0)
#         print(b)

# for i in range(len(b)-1, -1, -1):
#     c.append(b[i])
    
# print(c)

# start, end = 0, len(b)-1  
# temp = 0
# while end > start:
#     temp = b[start]
#     b[start] = b[end]
#     b[end] = temp #b[start], b[end] = b[end], b[start]
#     start+=1
#     end-=1

# print(b)

# for i in range(len(b)//2):
#     temp = b[i]
#     b[i] = b[len(b)-i-1]
#     b[len(b)-i-1] = temp
# print(b)

n = 123456

print(n)
nlst = list(n)
print(nlst)

#2*5 이차원리스트로 1~10 채우기
# q = [[0,0],[0,0],[0,0],[0,0],[0,0]]
# for i in range(5):
#     for j in range(2):
#         q[i][j] = i*2+j+1
# print(q)















