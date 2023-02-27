# [7]ATM
def solve(n):
    nums = [500,200,100,50,20,10]
    counter = 0
    while True:
        for i in nums:
            if n//i == 0:
                continue
            else:
                counter += (n//i)
                n -=i*(n//i)
                if n ==0:
                    return counter
            if 0<n<10:
                return -1
                
# [7]Halving Sum
def halving_sum(n):
    return 1 if n == 1 else sum([n//(2**i) for i in range(0, n//2) if n//(2**i) >=1])
