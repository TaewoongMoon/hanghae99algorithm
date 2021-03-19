#수 찾기
import sys

N1 = int(sys.stdin.readline())
original_list = list(map(int, sys.stdin.readline().split()))
N2 = int(sys.stdin.readline())
comparing_list = list(map(int, sys.stdin.readline().split()))

for i in comparing_list:
    if i in original_list:
        print(1)
    else:
        print(0)

#이분법으로 푸는방법???
import sys
def binary_search(element, original_list, start= 0, end = None): #element = N2 리스트의 원소, original_list = N1의 리스트, 시작, 끝)
    if end == None:    # 처음 시작할때 None으로 선언해주기에 end = len(original_list) - 1을 해준다
        end = len(original_list) -1 
    if start > end: #start가 end보다 커지면 return 0
        return 0

    mid = (start + end) // 2 

    if element == original_list[mid]: # 원소가 original_list[mid] 와 같다면 return 1
        return 1
    elif element > original_list[mid]: # 원소가 더 크다면 start를 mid지점보다 +1해서 다시 비교
        start = mid + 1
    elif element < original_list[mid]: #원소가 더 작다면 end값을 mid지점보다 -1해서 다시 비교
        end = mid - 1
    
    return binary_search(element, original_list, start, end) #재귀함수 돌리기

N1 = int(sys.stdin.readline())
original_before_modified = list(map(int, sys.stdin.readline().split()))
original_list = sorted(original_before_modified) #이분탐색은 무조건 오름 또는 내림차순으로 정렬을 해줘야한다.

N2 = int(sys.stdin.readline())
comparing_list = list(map(int, sys.stdin.readline().split()))

for i in range(len(comparing_list)): #comparing list의 length만큼 돌면서 값 반환
    print(binary_search(comparing_list[i], original_list))



#백트래킹 N & M
import sys
N, M = map(int, sys.stdin.readline().split())

check = [False] * N

answer = [0] * M

def dfs(idx):
    if M == idx:
        for i in range(M):
            print(answer[i], end = ' ')
        print()
        return

    

    for i in range(N):
        if check[i]:
            continue

        check[i] = True
        answer[idx] = i+1


        dfs(idx+1)

        check[i] = False    

dfs(0)