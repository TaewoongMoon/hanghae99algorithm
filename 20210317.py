# # 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!
# graph = {
#     1: [2, 5, 9],
#     2: [1, 3],
#     3: [2, 4],
#     4: [3],
#     5: [1, 6, 8],
#     6: [5, 7],
#     7: [6],
#     8: [5],
#     9: [1, 10],
#     10: [9]
# }
# visited = []

# #시작 노드(루트 노드)인 1부터 탐색합니다.
# #현재 방문한 노드를 visited_array에 추가합니다.
# #현재 방문한 노드와 인접한 노드중 방문하지 않는 노드에 방문합니다.
# def dfs_recursion(adjacent_graph, cur_node, visited_array):
#     visited_array.append(cur_node) #시작 노드 탐색

#     for adjacent_node in adjacent_graph[cur_node]: # 시작노드의 인접노드들을 다 불러와서
#         if adjacent_node not in visited_array: #인접노드중 하나가 visited array에 없다면 
#             dfs_recursion(adjacent_graph, adjacent_node, visited_array)  #dfs_recursion 함수를 불러서 다시한번 시작노드 탐색
#     return visited_array


# dfs_recursion(graph, 1, visited)  # 1 이 시작노드입니다!
# print(visited)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 이 출력되어야 합니다!


# # 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!
# graph = {
#     1: [2, 5, 9],
#     2: [1, 3],
#     3: [2, 4],
#     4: [3],
#     5: [1, 6, 8],
#     6: [5, 7],
#     7: [6],
#     8: [5],
#     9: [1, 10],
#     10: [9]
# }


# def dfs_stack(adjacent_graph, start_node):
#     stack = [start_node]
#     visited = []
#     while stack: #스택이 존재할때까지 계속해서 돌아간다
#         current_node = stack.pop() #current_node를 Stack 맨뒤에서 pop 한값을 가져온다.
#         if current_node not in visited: #current_node의 인접한 노드들이 visited에 없다면
#             visited.append(current_node) # visited에 붙여주고
#             stack.extend(sorted(adjacent_graph[current_node],reverse =True)) #붙인값들을 reverse 형태로 즉, 내림차순으로 sort하여서 리스트를 스택에 붙여라)
                
                
#     return visited



# print(dfs_stack(graph, 1))  # 1 이 시작노드입니다!
# # [1, 9, 10, 5, 8, 6, 7, 2, 3, 4] 이 출력되어야 합니다!

# 백준문제 1260번 - DFS와 BFS

# from collections import deque
# import sys

# def DFS(graph, start):
#     visited = []
#     stack = [start]

#     while stack:
#         current_node = stack.pop()
#         if current_node not in visited:
#             visited.append(current_node)
#             stack.extend(sorted(graph[current_node]), reverse= True) #LIFO - 역정렬해서 넣어줘야한다.
        
#     return visited
    
# def BFS(graph, start):
#     visited = []
#     queue = [start]

#     while queue:
#         current_node = queue.popleft()
#         if current_node not in visited:
#             visited.append(current_node)
#             queue.extend(sorted(graph[current_node])) #FIFO - 정렬해서 넣어줘야함

#     return visited

# N, M, V = map(int, sys.stdin.readline().split())
# graph = [set([]) for _ in range(N+1)]
# for _ in range(M):
#     a,b = map(int, sys.stdin.readline().split())
#     graph[a].add(b)
#     graph[b].add(a)
# N=4
# range(3,5)
# print(graph)
import sys
from collections import Counter

n = int(sys.stdin.readline())
s = []

for i in range(n):
    s.append(int(sys.stdin.readline()))
s.sort()


print(round(sum(s)/n))
print(s[n//2])

c = Counter(s).most_common()

if len(s) > 1:
    if c[0][1] == c[1][1]:
        print(c[1][0])
    else:
        print(c[0][0])
else:
    print(c[0][0])

print(max(s) - min(s))