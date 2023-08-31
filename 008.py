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
# df = pd.DataFrame(data)
# df = df.sort_values('City')
# print(df)
# print(df['Age'].mean())
# print(df[df['Name']=='Peter']['Age'].values)
# oldest = df.loc[df['Age'].idxmax()]
# print(oldest[['Name','City']])

# 모든 사람의 이름을 대문자로 변경하기
# df['Name'] = df['Name'].str.upper()
# print(df)
# 나이가 30 이상인 사람들만 선택하기
# older_than_30 = df[df['Age']>=30]
# print(older_than_30)

# 각 도시별로 몇명이 살고 있는지 계산하기
# city_counts = df['City'].value_counts()
# print(city_counts)

# Gender라는 새로운 열을 추가해서 임의 성별 할당하기
# np.random.seed(0)
# df['Gender'] = np.random.choice(['Male', 'Female'], size=df.shape[0])
# print(df)

#----------#

# 1000명의 사람 데이터 만들기
# 이름 : Person_1, Person_2, ... Person_1000
# 나이 : 20 ~ 60 랜덤
# 도시 : 특정 도시에서 랜덤으로 할당 ex) New York, Paris, Berlin, London, Seoul, Tokyo
# np.random.seed(0)
# data = pd.DataFrame({
#     'Name': ['Person_' + str(i) for i in range(1, 1001)],
#     'Age': np.random.randint(20, 60, 1000),
#     'City': np.random.choice(["New York", "Paris", "Berlin", "London", "Seoul", 'Tokyo'], 1000)
# })

# print(data)
# 도시별 평균 나이 구하기
# average_age_per_city = data.groupby('City')['Age'].mean()
# print(average_age_per_city)

# 가장 많은 사람이 살고 있는 도시
# most_populated_city = data['City'].value_counts().idxmax()
# print(most_populated_city)

# 연봉 추가해서 랜덤으로 할당 ex) $50,000 ~ $150,000
# np.random.seed(0)
# data['Salary'] = np.random.randint(50000, 150000, size=data.shape[0])
# print(data.head())

# 연봉 순서대로 정렬한 후 연봉 1등과 꼴등 출력해보기
# print(data.loc[data['Salary'].idxmax()])
# print(data.loc[data['Salary'].idxmin()])

# data = data.sort_values('Salary')
# print(data.iloc[0])
# print(data.iloc[len(data)-1])

# print(data.head(1))
# print(data.tail(1))

# data = {
#     'Name':['John', 'Anna', 'Peter', 'Linda'],
#     'Age':[28,24,35,32],
#     'City':['New York', "Paris", "Berlin", "London"]
# }

# df = pd.DataFrame(data)
# df = df.sort_values('City', ascending=False)

# groupby : 데이터 특정 조건에 다라 그룹으로 분류하는 함수

# data = pd.DataFrame({
#     'City': ['Seoul', 'Seoul', 'Busan', 'Busan'],
#     'Fruit': ['Apple', 'Banana', 'Apple', 'Banana'],
#     'Quantity': [10, 15, 7, 12],
#     'Price': [1000, 2000, 1500, 2500]
# })

# group = data.groupby(['City','Fruit'])['Quantity'].sum()

# print(group)

#----------#

# 데이터 통합
# 여러개의 데이터셋을 결합해서 단일 데이터 셋으로 만든다.

# concat
# 동일한 열 이름을 가진 여러 데이터프레임을 행 방향(axis = 0)나 열 방향(axis = 1)로 결합할 때 사용한다.

# df1 = pd.DataFrame({'A':['A0','A1'], 'B':['B0', 'B1']})
# df2 = pd.DataFrame({'A':['A2','A3'], 'B':['B2', 'B3']})

# row = pd.concat([df1,df2], ignore_index=True)

# print(row)

# column = pd.concat([df1, df2], axis=1)

# print(column)

# merge
# 공통된 열 혹은 인덱스 기준으로 통합된다.

# df1 = pd.DataFrame({'Name':['John', 'Anna', 'Peter'], 'Age':[28,24,36]})
# df2 = pd.DataFrame({'Name':['John', 'Anna', 'Peter'], 'City':['New York','Paris','Seoul']})

# res = pd.merge(df1, df2, on='Name')
# print(res)

# join
# 인덱스 기반 결합 작업, 왼쪽으로 조인, how(내부inner, 외부outer, 왼쪽left, 오른쪽right)
# df1 = pd.DataFrame({'A':['A0', 'A1', 'A2']}, index=['I', 'J', 'K'])
# df2 = pd.DataFrame({'B':['B0', 'B1', 'B2']}, index=['I', 'J', 'K'])

# res = df1.join(df2)
# print(res)

# 1000명의 사람 데이터 만들기
# 1번 데이터셋
# ID : ID_1, ID_2, ... ID_1000
# 나이 : 20 ~ 60 랜덤
# 도시 : 특정 도시에서 랜덤으로 할당 ex) New York, Paris, Berlin, London, Seoul, Tokyo
# data1 = pd.DataFrame({
#     'ID': ['ID_' + str(i) for i in range(1, 1001)],
#     'Age': np.random.randint(20, 60, 1000),
#     'City' : np.random.choice(['New York', 'Paris', 'Berlin', 'London', 'Seoul', 'Tokyo'], 1000)
# })

# 2번 데이터셋
# ID : ID_1, ID_2, ... ID_1000
# 연봉 : 랜덤
# data2 = pd.DataFrame({
#     'ID': ['ID_' + str(i) for i in range(1, 1001)],
#     'Salary' : np.random.randint(50000, 150000, size=1000)
# })
    
# 3번 데이터셋
# 도시 : 특정 도시에서 랜덤으로 할당 ex) New York, Paris, Berlin, London, Seoul, Tokyo
# 나라 : 특정 도시의 나라 ex) USA, France, Germany, UK, Korea, Japan
# data3 = pd.DataFrame({
#     'City' : ['New York', 'Paris', 'Berlin', 'London', 'Seoul', 'Tokyo'],
#     'Nation' : ['USA', 'France', 'Germany', 'UK', 'Korea', 'Japan']
# })

# 1. 1번 데이터셋과 2번 데이터셋 병합 (ID 기준)
# merged_data = pd.merge(data1, data2, on='ID', how='outer')

# 2. 병합된 데이터에 City를 기준으로 병합
# final_data = pd.merge(merged_data, data3, on='City')
# print(final_data.head(5))
# print(final_data.tail(5))

# 3. 각 나라별 평균 연봉
# average_salary_per_nation = final_data.groupby('Nation')['Salary'].mean()
# print(average_salary_per_nation)

# 4. 제일 연봉이 높은 사람 어느 나라 사람인지?
# high_salary_person_nation = final_data.loc[final_data['Salary'].idxmax()]['Nation']
# print("Highest salary person's Nation : ", high_salary_person_nation)

# df = pd.read_csv("sample.csv")
# print(df)