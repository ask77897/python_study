# str = "gpjgpjgpjgpjgpjgpjgpjgpjgpj"
#"gpjgpj" 가 있는지 겹치는것 불가 ex"gpjgpjgpj" = 1개
# i = 0
# cnt = 0
# while i<len(str)-5:
#     temp = ""
#     for j in range(6):
#         temp+=str[i+j]
#     # if str[i] + str[i+1] + str[i+2]...
#     if temp == "gpjgpj":
#         cnt+=1
#         i+=5
#     i+=1
# print(cnt)

# cnt = 0
# while len(str)>6:
#     temp = ""
#     for j in range(6):
#         temp += str[j]
#     if temp == "gpjgpj":
#         cnt+=1
#         str = str[6:]
#     str = str[1:]
# print(cnt)
# print(list(map(lambda x: x[i:i+5]=="gpjgpj",i in range(len(str)))))

#람다식으로 바꿔보기
# str = "jpgpgjgpjpgjgpjgpjgpjpgjpjgp"
# res = (list(filter(lambda x: x[0] == "j", [str[i:i+3] for i in range(len(str)-2)])))
# print(res)
# a = (list(filter(lambda y: y == "jpg", res)))
# print(a)

#----------#

# x = [1,2,3]

# try:
#     print(10/0)
#     x[5]
# except ZeroDivisionError as e:
#     print("숫자를 0으로 나눌 수 없음", e)
# except IndexError as e:
#     print("잘못된 인덱스", e)

# class MyError(Exception):
#     def __init__(self):
#         super().__init__("나의 오류")
# try:
#     raise MyError
# except Exception as e:
#     print("예외발생", e)
    
# class NotNumberException(Exception):
#     def __init__(self):
#         super().__init__("NotNumber: 잘못된 입력입니다.")
    
    
# def gugudan(a):
#     if not(2<= a <=9):
#         try:
#             raise NotNumberException
#         except Exception as e:
#             print(e)
#     else:
#         for j in range(1,10):
#             print(f"{a}*{j}={a*j}") 

# gugudan(2)
# gugudan(10)

#----------#

#패키지에서 디렉토리 내에 __init__.py 파일이 있어야 한다.
#버전 업데이트 되면서 (반드시 있어야 된다. -> 없어도 된다.) 로 변경됨
#이제는 없어도 되지만, 약속같은 느낌으로 사용된다.

#----------#

#데코레이터(decorator)
#코드를 수정하지 않고, 함수, 메소드 동작을 변경하거나 확장하고 싶을 때 사용
#일반적으로, 함수를 다른 함수에 매개변수로 전달하는 것처럼 구현된다.

#데코레이터 함수와 래퍼 함수
#데코레이터 함수를 생성한다. (매개변수로 다른 함수를 받는다.)
#데코레이터 함수 내부에 래퍼 함수를 만든다.
#래퍼 함수가 함수의 동작을 변경, 확장해 줄 수 있다.

# def log_decorator(func):
#     def wrapper(*args, **kwargs):
#         print(func.__name__,"함수가 실행되기 전")
#         result = func(*args, **kwargs)
#         print(func.__name__,"함수가 실행된 후")
#         return result
#     return wrapper
# @log_decorator
# def function():
#     print("데코레이터 함수 실행")

# function()

#일급 객체의 조건
#변수에 저장할 수 있다.
#인수로 전달할 수 있다.
#반환값으로 사용할 수 있다.
#자료구조 내부에 넣을 수 있다.

#파이썬에서는 함수가 일급 객체이다.
#함수에 변수를 할당할 수 있고, 인수를 전달하고, 반환할 수 있다.

#클로저(Closure)
#함수 내부에서 정의된 함수에서 외부 함수의 변수를 참조하거나 변경을 하고,
#외부 함수가 종료된 후에도 해당 변수값을 유지할 수 있게 해주는 함수

# def outer(x):
#     def inner(y):
#         return x+y
#     return inner

# a = outer(5)
# res = a(3)
# print(res)

#숙제  - topping, addTopping() -> 리스트, 값 여러개, 값 하나

#----------#

#파일 입출력

#1. 파일 열기 (open) - 파일을 열어서 객체를 생성한다. 모드 설정(읽기, 쓰기, 추가 등)
#2. 파일 읽기 (read) or 파일 쓰기 (write) - 생성된 객체를 통해서 파일을 읽거나 쓸 수 있음.
#3. 파일 닫기 (close) - 파일 사용이 끝나면 반드시 닫아줘야 한다.
#   파일을 닫지 않으면, 메모리에 남아있어서 데이터 손실의 위험이 있다.

# file = open("example.txt", "w")
# file.write("파일 입출력 테스트")
# file.close()

# file = open("example.txt", "r")
# res = file.read()
# for i in res:
#     print(i, end = "")
#     if i == " ":
#         print()
# print(res)
# file.close()

# with open("example.txt", "r") as file:
#     res = file.read()
#     print(res)

#다이어리 프로그램 - 날짜를 입력하고, 일기 작성 날짜를 입력해서 작성한 일기를 출력

# def menu():
#     print("1. Write a diary")
#     print("2. Read a diary")
#     choice = int(input("어느 것을 하시겠습니까?"))

#     if choice == 1:
#         write_diary()
#     elif choice == 2:
#         read_diary()

