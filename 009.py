import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt #MATHLAB - 파이썬보다 그래픽에 특화되있는 것
import matplotlib as mpl

mpl.rcParams['font.family'] = 'Malgun gothic'
mpl.rcParams['axes.unicode_minus'] = False

#데이터 생성
# x = np.linspace(0,10,100)
# y = np.sin(x)

#선그래프 생성
# plt.plot(x,y)

#그래프 꾸미기
# plt.title('sine graph')
# plt.xlabel("Time")
# plt.ylabel("sine of Time")

#그래프 출력
# plt.show()

#metplotlib - 가장 기본적인 데이터 시각화 라이브러리
#2D 그래프 특화 3D도 일부 가능
#선, 막대 그래프, 히스토그램, 산점도...
#seaborn - matplot 기반으로 고급 통계 차트

#데이터 생성
# x = [1,2,3,4]
# y1 = [2,4,6,8]
# y2 = [3,6,9,12]

#그래프꾸미기
# plt.plot(x, y1, 'r', label = '선그래프 1')
# plt.plot(x, y2, 'b--', label = '선그래프 2')
#범례 추가
# plt.legend()
#텍스트
# plt.text(2.5,7,"문자열 출력", fontsize=12)
#축 라벨
# plt.xlabel("x 축")
# plt.ylabel("y 축")
#제목 설정
# plt.title("제목")
#눈금설정
# plt.xticks([1,2,3,4])
# plt.yticks([0,5,10])
#격자 표시
# plt.grid(True)
#차트 꾸미기
# ax = plt.gca() #get current axes - 현재 활성화된 축 객체를 가져온다.
# ax.spines["top"].set_visible(False) 
# ax.spines["right"].set_visible(False)
# ax.spines["bottom"].set_visible(0.5)
# ax.spines["left"].set_visible(0.5)
# ax.tick_params(width=0.5)
#차트 출력
# plt.show()

#----------#

#산점도
# np.random.seed(100)
# x = np.random.normal(0, 1, 50)#평균이 0 표준편차 1 인 난수 50개
# y = np.random.normal(0, 1, 50)

# plt.scatter(x,y)
# plt.xlabel('X')
# plt.ylabel('Y')

# plt.title("Scatter Example")

# plt.show()

#----------#

df = pd.read_csv("seocho_people.csv")
# print(df)

def read_csv_file(file_path):
    data = []
    with open(file_path, mode = 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader) # 헤더 건너뛰기

        for row in reader:
            name, age, gender, address = row
            data.append((int(age), gender, address))
    return data

# print(read_csv_file('seocho_people.csv'))

#나이와 성별에 따른 산점도 그래프를 그리고
#성별 평균 나이 구해보기

# a = []
# b = []
# c = []
# d = []
# x = []
# y = []
# for i in range(len(read_csv_file('seocho_people.csv'))):
#     if read_csv_file('seocho_people.csv')[i][1]=='여성':
#         x.append(read_csv_file('seocho_people.csv')[i][1])
#         a.append(read_csv_file('seocho_people.csv')[i][2])
#         c.append(read_csv_file('seocho_people.csv')[i][0])
#     elif read_csv_file('seocho_people.csv')[i][1]=='남성':
#         y.append(read_csv_file('seocho_people.csv')[i][1])
#         b.append(read_csv_file('seocho_people.csv')[i][2])
#         d.append(read_csv_file('seocho_people.csv')[i][0])


# plt.figure(1)
# plt.scatter(b,d, c='b')
# plt.scatter(a,c, c='r')
# plt.xlabel('Address')
# plt.ylabel('Age')
# plt.title('산점도1')
# plt.legend(['남성','여성'])
# plt.show()

# plt.figure(2)
# plt.scatter(d,y, c='r' '0.9')
# plt.scatter(c,x, c='0.1')
# plt.xlabel('Age')
# plt.ylabel('Gender')
# plt.title('산점도2')
# plt.legend(['남성','여성'])
# plt.text(np.mean(c), '여성', "여성 평균 나이")
# plt.text(np.mean(d), '남성', '남성 평균 나이')
# plt.show()


