# q = [[0,0],[0,0],[0,0],[0,0],[0,0]]

# for i in range(len(q)):
#     for j in range(len(q[0])):
#         q[i][j] = 2*i+j+1
        
# for i in range(len(q)):
#     for j in range(len(q[0])):
#         print(q[i][j], end=" ")
#     print()
    
# q = []
# num = 1

# for i in range(5):
#     temp = []
#     for j in range(2):
#         temp.append(num)
#         num+=1
#     q.append(temp)
    
# print(q)

#----------#

# n = 123456
# lst = []

# while n > 0:
#     lst.append(n%10)
#     lst.insert(0,n%10)
#     n = n//10
    
# print(lst)

# for i in range(len(lst)//2):
#     temp = lst[i]
#     lst[i] = lst[len(lst)-i-1]
#     lst[len(lst)-i-1] = temp
    
# lst = []
# n = 123456
# num = 10
# count = 0
# while n > num:
#     num *= 10
#     count += 1
# print(count)
# print(n//10**count)

# while n > 0:
#     lst.append(n//10**count)
#     n = n % 10**count
#     count-=1
# print(lst)

#----------#

# x = input("이름입력: ")
# y = input("나이입력: ")
# z = input("연락처입력: ")
# p = dict(name = x, age = y, num = z)
# print(p)

# plst = []
# for i in range(2):
#     x = input("이름입력: ")
#     y = input("나이입력: ")
#     z = input("연락처입력: ")
#     p2 = {'name':x,'age':y,'num':z}
#     plst.append(p2)
# print(plst)

# plst2 = []
# while True:
#     x = input("이름입력: ")
#     y = input("나이입력: ")
#     z = input("연락처입력: ")
#     if y == 0:
#         break
#     p3 = {"name":x, "age":y, "num":z}
#     plst2.append(p3)
# print(plst2)
 
#----------#
# s = {1, 2, 3}
# n = [1, 2, 3]
# nset = set(n)
# s.add(3)
# print(s)       
#사람 세명이 각각 먹고 싶은 음식이 있다고 할 때, 어떤 메뉴를 시키는게 가장 좋을지(교집합)
# a = {"치킨", "피자", "자장면"}
# b = {"국밥", "고기", "피자"}
# c = {"피자", "백반", "찌개"}
# print(set.intersection(a,b,c))
# print(a&b&c)
#사람 3명이 각각 음식을 여러개 가지고 있다고 할 때, 두명이 서로 음식을 교환해보자
# a = {"치킨", "피자", "자장면"}
# b = {"국밥", "고기", "피자"}
# c = {"피자", "백반", "찌개"}

# while True:
#     print(a)
#     print(b)
#     print(c)
#     inputSet = int(input("1.교환하기, 2.종료하기"))
#     if inputSet == 1:
#         inputSet = int(input("누구와 교환? 2.b, 3.c"))
#         if inputSet == 2:
#             afood = input("어떤 음식을 교환?: ")
#             bfood = input("어떤 음식을 교환?: ")
#             if afood in a or bfood in b:
#                 print("이미 가지고 있는 음식입니다. 교환할 수 없습니다.")
#             elif afood in a and bfood in b:
#                 a.add(bfood)
#                 b.add(afood)
#                 a.remove(afood)
#                 b.remove(bfood)
#         elif inputSet ==3:
#             afood = input("어떤 음식을 교환?: ")
#             cfood = input("어떤 음식을 교환?: ")
#             if afood in a or cfood in c:
#                 print("이미 가지고 있는 음식입니다. 교환할 수 없습니다.")
#             elif afood in a and cfood in c:
#                 a.add(cfood)
#                 c.add(afood)
#                 a.remove(afood)
#                 c.remove(cfood)
#     elif inputSet ==2:
#         break
#     else:
#         print("잘못된입력")


#---------#
# lst = [1,2,3,4,5,6,7,8,9]

# max = lst[0]
# min = lst[0]
# sum = 0

# for i in lst:
#     if max < i:
#         max = i
#     if min > i:
#         min = i
#     sum += i
# print('max:',max," min:",min," sum:",sum)

#----------#

# fruit = "사과,배,옥수수,당근"
# fruit_list = []
# fruit_list = fruit.split(",")
# print(fruit_list)
# a = 0
# for i in range(len(fruit)):
#     if fruit[i]!="," and fruit[i]!=" ":
#         print(i, end = " ")
#         fruit_list.append(fruit[12:])
        
