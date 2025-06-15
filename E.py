#write a python program to print E
#getting the input from user for number of rows and columns
n=int(input("enter no.of rows & columns:"))


#initialize two for loops for i represents row and j for coumn
for i in range(0,n):
    print("")
    for j in range(0,n):
        if(i==0 or j==0 or i==n//2 or i==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")