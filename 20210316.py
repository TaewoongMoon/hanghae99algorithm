# 10828번 -백준문제 (스택)
# import sys
# def push(n):
#     list_.append(n)

# def pop():
#     try:
#         print(list_.pop())
    
#     except:
#         print(-1)

# def size():
#     return len(list_)


# def empty():
#     if size() == 0:
#         print(1)
    
#     else:
#         print(0)

# def top():
#     try:
#         print(list_[-1])

#     except:
#         print(-1)

# list_ = []

# command_number = int(sys.stdin.readline())

# for _ in range(command_number):
#     command_ = sys.stdin.readline()
    
#     if command_[0] == 'push':
#         push(command_[1])

#     elif command_[0] == 'pop':
#         pop()
    
#     elif command_[0] == 'size':
#         print(size())

#     elif command_[0] == 'empty':
#         empty()

#     elif command_[0] == 'top':
#         top()

#백준문제 10773번 - 제로

# import sys

# K = int(sys.stdin.readline())
# list_ = []
# for _ in range(K):
#     value = int(sys.stdin.readline())
#     if value == 0:
#         if len(list_) >= 1:
#             list_.pop()
    
#     else:
#         list_.append(value)

# print(sum(list_))

#백준문제 -9012번 (괄호)
# import sys

# N = int(sys.stdin.readline())
# vps_test =  []

# for _ in range(N):
#     vps_test.append(sys.stdin.readline())


# for i in vps_test:
#     vps = 0
#     for j in i:
#         if j == '(':
#             vps += 1

#         if j == ')':
#             vps -= 1
        
#         if vps <0:
#             break

#     if vps != 0:
#         print('NO')
    
#     else:
#         print('YES')


# 백준문제 18258번 - 큐2
import sys
#Class 만들어서 시도해보기
def push(n):
    command_list.append(n)

def pop():
    try:
        print(command_list.pop(0))
    except:
        print(-1)

def size():
    return len(command_list)

def empty():
    if size() == 0:
        print(1)
    
    else:
        print(0)

def front():
    try:
        print(command_list[0])

    except:
        print(-1)

def back():
    try:
        print(command_list[-1])
    
    except:
        print(-1)

command_num = int(sys.stdin.readline())
command_list = []

for _ in range(command_num):
    command_word = sys.stdin.readline().split()
    if command_word[0] == 'push':
        push(command_word[1])

    elif command_word[0] == 'pop':
        pop()

    elif command_word[0] == 'size':
        print(size())

    elif command_word[0] == 'empty':
        empty()
    
    elif command_word[0] == 'front':
        front()

    elif command_word[0] == 'back':
        back()



#스택을 이용한 DFS 방법
#1. 시작 노드를 스택에 넣습니다.
#2 현재 스택의 노드를 빼서 visted에 추가합니다.
#3 현재 방문한 노드와 인접한 노드중에서 


#DFS와 BFS - 1260번





#통계학 - 2108번
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

print(s[-1] - s[0])


#