# for i in range(len(fruit)):
#     if fruit[i]=="," or fruit[i]==" ":
#         print(i, end = " ")
#         fruit_list.append(fruit[a:i])
# s = ''
# for i in fruit:
#     if i==",":
#         fruit_list.append(s)
#         s = ''
#     else:
#         print(i, end="")
#         s += i
# fruit_list.append(s)        
# print(fruit_list)

# fruit = "사과,배,옥수수,당근"
# fruit_list = []
# s = 0
# for i in range(len(fruit)):
#     if fruit[i] == ",":
#         fruit_list.append(fruit[s:i])
#         s = i+1
# fruit_list.append(fruit[s:len(fruit)])
# print(fruit_list)

# print(ord('a'))#ordinal position
# print(chr(97))#character

# fruit = "apple+pear-corn/carrot"
# fruit_list = []
# s = 0
# for i in range(len(fruit)):
#     if not((ord(fruit[i]) >= 65 and ord(fruit[i]) <= 90) or (ord(fruit[i]) >=97 and ord(fruit[i]) <= 122)):
#         if fruit[s:i] != "":
#             fruit_list.append(fruit[s:i])
#         s = i+1
# fruit_list.append(fruit[s:len(fruit)])
# print(fruit_list)

# fruit = "carrotapplecornpear"#만약 구분자가 없다면 단어 데이터베이스가 필요
# fruit_list = ['apple','pear','corn','carrot']#임시 데이터베이스
# lst=[]
# s = ''
# for i in fruit:
#     s+=i
#     if s in fruit_list:
#         lst.append(s)
#         s = ''
# if s in fruit_list:
#     lst.append(s) 
# print(lst)
# fruit = "-".join(fruit_list)
# print(fruit)

#----------#

# a = [i for i in range(10)]
# #a = [i] a에 [i]를 넣겠다.
# #i가 뭔데?
# #for i in range(10) :0...9
# #a = [0...9]
# print(a)

# a = [i for i in range(10) if i%2==0]
# #a = [i] a에 [i]를 넣겠다.
# #i가 뭔데?
# #for i in range(10) :0...9
# #if i%2==0 i는 2로 나눈 나머지가 0이야
# #a = [0,2,4,6,8]
# print(a)

# a = [i*j for i in range(2,10) for j in range(1,10)]
# #a = [i*j] a에 [i*j]를 넣겠다.
# #i가 뭔데?
# #for i in range(2,10) i는 2...9
# #j는 뭔데?
# #for j in range(1,10) j는 1...9
# print(a)

# word=["school","game","piano","science","hotel","mountain"]
# word2 = [i for i in word if len(i)>=6] #[word[i] for i in range(len(word)) if len(word[i])>=6]
# print(word2)
# wordn = [len(i) for i in word]
# print(wordn)

# a = [0,0,0,0,0,0,0,0,0,0]
# a = [i-j for i in range(10) for j in range(10) if i-j==0 ]
# b = [i*0 for i in range(10)]
# c = [i for i in range(1) for j in range(10)]
# d = [i-i for i in range(10)]
# e = [0 for _ in range(10)]
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)

# a = [[10,20], [30,40],[50,60]]
# b = [[2,3],[4,5],[6,7]]
# c = []
# for i in range(3):
#     temp = []
#     for j in range(2):
#         temp.append((a[i][j])*(b[i][j]))
#     c.append(temp)
# print(c)

#[[1,2],[3,4],[5,6]] 리스트 컴프리헨션으로 만들기
# t1 = [[2*i+j+1 for j in range(2)] for i in range(3)]
# print(t1)
#2차원 10*10 리스트 0으로 채우기 컴프리헨션으로 만들기
# t2_1 = [[0 for _ in range(10)] for _ in range(10)]
# t2_2 = [[i-i for i in range(10)] for _ in range(10)]
# t2_3 = [[i*0 for i in range(10)] for _ in range(10)]
# print(t2_1)
# print(t2_2)
# print(t2_3)
#100이하의 소수(약수가 1과 자기자신)으로 이루어진 1차원 리스트 컴프리헨션으로 만들기
# t3 = [i for i in range(1,101) if(i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0 and i!=1) or (i==2 or i==3 or i==5 or i==7)]
# print(t3)

for i in range(5):
    print(' ')
    for j in range(5):
        print("*", end = "")

for i in range(5):
    print(' ')
    for j in range(5):
        