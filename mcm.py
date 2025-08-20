memotable=[[None for r in range(n) ]for r in range(n)]

def MatrixChain(arr,i=0,j=0):
    n=len(arr)
    if i+1==j:
        return 0
    elif i+2==j:
        return arr[i]*arr[i+1]*arr[j]
    res=float('inf')
    for k in range(i+1,j):
        res=min(res,MatrixChain(arr,i,k)+MatrixChain(arr,k,j)+arr[i]*arr[j]*arr[k])
    return res
    