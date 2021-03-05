num = int(input())
check_num = num
new_num = 0
temp = 0
cycle_number = 0
try:
    while True:
        temp = num/10 + num%10
        new_num = ((num%10)*10) + temp%10
        cycle_number += 1
        num = new_num
        if new_num == check_num:
            break
    print(cycle_number)
except KeyboardInterrupt:
    print("keyboard error")