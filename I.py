#getting input from user for no.of rows and columns
n=int(input("Enter no.of rows and columns:"))

#initialize for loop to print alphabet I
for i in range(n):
    for j in range(n):
        if(i==0 or i==n-1 or j==n//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()