#getting input from user for no.of rows and columns
n=int(input("enter no.of rows:"))

#initialize for loop to print alphabet v
#here i represents row and j represents column
for i in range(n):
    for j in range(n*2-1):
        if(
            i==j or i+j==n*2-2
        ):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()