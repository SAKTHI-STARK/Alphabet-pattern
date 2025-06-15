#getting input from user for no.of rows & columns
n=int(input("Enter no.of rows & columns:"))

#initialize for loop to print alphabet O
# here i represents row and j represents column
for i in range(n):
    print()
    for j in range(n):
        if (i==j or (i==n-1 and j==0) or (j==n-1 and i==0)):
            print(" ",end=" ")
        elif(i==0 or j==0 or i==n-1 or j==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")