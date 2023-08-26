# read() : 파일의 전체 내용을 문자열로 반환
# readline() : 파일에서 한 줄씩 문자열로 읽어옵니다.
# readlines() : 파일의 전체 내용을 한 줄씩 읽어와서 각각 리스트로 만들어서 반환

# with open("alice.txt", "r") as f:
#     line = f.readline()

#     while line:
#         # print(line.strip()) #print(line, end="")
#         line = f.readline()

# with open("alice.txt", "r") as f:
#     line = f.readlines()
#     for i in line:
#         print(i.strip())
#     print(len(line))

# 모드
# "r" : 읽기 모드
# "w" : 쓰기 모드 (이전에 데이터를 모두 삭제하고 새로 적는다.)
# "x" : 생성 모드 (파일을 생성해주는 모드, 이미 파일이 있으면 에러)
# "a" : 추가 모드 (파일에 데이터를 추가하기 위해 사용된다. 해당 파일이 이미 존재한다면, 기존의 데이터 뒤에 새로운 데이터를 추가한다.)
# "b" : 바이너리 모드 (바이너리 데이터를 사용하기 위해)
# "t" : 텍스트 모드 (텍스트 데이터를 다루기 위해 사용됨. (기본값)) 생략가능.
# "r+" : 파일 읽기 쓰기를 모두 사용할 수 있는 모드
# "rb" : 읽기 모드
# "wb" : 쓰기 모드
# "ab" : 추가 모드
# "xtb" : 생성 모드
# "rb+", "wb+", "ab+" : 읽기 쓰기 모드

#----------#

# Pandas
# 데이터 분석 및 조작을 위한 라이브러리 (Numpy 기반)
import numpy as np
import pandas as pd

# Series : 1차원 배열 구조
# DataFrame : 2차원 배열 구조

# CSV, Excel, SQL 쿼리

# Series
# s = pd.Series([1,3,4, np.nan, 6, 8])
# print(s)
# print(s[3])

# s = pd.Series([1,3,4, np.nan, 6,8], index=['A','B','C','D','E', 'F'])
# print(s)
# print(s['C'])

# # DataFrame
# data = {
#     'Name':['짱구', '철수', '훈이'],
#     'Age':[5,5,5]
# }

# df = pd.DataFrame(data)

# print(df)
# print('----------------------')
# print(df['Name'])
# print('----------------------')
# print(df.loc[0]) # 이름
# print('----------------------')
# print(df.iloc[0]) # 위치

#----------#

data = {
    'Name':['John', 'Anna', 'Peter', 'Linda'],
    'Age':[28,24,35,32],
    'City':['New York', "Paris", "Berlin", "London"]
}

# 1. 도시 기준으로 정렬
# 2. 평균 나이 구하기
# 3. 이름이 Peter인 사람의 나이 출력
# 4. 가장 나이가 많은 사람이 살고 있는 이름, 도시 출력해보기
df = pd.DataFrame(data)
df = df.sort_values('City')
print(df)
print(df['Age'].mean())
print(df[df['Name']=='Peter']['Age'].values)
oldest = df.loc[df['Age'].idxmax()]
print(oldest[['Name','City']])

# 모든 사람의 이름을 대문자로 변경하기
df['Name'] = df['Name'].str.upper()
print(df)
# 나이가 30 이상인 사람들만 선택하기
older_than_30 = df[df['Age']>=30]
print(older_than_30)

# 각 도시별로 몇명이 살고 있는지 계산하기
city_counts = df['City'].value_counts()
print(city_counts)

# Gender라는 새로운 열을 추가해서 임의 성별 할당하기
np.random.seed(0)
df['Gender'] = np.random.choice(['Male', 'Female'], size=df.shape[0])
print(df)
