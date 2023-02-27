# [5]Pete, the baker
def cakes(recipe, available):
    count = []
    for i,u in recipe.items():
        count.extend([math.floor(h/u) for j,h in available.items() if i == j])
    return min(count) if len(count) == len(recipe) else 0
  
  # [5]Maximum subarray sum
def max_sequence(arr):
    current = 0
    biggest = 0
    for i in arr:
        current +=i
        if current < 0:
            current = 0
        if current > biggest:
            biggest = current
    return biggest
  
  # [5]Square Matrix Multiplication
def matrix_mult(a, b):
    new = []
    for i in range(len(a)):
        new_row = []
        for j in range(len(b)):
            s = sum([a[i][k] * b[k][j] for k in range(len(b[j]))])
            new_row.append(s)
        new.append(new_row)
    return new

# [5]Directions Reduction
def dirReduc(arr):
    dict = {"NORTH":"SOUTH","SOUTH":"NORTH","EAST":"WEST","WEST":"EAST"}
    res = []
    for i in arr:
        if res and dict[i] == res[-1]:
            res.pop()
        else:
            res.append(i)
    return res

# [5]Primes in numbers
def primeFactors(n):
    i = 2
    res = {}
    while n/i != 1:
        if n%i == 0:
            if i in res:
                res[i] = res[i]+1
            else:
                res[i] = 1
            n = n/i
        else:
            i+=1
            
    if i in res:
        res[i] = res[i]+1
    else:
        res[i] = 1
    t = ''
    res = sorted(res.items(),key = lambda a:a[0])

    for key in res:
        if key[1] == 1:
            t = t + '('+str(key[0]) +')'
        else:
            t = t + '(' +str(key[0]) + '**' + str(key[1]) + ')'
    return t
