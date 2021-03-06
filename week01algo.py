# -*- coding: utf-8 -*-
#3 - 45분이상, 45분미만, 그리고 시간이 0시일때 case로 나눠서 푸는 문제
h,m = input().split()
h = 0<=int(h)<=24
m = 0<=int(m)<=59
if m>44:
    print(h, m-45)
elif h>=1 and m<45:
    print(h-1, m+15)
else:
    print(23, m+15)


# 4 - 
num = int(input())
check_num = num
temp = 0
cycle_number = 0
while num!= check_num:
    temp = num//10 + num%10
    num = ((num%10)*10) + temp%10
    cycle_number += 1
print(cycle_number)

5. - 대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.
입력
첫째 줄에는 테스트 케이스의 개수 C가 주어진다.

둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고, 이어서 N명의 점수가 주어진다. 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.

출력
각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다.

예제 입력 1
5
5 50 50 70 80 100
7 100 95 90 80 70 60 50
3 70 90 80
3 70 90 81
9 100 99 98 97 96 95 94 93 91
예제 출력 1
40.000%
57.143%
33.333%
66.667%
55.556%

cases_ = int(input())
for i in range(cases_):
    k = list(map(int, input().split()))
    _average = (sum(k) - k[0]) / k[0]
    _count = 0
    for j in range(1, k[0]+1):
        if k[j] > _average:
            _count += 1
    print("{0:.3f}".format(_count/k[0]*100))

#6. 
문제
셀프 넘버는 1949년 인도 수학자 D.R. Kaprekar가 이름 붙였다. 양의 정수 n에 대해서 d(n)을 n과 n의 각 자리수를 더하는 함수라고 정의하자. 예를 들어, d(75) = 75+7+5 = 87이다.

양의 정수 n이 주어졌을 때, 이 수를 시작해서 n, d(n), d(d(n)), d(d(d(n))), ...과 같은 무한 수열을 만들 수 있다. 

예를 들어, 33으로 시작한다면 다음 수는 33 + 3 + 3 = 39이고, 그 다음 수는 39 + 3 + 9 = 51, 다음 수는 51 + 5 + 1 = 57이다. 이런식으로 다음과 같은 수열을 만들 수 있다.

33, 39, 51, 57, 69, 84, 96, 111, 114, 120, 123, 129, 141, ...

n을 d(n)의 생성자라고 한다. 위의 수열에서 33은 39의 생성자이고, 39는 51의 생성자, 51은 57의 생성자이다. 생성자가 한 개보다 많은 경우도 있다. 예를 들어, 101은 생성자가 2개(91과 100) 있다. 

생성자가 없는 숫자를 셀프 넘버라고 한다. 100보다 작은 셀프 넘버는 총 13개가 있다. 1, 3, 5, 7, 9, 20, 31, 42, 53, 64, 75, 86, 97

10000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

해당 문제는 String을 for문으로 돌렸을 때 값이 어떻게 나오는지 이해를 해야되는 부분이다.
items = 'bubblepop'
for i in items:
    print(j) -> # 'b','u','b', 'b', 'l', 'e', 'p', 'o', 'p'
list1 = list()
def d(N):
    for j in str(N):
        N+= int(j)
    list1.append(N)

for i in range(1,10000):
    d(i)
    if i not in list1:
        print(i)

#7
from collections import Counter
word = list(input().upper())
frequency = Counter(word)
result_ = []
for name_,number_ in frequency.items():
    if number_ == max(frequency.values()):
        result_.append(name_)

        if len(result_) > 1:
            break
if len(result_) == 1:
    print(result_[0])
else:
    print('?')

#8 replace함수를 사용하여 빠르게 풀 수 있는 문제...
croatia_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
croatia_text = input()
for i in croatia_list:
    croatia_text = croatia_text.replace(i, 'a')
print(len(croatia_text))