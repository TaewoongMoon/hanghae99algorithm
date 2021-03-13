Dynamic Programming - 동적계획법: 복잡한 문제를 간단한 여러개의 문제로 나누어 푸는 방법을 말한다.  
input = 20


def fibo_recursion(n):
    if n==1 or n==2:
        return 1 
    return fibo_recursion(n-1) * fibo_recursion(n-2)


print(fibo_recursion(input))  # 6765

input = 50

# memo 라는 변수에 Fibo(1)과 Fibo(2) 값을 저장해놨습니다!
fibo_memo = {
    1: 1,
    2: 1
}


def fibo_dynamic_programming(n, fibo_memo):
    if n in fibo_memo:
        return fibo_memo[n]
    
    nth_fibo = fibo_dynamic_programming(n-1, fibo_memo) + fibo_dynamic_programming(n-2, fibo_memo)
    fibo_memo[n] = nth_fibo
    return nth_fibo


print(fibo_dynamic_programming(input, fibo_memo))

백준문제 (9184번) - 신나는 함수 실행
fibo_memo = {}
def w(a,b,c):
    if (a,b,c) in fibo_memo:
        return fibo_memo[(a,b,c)]
    if a<= 0 or b<=0 or c<=0:
        fibo_memo[(a,b,c)] = 1
        return 1
    if a> 20 or b >20 or c> 20:
        return  w(20,20,20)
    if a<b and b<c:
        val = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        fibo_memo[(a,b,c)] = val
        return val
    else:
        val = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) -w(a-1, b-1, c-1)
        fibo_memo[(a,b,c)] = val
        return val

a, b, c = map(int,input().split())
while a != -1 or b != -1 or c != -1:
    print(f'w({a},{b},{c})= {w(a,b,c)}')
    a ,b, c = map(int, input().split())

백준문제 - 9461번 (파도반 수열) 
import sys
n = int(sys.stdin.readline())
triangle_memo = {1:1, 2:1, 3:1, 4:2, 5:2}
result = []
def triangle_dynamic_programming(n):
    if n in triangle_memo:
        return triangle_memo[n]
    
    nth_triangle = triangle_dynamic_programming(n-1) + triangle_dynamic_programming(n-5)
    triangle_memo[n] = nth_triangle
    return nth_triangle


for i in range(n):
    input_ = int(sys.stdin.readline())
    result.append(str(triangle_dynamic_programming(input_)))

print(' '.join(result))

#백준문제 - 1149번 (RGB거리)
N = int(input())
homes  =[]
for i in range(N):
    R,G,B = map(int, input().split())
    homes.append({'R':R, 'G':G, 'B':B})
dp=[homes[0]]
for i in range(1,N):
    dp.append({'R':homes[i]['R']+min(dp[-1]['G'],dp[-1]['B']),'G':homes[i]['G']+min(dp[-1]['B'],dp[-1]['R']), 'B':homes[i]['B']+min(dp[-1]['G'],dp[-1]['R']) })
print(min(dp[-1]['R'],dp[-1]['G'],dp[-1]['B'] ))


백준문제 - 1932번 (정수 삼각형)    
import sys
n = int(sys.stdin.readline())
dp_memo = [] 
for i in range(n):
    dp_memo.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, n):
    for j in range(len(dp_memo[i])):
        if j == 0:
            dp_memo[i][j] += dp_memo[i-1][j]
        elif j == len(dp_memo[i]) -1:
            dp_memo[i][j] += dp_memo[i-1][j-1]
        else:
            dp_memo[i][j] += max(dp_memo[i-1][j], dp_memo[i-1][j-1])

print(max(dp_memo[n-1]))
  

#백준문제 - 11047번 (동전 0)
import sys
type_number, value = map(int, sys.stdin.readline().split())
coin_list = [int(input()) for _ in range(type_number)] #input()함수를 통해 int 형태로 리스트로 묶어 정해진 범위만큼 입력할 수 있다.
total_coin_count = 0
coin_list.sort(reverse = True)
for coin in coin_list:
    coin_num = value // coin
    total_coin_count += coin_num
    value -= coin_num * coin

print(total_coin_count)



