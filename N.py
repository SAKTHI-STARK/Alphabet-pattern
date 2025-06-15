#getting input from user for no.of rows & columns
n=int(input("Enter no.of row & columns:"))

#initializw for loop for loop to print N alphabet
#here I represents for row and j represents for column
for i in range(n):
    for j in range(n):
        if(j==0 or j==n-1 or i==j):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()