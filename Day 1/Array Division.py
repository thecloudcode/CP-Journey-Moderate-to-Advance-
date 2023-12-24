# CSES Problem : https://cses.fi/problemset/task/1085/

# You are given an array containing n positive integers.
# Your task is to divide the array into k subarrays so that the maximum sum in a subarray is as small as possible.

# Binary search problem
# Get all the possible sums as, from max(array) to sum(array) as this is all the possible sums of a sub array
# Now, in a function, if the target value can be achieved to be the maximum in all subarrays, we count how many sub arrays we actually need
# If in case we need less subarrays than k then we go towards left in Binary Search
# If we need more subarrays than k then we go towards right in Binary Search

def check (a,b,k):
    currsum = 0
    partitions = 1
    for i in a:
        if i+currsum>b:
            currsum=0
            partitions+=1
        currsum+=i
    return partitions<=k

n ,k = map(int,input().split())
x = list(map(int,input().split()))

s = max(x)
e = sum(x)
ans = -1

while(s<=e):
    mid = (s+e)//2
    if check(x,mid,k):
        ans = mid
        e-= 1
    else:
        s+= 1

print(ans)
