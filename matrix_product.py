n,m=map(int,input().split())
A=int(input())
mat=[]
for i in range(n):
    result=[]
    for j in range(m):
        d=int(input())
        ad=d*A
        result.append(ad)
    mat.append(result) 
print(mat) 