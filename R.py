#getting input from user for rows and columns
n=int(input("Enter no.of rows & columns:"))

#initiialize for loop for print alphabet R
#here i represents row and j represents column
for i in range(n):
    for j in range(n):
        if(j==0 or i==0 and j<n-1) or (i-j==2):
            print("*",end=" ")
        elif(i==n//2 and j<n-1) or j==n-1 and i>0 and i<n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()