# def create_scatter_plot(data):
#     coordinates_lst = [(age, 0 if gender == '남성' else 1) for age, gender, _ in data]
#     x_coords_lst, y_coords_lst = zip(*coordinates_lst)
#     plt.scatter(x_coords_lst,y_coords_lst, c=y_coords_lst, cmap=plt.get_cmap('tab20b'))
#     plt.yticks([0,1], ['남성','여성'])
#     plt.xlabel("Age")
#     # plt.ylabel()
#     plt.title("Age & Gender")
    
# def compare_age(data):
#     male_lst = [age for age,gender, _ in data if gender =='남성']
#     female_lst = [age for age,gender, _ in data if gender =='여성']
#     average_male = sum(male_lst)/len(male_lst)
#     average_female = sum(female_lst)/len(female_lst)
#     print(f"남성 평균 나이 : {average_male:.2f}")
#     print(f"여성 평균 나이 : {average_female:.2f}")
    
data_set = read_csv_file('seocho_people.csv')

# create_scatter_plot(data_set)
# plt.colorbar(label='gender')
# plt.show()

# compare_age(data_set)

# def create_scatter_plot(data):
#     coordinates_lst1 = [(age, address) for age, gender, address in data if gender =='남성']
#     coordinates_lst2 = [(age, address) for age, gender, address in data if gender =='여성']
#     x_coords_lst1, y_coords_lst1 = zip(*coordinates_lst1)
#     x_coords_lst2, y_coords_lst2 = zip(*coordinates_lst2)
#     plt.scatter(y_coords_lst1,x_coords_lst1, c='b')
#     plt.scatter(y_coords_lst2,x_coords_lst2, c='r')
#     plt.xlabel("Age")
#     plt.ylabel('Address')
#     plt.title("Age & Address")
# data_set = read_csv_file('seocho_people.csv')    

def create_scatter(data):
    address = sorted(set(address for _,_,address in data))
    address_xcoord = {}
    for idx, address in enumerate(address):
        address_xcoord[address] = 50 + (idx * 100)
    
    coord_lst = [(address_xcoord[address], age, 'blue' if gender == '남성' else 'red')
                for age, gender, address in data]
    
    x_coord_lst, y_coord_lst, colors = zip(*coord_lst)
    
    x_label = ['강남대로', '반포대로', '신반포로', '잠원로']
    x_position = [20000,40000,60000,80000]
    plt.xticks(x_position,x_label, rotation = 45)
    plt.scatter(x_coord_lst, y_coord_lst, color = colors, alpha = 0.5)
    plt.xlabel('주소')
    plt.ylabel('나이')
    plt.title('서초구 주민 인구 - 나이, 성별, 주소')
    
# create_scatter_plot(data_set)
create_scatter(data_set)
plt.show()

#상점 물건 판매량
# data = [
#     [50, 40, 30, 20, 60, 70, 80, 90, 100, 110, 120, 130],
#     [60, 50, 40, 30, 80, 90, 100, 110, 120, 130, 140, 150]
# ]
# def create_bar(data):
#     month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
#     index = np.arange(len(month))
#     sell_lst1 = [i for i in data[0]]
#     sell_lst2 = [i for i in data[1]]
#     plt.bar(index, sell_lst1, tick_label = month, color = 'orange', width = 0.3)
#     plt.bar(index+0.3, sell_lst2, tick_label = month, color = 'purple', width = 0.3)
#     plt.title('서초구 상점 물건 판매량')
#     plt.xlabel('월')
#     plt.ylabel('판매량')
#     plt.legend(['2022년','2023년'])
    
# create_bar(data)
# plt.show()
    
#----------#

# def create_bar_chrt(address, freq):
#     plt.bar(address, freq)
#     plt.xlabel('address')
#     plt.ylabel('freq')
#     plt.title("frequency")
    
# address = ['강남대로', '반포대로','신반포로', '장원로']
# freq = [50,30,20,40]

# create_bar_chrt(address, freq)
# plt.show()

#----------#

# import calendar

# month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
# print(calendar.calendar(2023))
# print(calendar.month(2023,8))
# print(calendar.weekday(2023,8,28))
# print(list(calendar.month_name[1:]))
# print(list(calendar.month_abbr[1:]))


#데이터 베이스
#데이터를 저장, 사용하기 위한 메모리 상자를 만들어서 사용해왔다.
#[변수]-[자료구조]-(함수)-(클래스)-(객체구조)-[텍스트 파일]-[csv]-[데이터베이스]
























