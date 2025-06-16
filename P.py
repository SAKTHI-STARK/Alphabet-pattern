#getting input from user for rows and columns
n=int(input("enter no.of rows & columns:"))

#initialize for loop to print alphabet P
#here i represents for rows and column represents for columns
for i in range(n):
    for j in range(n):
        if (i==0 and j<n-1) or (j==0):#print * in first row without last value and print * in first column
            print("*",end=" ")
        elif(j==n-1 and i>0 and i<n//2) or (i==n//2 and j<n-1): #it print * on last column with prune first and mid value
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()