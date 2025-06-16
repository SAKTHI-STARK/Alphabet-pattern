#getting input from user for no.of rows and columns
n=int(input("enter no.of rows & columns:"))

#initialize for loop to print alphabet X
#here i represents row and j represents columns
for i in range(n):
    for j in range(n):
        if(i==j or i+j==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()