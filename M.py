#getting input from user for rows & columns
n=int(input("Enter no.of rows & columns:"))

mid=n//2
#initialize for loop to print alphabet M
#here i represents row and j represents column
for i in range(n):
    for j in range(n):
        if (j==0 or j==n-1 or (i==j and j<=mid) or (i<mid and i+j==n-1)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()