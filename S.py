#getting input form user for number of rows and columns
n=int(input("enter no.of rows & columns:"))

#initialize for loop to print pattebnmm,rn s
#here i represents row and column represent by j
for i in range(n):
    for j in range(n):
        if((j==0 and i>0 and i<n//2) 
            or 
        (i==0 and j>0)
            or
        (j>0 and i==n//2 and j<n-1)
            or
        (j==n-1 and i>n//2 and i<n-1)
            or
        (i==n-1 and j<n-1)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()