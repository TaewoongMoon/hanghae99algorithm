import sys
memo = {
    "count_0_0" : 1,
    "count_0_1" : 0,
    "count_1_0" : 0,
    "count_1_1" : 1,
    0:0,
    1:1
}
def count_0_1_in_fibo(n,fibo_memo):
    if n == 0:
        return memo[0]
    elif n == 1:
        return memo[1]
    else:
        if n in memo:
            return memo[n]
        fibo_n = count_0_1_in_fibo(n-1,fibo_memo) + count_0_1_in_fibo(n-2,fibo_memo)
        memo[n] = fibo_n
        memo["count_"+str(n)+"_0"] = memo["count_"+str(n-1)+"_0"] + memo["count_"+str(n-2)+"_0"]
        memo["count_"+str(n)+"_1"] = memo["count_"+str(n-1)+"_1"] + memo["count_"+str(n-2)+"_1"]
    return fibo_n
num_tot = int(sys.stdin.readline())
num_test = []
for i in range(num_tot):
    num_fibo = int(sys.stdin.readline())
    num_test.append(num_fibo)
    count_0_1_in_fibo(num_fibo,memo)
for j in num_test:
    print(memo["count_"+str(j)+"_0"],memo["count_"+str(j)+"_1"])