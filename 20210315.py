
약수 - 1037번 백준문제
import sys

divisor_number = int(sys.stdin.readline())
divisor_list = list(map(int, sys.stdin.readline().split()))


value = max(divisor_list) * min(divisor_list)
print(value)


최대공약수와 최소공배수

import sys
n_1, n_2 = map(int, sys.stdin.readline().split())
n_1_list = []
n_2_list = []
overlapping_list = []
max_number = 1
for i in range(1,n_1+1):
    if n_1 % i == 0:
        n_1_list.append(i)

for i in range(1, n_2+1):
    if n_2 % i == 0:
        n_2_list.append(i)

for i in n_1_list:
    if i in n_2_list:
        overlapping_list.append(i)

max_number = max(overlapping_list)

value_1 = n_1 // max_number
value_2 = n_2 // max_number

min_number_multiply = value_1 * value_2 * max_number

print(max_number, min_number_multiply)

최소공배수 - 1934번
import sys
def gcd(x, y):
    while y:
        x,y = y,x%y #유클리드 호제법
    return x


def lcm(x, y):
    return x * y // gcd(x, y) 

test_case = int(sys.stdin.readline())
result = []

for _ in range(test_case):
    n1, n2 = map(int, sys.stdin.readline().split())
    gcd(n1, n2)
    lcm(n1, n2)
 
    result.append(lcm(n1,n2))


for i in result:
    print(i)

이항계수-1

import sys
import math

n, k = map(int, sys.stdin.readline().split())

result = math.factorial(n) / (math.factorial(k) * math.factorial(n-k))

print(int(result))

다리놓기

import sys
import math
result_list = []
test_case = int(sys.stdin.readline())
for _ in range(test_case):
    west_site, east_site = map(int, sys.stdin.readline().split())
    
    possible_numbers = math.factorial(east_site) / (math.factorial(west_site) * math.factorial(east_site-west_site))

    result_list.append(possible_numbers)

for i in result_list:
    print(int(i))



#ATM -  11399번
import sys
num_of_people = int(sys.stdin.readline())

time_list = list(map(int, sys.stdin.readline().split()))

final_list = (sorted(time_list))

duration_1 = 0
duration_2 = 0

for i in final_list:
        duration_1 += i
        duration_2 += duration_1
    
print(duration_2)


