#Najmul Huda
#sorted 
def isSorted(arr, n):
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            return False
    return True
def called_1(n):
    print(n-2)
    i = 1
    while i <= n-2:  
        print(f'{i} {n-1} {n}')
        i += 1

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    if arr[n-2]>arr[n-1]:
        print(-1)
    elif  arr[n-1]>=0:
        called_1(n)
    else:
        if isSorted(arr,n) is True:
            print(0)
        else:
            print(-1)


# Test cases
t = int(input())
for _ in range(t):
    solve()