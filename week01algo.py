3 - 45분이상, 45분미만, 그리고 시간이 0시일때 case로 나눠서 푸는 문제
h,m = input().split()
h = 0<=int(h)<=24
m = 0<=int(m)<=59
if m>44:
    print(h, m-45)
elif h>=1 and m<45:
    print(h-1, m+15)
else:
    print(23, m+15)


4 - 
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


