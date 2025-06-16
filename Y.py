#getting input from user for no.of rows and columns
n=int(input("enter no.of rows & columns:"))

#initialize for loop to print alphabet Y
#i represent row and j represents column
for i in range(n):
    for j in range(n):
        if(j==n//2 and i>=n//2 or i==j and j<=n//2 or i+j==n-1 and j>=n//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()