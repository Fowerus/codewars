# [6]Convert string to camel case
def to_camel_case(text):
    text = ' '.join(' '.join(text.split('-')).split('_')).split()
    return ''.join(text[0])+''.join(' '.join(text[1:]).title().split()) if len(text)>0 else ''
  
  # [6]Sum of Digits / Digital Root
def digital_root(n):
    n = sum([int(i) for i in str(n)])
    return [digital_root(n) if n > 9 else n][0]
  
  # [6]Is a number prime?
def is_prime(num):
    return len([num//i for i in range(1,abs(num)+1) if num//i == num/i])>2
  
  # [6]Find the unique number
def find_uniq(arr):
    arr.sort()
    if(arr[0] < arr[len(arr)-1] and arr[0] < arr[len(arr)-2]):
        num = arr[0]
    else:
        num = arr[len(arr)-1]
    return num
  
  # [6]No Order of Operations
def no_order(equation):
    try:
        equation = equation.replace('+', ')+')
        equation = equation.replace('-', ')-')
        equation = equation.replace('*', ')*')
        equation = equation.replace('/', ')//')
        equation = equation.replace('%', ')%')
        equation = equation.replace('^', ')**')
        equation = '('*equation.count(')')+equation
        equation = ''.join(equation.split())
        print(equation)
        return eval(''.join(equation.split()))
    except:
        return None
     
# [6]Multiplication table
def multiplication_table(size):
    return [[j * i for j in range(1, size + 1)] for i in range(1, size + 1)]

# [6]Are they the "same"?
def comp(array1, array2):
    if array2 is not None and arra1 is not None:
        for i in array2:
            for j in array1:
                if eval(str(i)) == j:
                    return True
    return False

# [6]Is a number prime?
import math
def is_prime(num):
    if num < 2: return False 
    for i in range(2, int(math.sqrt(num)) + 1):
        if (num % i == 0):
            return False
    return True
