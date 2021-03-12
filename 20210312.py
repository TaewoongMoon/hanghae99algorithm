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