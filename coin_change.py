def countWays(arr,n,sum):
    if n==1:
        if sum%arr[0]==0:
            return 1
        else: 
            return 0
    if sum<0:
        return 0
    if sum==0:
        return 1
    include=countWays(arr,n,sum-arr[n])
    exclude=countWays(arr,n-1,sum)
    return include+exclude
 