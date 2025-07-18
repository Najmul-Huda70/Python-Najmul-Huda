#Najmul Huda
from math import gcd
from functools import reduce
def solve():
    n=int(input())
    arr =list(map(int,input().split()))
    # is palindrome
    flag=True
    for i in range(n//2):
        if arr[i] != arr[n-i-1]:
            flag=False
            break
    if flag == True:
        print(0)
        return
    # not palindrome
    difference=[]
    for i in range(n//2):
        if arr[i]!=arr[n-i-1]:
            diff=abs(arr[i]-arr[n-i-1])
            difference.append(diff)
    # calculate all element gcd
    ans=reduce(gcd,difference)
    # Check palidrome condition
    for i in range(n // 2):
        if arr[i] % ans != arr[n - i - 1] % ans:
            ans = gcd(arr[i], arr[n - i - 1])
            if ans == 0:
                ans = 1 
            break
    
    print(ans)

    
#Testcase
t=int(input())
for _ in range(t):
    solve()