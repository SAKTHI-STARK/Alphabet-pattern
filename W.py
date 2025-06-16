#getting input from user for no.of rows & columns
n=int(input("enter no.of rows & columns:"))

#initialize for loop to print alphabet V
#here i represents for rows and j represents column

for i in range(n):
    for j in range(n):
        if(j==0 or j==n-1 or (i==j and i>=n//2) or (i+j==n-1 and j<n//2)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()