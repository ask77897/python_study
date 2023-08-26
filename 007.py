#alice.txt에서 
#1. 단어가 총 몇개 있는지 - 2145
#2. 어떤 단어가 있는지, 각 단어가 몇 개씩 있는지

# with open('alice.txt', 'r') as f:
#     contents = f.read() 
    
# print(contents)
# con = contents.replace("\n\n", " ")
# con1 = con.replace("\n", " ")
# a = list(con1.split(" "))
# print(a)
# print(len(a))

# 구두점 제거
# punctuations = '''!()_[]{};:'"\,<>./?@#$%^&*-~'''
# for punctuations in punctuations:
#     contents = contents.replace(punctuations, "")
# content = contents.replace("\n", " ")
# print(content.split())
# print(len(contents.split()))
# c = contents.lower()
# words = c.split()

#각 단어 갯수 계산
# word_count = {}
# for word in words:
#     if word in word_count:
#         word_count[word] += 1
#     else:
#         word_count[word] =1

#단어 갯수 출력
# for word, count in word_count.items():
#     print(f"({word}:{count})")
    

#----------#

#Numpy(Numberical Python)
#과학, 공학 연산을 쉽게 하도록 지원하는 다차원 배열(multi-dimensional arry) 라이브러리
#Numpy를 사용해서 대규모 배열 처리를 쉽게 하도록 하고, 파이썬 List 와는 차이가 있다.

import numpy as np

# a = np.array([1,2,3,4,5])
# b = np.array(([1,2,3],[4,5,6]))

# print(a)
# print(b)

#내부에 연속된 메모리 구조를 가지고 (Array Interface)를 가지고 있고
#C를 통해 연산된다.

#생성 함수 : np.array(), np.zeros(), np.ones(), np.empty(), np.arange(), np.linspace()
#변환 함수 : ndarray.reshape(), ndarray.revel(), ndarray.transpose(), ndarray.swapaxes()
#연산 함수 : np.add(), np.substract(), np.multyply(), np.divide(), np.sqrt(), np.dot
#           np.mean(), np.std(), np.max(), np.min(), np.argmax(), np.argmin()
#집계 함수 : ndarray.sum(), ndarray.mean(), ndarray.std(), ndarray.max(), ndarray.min()
#           ndarray.argmax(), ndarray.argmin()
#논리 함수 : np.logical_and(), np.logical_or(), np.logical_not()

#생성 함수
# arr1 = np.zeros(5)
# print(arr1)

# arr2 = np.zeros((21,81))
# print(arr2)

# arr3 = np.zeros((3,3,3))
# print(arr3)

# arr1 = np.ones(5)
# print(arr1)

# arr2 = np.ones((10,10))
# print(arr2)

# arr3 = np.empty(5)
# print(arr3)

# arr4 = np.empty((3,3))
# print(arr4)

# arr1 = np.arange(5)
# print(arr1)

# arr2 = np.arange(3,10)
# print(arr2)

# arr3 = np.arange(1,10,0.2)
# print(arr3)

# arr1 = np.linspace(0,1,5)
# print(arr1)

# arr2 = np.linspace(-10, 10, 10)
# print(arr2)

#변환 함수
#배열 형태 변환

# arr1 = np.array([1,2,3,4,5,6])
# arr2 = arr1.reshape(2,3)
# print(arr2)

# arr3 = arr2.flatten()
# print(arr3)

#타입 변환
#정수를 실수로
# arr_int = np.array([1,2,3])
# arr_float = arr_int.astype(float)
# print(arr_float)

# arr_str = np.array(['1','2','3'])
# arr_int1 = arr_str.astype(int)
# print(arr_int1)

#축 변환
# b = np.array([[1,2],[3,4],[5,6]])
# trans = b.transpose()
# print(trans)

# print(np.transpose(trans))

#집계 함수
# b = np.array([[1,2],[3,4],[5,6]])
# print(b.sum())
# print(b.mean())
# print(b.std())
# print(b.max())
# print(b.min())
# print(b.argmax())
# print(b.argmin())

#논리 함수
# arr1 = np.array([True, False, False, True])
# arr2 = np.array([True, True, False, False])

# print(np.logical_and(arr1, arr2))
# print(np.logical_or(arr1, arr2))
# print(np.logical_not(arr1))
# print(np.logical_not(arr2))

#----------#

#2차원 배열에서 각 행과 각 열의 합을 구하여 리스트로 반환해보기

# arr1 = np.array(([1,2,3],[4,5,6],[7,8,9]))
# print(arr1[0],arr1[1],arr1[2])

# arr2 = []
# for i in range(len(arr1)):#for i in arr1
#     arr2.append(arr1[i].sum())
# print(arr2)

# arr3 = []
# for i in range(len(arr1)):#for i in arr1.transpose()
#     a = np.transpose(arr1)
#     arr3.append(a[i].sum())#(i.sum())
# print(arr3)

# print(arr1.sum(axis=None))
# print(arr1.sum(axis=0))#x축
# print(arr1.sum(axis=1))#y축


# arr1 = (np.random.rand(3,3))
# print(arr1)
# print(np.sort(arr1))

#10*10 배열에서 서로 다른 두 원소를 선택해서
#두 원소의 차이의 절대값이 가장 작은 두 원소를 찾아보기
# arr = np.random.rand(10,10)
# arr = arr.flatten()
# print(arr.max() - arr.min())
# sorted_arr = np.sort(arr)

# print(sorted_arr)
# print(sorted_arr[sorted_arr.argmax()] - sorted_arr[sorted_arr.argmin()])

# min = sorted_arr[sorted_arr.argmax()] - sorted_arr[sorted_arr.argmin()]
# min_index = 0
# for i in range(len(sorted_arr)-1):
#     diff = abs(sorted_arr[i] - sorted_arr[i+1])

#     if diff < 0:
#         diff *= -1

#     if diff < min:
#         min = diff
#         min_index = i

# print(f"첫번째 원소 : {sorted_arr[min_index]}, 두번째 원소 : {sorted_arr[min_index+1]}, 최소값 : {min}")





