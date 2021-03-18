#2579번 - 계단오르기 (#dynamic programming)
# 아래에서 위에 오르는 방향으로 경우의 수를 생각하면 복잡해지기 때문에 아래에서 위로 떨어질때 어떤 경우의수들이 나올 수 있는지 생각해본다
# 1. 직전 계단 (n-1)을 밟고 연속 세계단을 밟을 수 없으니 전전 계단을 밟고 난후 나머지 d(i-3)값을 계산한 경우의 수
# 2. 전전 계단을 밟고 나머지 d(i-2) 값을 계산한 경우의수

#1과 2중 max값을 선택해서 반환
import sys
N = int(sys.stdin.readline())
score = [0]      #score를 받을 수 있는 리스트 생성. 0을 넣은 이유는 d[0]은 0번째 게단을 의미. 값이 없기때문에, 첫번째 계단부터 값을 받아주기 위해서 score.append(sys.stdin.readline())을 해준다.
d = [0] *301     #마찬가지로 d[0]은 존재하지않는다. 그렇기 때문에 [0]안에 있는 원소를 300개 대신 301개를 만들어준다.

for _ in range(N):
    score.append(int(sys.stdin.readline())) #입력값을 순서대로 받아서 (첫번째 계단 value, 두번째 계단 value) score값에다가 append시켜준다

if N > 0:  
    d[1] = score[1] # N>0보다 크다면 즉, d[1] = score[1]. 첫계단을 밟는데 경우의 수는 없다

if N > 1:
    d[2] = score[1] +score[2] #N> 1보다 크고 d[2]값을 찾는다면 max-score는 무조건 첫번째 계단 두번째 계단 둘다 밟는것이다. 그렇기 때문에 d[2] = score[1] + score[2]로 식을 세울 수 있다.

for i in range(3, N+1):
    d[i] = max(score[i] + score[i-1]+ d[i-3], score[i] + d[i-2]) #dynamic programming 활용, d[1] & d[2] 값을 기억해서 반환, 재귀문제(?)


print(d[N])

#가장 긴 바이토닉 수열 - dynamic programming
import sys
N = int(sys.stdin.readline()) 
num = list(map(int, sys.stdin.readline().split())) 
#증가하는 수열을보고 싶은데 증가하는 수열의 길이를 알아보자

dp = [0] * N #N 길이만큼 increasing list들 검사. 그렇게 해서 만약에 길이가 늘어난다면 array가 증가하겠지만, 그렇지 않다면 [1,2,3,3,3] 이런식으로 머물게 된다.
dp_ = [0] * N #N 길이만큼 decreasing list를 검사
res = 0 

for i in range(N): # i = 0 을 제외하고 1부터 하나씩 비교하는 for문 i=2
    for j in range(i):
        if num[i] > num[j] and dp[i] < dp[j]: #i값이 j보다 크고 dp[i] 인덱스 값이 dp[j] 인덱스 값보다 작으면 dp[i] = dp[j]로 하는 구조.
            dp[i] = dp[j] 
    dp[i] += 1 #for문을 다돌고 난 이후에 dp[i] 번째에 무조건 1을 더해준다. 만약에 더 큰값이 없다면 해당 인덱스는 그 전 수열길이 값을 가져오는 구조이다.


for i in range(N-1, -1, -1): #reverse 를 위에 for문와 똑같이 실행
    for j in range(N-1, i, -1):
        if num[i] > num[j] and dp_[i] < dp_[j]:
            dp_[i] = dp_[j]
    dp_[i] += 1

for i in range(N):
    res = max(res, dp[i] + dp_[i] -1) #중간에 기준점이 똑같기 때문에 나온값에 -1을 해준다

print(res)

#2798번 - 블랙잭
import sys
N, M = map(int, sys.stdin.readline().split())
number_list = list(map(int, sys.stdin.readline().split()))

temp_number = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if number_list[i] + number_list[j] + number_list[k] > M:
                continue
            else:
                temp_number = max(temp_number, number_list[i]+number_list[j] + number_list[k])

print(temp_number)


# 쿼드트리 - 1992번
from sys import stdin

input = stdin.readline


def making_colored_paper(n, cp, x, y):
    if n == 1:
        return cp[x][y]

    cp1 = making_colored_paper(n // 2, cp, x, y)
    cp2 = making_colored_paper(n // 2, cp, x, y + n // 2)
    cp3 = making_colored_paper(n // 2, cp, x + n // 2, y)
    cp4 = making_colored_paper(n // 2, cp, x + n // 2, y + n // 2)

    if cp1 == cp2 == cp3 == cp4 and len(cp1) == 1:
        return cp1

    return f'({cp1}{cp2}{cp3}{cp4})'

if __name__ == "__main__":
    N = int(input())
    paper = [list(input().rstrip()) for _ in range(N)]
    res = making_colored_paper(N, paper, 0, 0)
    print(paper)