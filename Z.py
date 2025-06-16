#getting input for no.of rows and columns
n=int(input("enter no.of rows & columns:"))

#initialize for loop to print alphabet Z
#here i represents rows and j represents columns
for i in range(n):
    for j in range(n):
        if(i==0 or i==n-1 or i+j==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()