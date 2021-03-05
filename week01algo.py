# #3
# h,m = input().split()
# h = 0<=int(h)<=24
# m = 0<=int(m)<=59
# if m>44:
#     print(h, m-45)
# elif h>=1 and m<45:
#     print(h-1, m+15)
# else:
#     print(23, m+15)


#4
num = int(input())
check_num = num
temp = 0
cycle_number = 0
while num!= check_num:
    temp = num//10 + num%10
    num = ((num%10)*10) + temp%10
    cycle_number += 1
print(cycle_number)





