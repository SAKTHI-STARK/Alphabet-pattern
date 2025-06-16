#getting input from user for no.of rows and columns
n=int(input("Enter no.of rows & columns:"))

#initialize for loop to print t
#here i represents row and j represent column
for i in range(n):
    for j in range(n):
        if(i==0 or j==n//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()