#gettig input from user for rows & columns
n=int(input("Enter no.of rows & columns:"))

#initialize for loop to print alphabet J
for i in range(n):
    for j in range(n):
        if(i==0 or j==n//2 or (i==n-1 and j<n//2)) or (j==0 and i>n//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()