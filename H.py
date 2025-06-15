#getting input from user for no.of rows and columns
n=int(input("Enter no of rows and columns:"))

#initialize for loop for print the alphabet H
for i in range(n):
    print("")
    for j in range(n):
        if(
             j==0 or j==n-1 or i==n//2
        ):
            print("*",end=" ")
        else:
            print(" ",end=" ")