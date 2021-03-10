#스택 문제 - 균형잡힌 세상
while True:
    stk = []
    words = list(input())
    if len(words)==1 and words[0]=='.' : break

    for i in words:
        if i=='(' or i=='[' : stk.append(i)

        elif i == ')':
            if len(stk)>0 and stk[-1] =='(' : stk.pop()
            else: stk.append(i); break

        elif i == ']':
            if len(stk)>  0 and stk[-1] =='[' : stk.pop()
            else: stk.append(i); break

    if len(stk) == 0 : print('yes')
    else: print('no')

#수열 문제
n = int(input())
count = 1
stack = []
result = []
for i in range(1, n+1): #데이터 갯수만큼 반복
    data = int(input())
    while count <= data: #입력받은 데이터에 도달할때까지 stack 쌓고 count 증가
        stack.append(count)
        count += 1
        result.append('+')
    if data == stack[-1]:
        stack.pop()
        result.append('-')
    else:
        print('NO')
        exit(0) #프로그램 종료하는 방법
print('\n'.join(result)) #가능한경우 result를 반환하고 엔터 그리고 다음 result값을 반환하는 문자열 형태로 준다.

#돌아가는 큐
from collections import deque
#숫자크기, 뽑을숫자갯수
n, m = map(int, input().split())
#que 생성
queue = deque(list(range(1, n+1)))

#뽑아내는 위치 출력
pickNum = map(int,input().split())

#deque 함수들
count =0

for i in pickNum:
    index_number = queue.index(i) #뽑아내려고 하는 수의 위치
    if index_number < len(queue) - index_number:
        for _ in range(index_number):     #index_number직전 숫자들을 왼쪽에서 오른쪽으로 옮긴다
            queue.append(queue.popleft())
            count += 1
        queue.popleft()                 #옮기고 난 마지막 숫자를 pop()한다.
    else:
        for _ in range(len(queue) - index_number):
            queue.appendleft(queue.pop())
            count += 1
        queue.popleft()

print(count)
