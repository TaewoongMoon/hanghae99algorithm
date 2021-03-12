#1 -문제
i_card_number = input() #상근이 카드 갯수
i_card_list = list(map(int, input().split())) #상근이 카드 리스트
random_number = input() #랜덤한 카드 갯수
random_list = list(map(int, input().split())) #랜덤 카드 리스트
i_cardlist_set = set(i_card_list) #상근이 카드 리스트를 셋함수로 변환
i_random_set = set(random_list) #랜덤 카드 리스트를 셋함수를 변환
list_1_0 = [] #비어있는 리스트

difference_ = i_random_set - i_cardlist_set #겹치는 부분들을 제외한 나머지 원소들
for i in random_list: 
    if i not in difference_:
        list_1_0.append('1') #겹치는 원소들을 str(1)로 반환
    else:
        list_1_0.append('0') #겹치지 않는 원소들을 str(0)로 변환

print(' '.join(list_1_0)) #join 함수를 공백과 함께 이용해서 프린트 

#2 - 카드 순환 백준문제
from collections import deque
N = int(input())
card_list = deque(list(range(1, N+1)))

while len(card_list) != 1:
    del card_list[0]
    a = card_list.popleft()
    card_list.append(a)

print(*card_list)


#3
N = int(input())
empty_list = []

for i in range(N):
    number_ = int(input())
    empty_list.append(number_)
a = sorted(empty_list)

for i in a:
    print(i)


백준문제 - 1316, 그룹단어 체커
import sys

N = int(sys.stdin.readline()) #단어의 갯수
count = 0

for i in range(N):
    test_result = 0 #그룹단어인지 판별. 새로운 단어가 들어올때마다 0으로 update 해줘야함
    words = sys.stdin.readline().lower()
    for i in range(len(words)):
        if words.find(words[i], i+1) -i > 1:
            test_result = -1
            break
        else:
            test_result = 1 #i 를 다 도는동안 모든 조건이 다 break걸리지 않고 else문으로 넘어온다면 test_result 게속해서 1을 반환
    if test_result == 1:
        count +=1
    else:
        continue

print(count)

#백준문제-2839번, 설탕배달
import sys
N = int(sys.stdin.readline())

if N % 5 == 0: #5로 바로 나누어진다면 해당 몫을 반환하면 그게 봉지의 갯수
    print(N//5)

else:
    min_list = []   #봉지갯수 비교를 위한 리스트 생성
    threekg_bag = 1 #3kg짜리 가방을 1개부터 시작

    while N >= 3: 
        N -= 3   
        if N % 5 ==0:
            min_list.append(threekg_bag + N//5) #3kg짜리와 5kg짜리를 더해서 나온 봉지의 갯수를 리스트에 append
        
        threekg_bag +=1 #2 #3
    
    if len(min_list) == 0: #나누어지지 않았다면 -1반환
        print(-1)
    else:
        print(min(min_list)) #리스트중에 최소 봉지 갯수 반환

#백준문제 - 1011번, Fly me to the Alpha Centuari

import math
import sys
N = int(sys.stdin.readline())

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    distance = y -x    # 두 거리를 계산할 때 필요하다.
    count = 0 

    #해당문제는 거리의 제곱근 기준으로 최소 이동 횟수를 잡을 수 있다.
    trial_number = math.floor(math.sqrt(distance))  #거리의 제곱근을 구한다. 10이면 3과 4이인데 floor를 사용하여 3으로 반환
    trial_number_square = trial_number ** 2 #trial_number의 제곱수를 반환
    trial_plus_one = math.sqrt(trial_number_square) # 이동횟수를 +1해줄 최소 distance 움직임 수

    #거리에 따라서 나눈 구조
    if distance > trial_number_square + trial_plus_one:
        count = 2 * trial_number + 1
    elif distance > trial_number and distance <= trial_number_square + trial_plus_one:
        count = 2 * trial_number
    elif distance == trial_number_square:
        count = (2 * trial_number) -1
    elif distance < 4:
        count = distance

print(count)

#백준문제 - 4948번 , 베르트랑 공준문제

import sys
m = int(sys.stdin.readline())
n = (2*m)+1
numberof_prime = [True] * (n)
prime_list = []
for i in range(2, int(n**0.5)+1):
    if numberof_prime[i] == True:
        for j in range(2*i, n, i):
            numberof_prime[j] = False
for i in range(m+1, n):
    if i > 1 and numberof_prime[i] == True:
        prime_list.append(i)
print(len(prime_list))

#백준문제 - 1436번 (영화감독 숌)

n = int(input()) 
k, cnt = 666, 0   #처음 들어갈 K값과 카운트 = 0으로 만들어서 시작

while True:     #break가 걸릴때 까지 계속해서 진행하는 무한루프문
    if '666' in str(k): #666이라는 문자열이 str(k)안에 있다면 cnt +=1
        cnt +=1
    if cnt == n:  #입력한 input() 값과 같아질때 k값 반환
        print(k)
        break
    k +=1 #계속해서 마지막에 k를 1씩 더해준다
    





