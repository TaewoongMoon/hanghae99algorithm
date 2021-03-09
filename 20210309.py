#하노이의 탑 문제 해결하기
# def hanoi_top(n, start,  end,  middle):
#     if n == 1:
#         print(f'{start} {end}')
#         return
#     else:
#         hanoi_top(n-1,start, middle,end)
#         print(f'{start} {end}')
#         hanoi_top(n-1,middle, end, start)

# hanoi_top(3,1,3,2)

#정렬문제
num = int(input())
list1 = list()
for i in range(num):
    k = list(map(int, input().split()))
    list1.append(k)

final_list = sorted(list1, key = lambda x: (x[1], x[0]))
for i in final_list:
    x = i[0]
    y = i[1]
    print(x, y)

a = 11