# def write_diary():
#     date = input("날짜를 입력하세요(dd-mm-yyyy):")
#     text = input()
#     with open(f"{date}.txt", "w") as f:
#         f.write(text)
#     print("저장 완료")
#     # file = open("diary.txt", "w")
#     # file.write(input())
#     # file.close()
# def read_diary():
#     view = input("보고 싶은 다이어리의 날짜를 입력하세요(dd-mm-yyyy):")
#     try:
#         with open(f"{view}.txt", "r") as f:
#             res = f.read()
#         # file = open("diary.txt", "r")
#         print(res)
#     except FileNotFoundError:
#         print("해당 날짜의 다이어리를 찾을 수 없습니다.")
# while True:
#     menu()

#----------#

#pickle 모듈
#파이썬에 딕셔너리, 리스트, 클래스 - 자료구조, 객체 등을 자료형 변환 없이 그대로 파일에 저장하고 싶을 때 사용한다.
#인수가 여러 개일 때, 게시판(1.글번호 2.글제목 3.글내용)
import pickle
# data = {"no": 1, "title": "제목", "content": "내용"}
# # print(data["no"])
# with open('data.p', 'wb') as f:
#     pickle.dump(data, f)
    
# d = dict()
# with open('data.p', 'rb') as f:
#     d = pickle.load(f)
# print(d)

# import random
# win = 0
# games = 0
# while True:
#     a = int(input("1.가위, 2.바위, 3.보, 0.종료:"))
#     b = int(random.randrange(1,4))
#     if a == 1:
#         if b == 1:
#             games += 1
#         elif b == 2:
#             games += 1
#         elif b == 3:
#             win += 1
#             games += 1
#     elif a == 2:
#         if b == 1:
#             win += 1
#             games += 1
#         elif b == 2:
#             games += 1
#         elif b == 3:
#             games += 1
#     elif a == 3:
#         if b == 1:
#             games += 1
#         elif b == 2:
#             win += 1
#             games += 1
#         elif b == 3:
#             games += 1
#     with open('game.txt', "w") as f:
#         f.write(f"총 게임횟수: {games}, 승리횟수: {win}")
#     with open('game.txt', 'r') as f:
#         res = f.read()
#     print(res)
#     if a == 0:
#         break

#----------#

# def save(data, filename, next_id):
#     with open(filename, "wb") as db:
#         data = {'id':next_id,"이름":name, "수학":math, "과학":science, "영어":english}
#         pickle.dump(data, db)
# def load(filename):
#     try:
#         with open(filename, 'rb') as db:
#             data = pickle.load(db)
#             return data
#     except FileNotFoundError:
#         print("파일이 존재하지 않습니다.")
#         return []
#     except Exception as e:
#         print("데이터 로드 중 오류 발생", e)    
#         return []
# def add(data, name, math, science, english):
#     next_id = 1 if len(data)==0 else data[-1]['id']+1
#     data.append({'id':next_id,"이름":name, "수학":math, "과학":science, "영어":english})
#     return data
# def remove(data, c):
#     updated_data = [b for b in data if b['id']!=c]
#     return updated_data
# def printData(data):
#     for b in range(len(data)):
#         print(f"{data[b]['id']}, {data[b]['name']}, {data[b]['math']}, {data[b]['science']}, {data[b]['english']}")
# filename = 'scores.p'
# s = load(filename)
# while True:
#     a = int(input("메뉴를 선택해주세요. 1.입력, 2.조회, 3.삭제, 0.종료: "))
#     if a == 1:
#         name = input("이름: ")
#         math = (input("수학: "))
#         science = (input("과학: "))
#         english = (input("영어: "))
#         s = add(s, name, math, science, english)
#     elif a == 2:
#         printData(s)
#     elif a == 3:
#         c = int(input("삭제할 번호를 입력해주세요:"))
#         s = remove(s, c)
#         print("삭제되었습니다.")
#     elif a == 0:
#         save(s, filename)
#         print("종료되었습니다.")
#         break

#----------#

# def menu():
#     user = int(input("메뉴를 선택해주세요 (1-입력, 2-조회, 3-삭제, 0-종료):"))

#     if user == 1:
#         name = input("이름:")
#         math = input("수학:")
#         science = input("과학:")
#         english = input("영어:")
#         write_user(name, math, science, english)

#     elif user == 2:
#         load_user()

#     elif user == 3:
#         load_user()
#         delete = int(input("삭제할 번호를 입력해주세요 : "))
#         delete_user(delete)

#     elif user == 0:
#         print("종료되었습니다.")
#         return -1
#     return 0

# def write_user(name, math, science, english):
#     dic = {"이름":name, "수학":math, "과학": science, "영어": english}
#     lst = []
#     with open('data.p', 'rb') as f:
#         item = pickle.load(f)

#     if item != "":
#         if type(item) == dict:
#           lst.append(item)
#         elif type(item) == list:
#           lst += item

#     lst.append(dic)
#     with open('data.p', 'wb') as f:
#         pickle.dump(lst, f)
# def load_user():
#     with open('data.p', 'rb') as f:
#         data = pickle.load(f)

#     for i in range(len(data)):
#         # print(data[i])
#         print(f'[{i}] 이름 : {data[i]["이름"]}, 수학 : {data[i]["수학"]}, 과학 : {data[i]["과학"]}, 영어 : {data[i]["영어"]}')

# def delete_user(delete):
#     with open('data.p', 'rb') as f:
#         lst = pickle.load(f)

#     if delete < 0 or delete >= len(lst):
#         print("잘못된 입력입니다. 삭제할 수 없습니다.")
#         return

#     lst.pop(delete)

#     with open('data.p', 'wb') as f:
#         pickle.dump(lst, f)

#     print("삭제가 완료되었습니다.")

# try:
#     with open('data.p', 'rb') as f:
#         pickle.load(f)
# except:
#     with open('data.p', 'wb') as f:
#         pickle.dump("", f)

# while True:
#     if menu() == -1:
#         break







