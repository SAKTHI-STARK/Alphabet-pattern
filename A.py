#geting no of rows and columns from the user as input
n=int(input("Enter no.of Rows & Columns:"))

#creating loop using for
for i in range(0,n):
    print("")
    for j in range(0,n):
        if ((i==0 and j==0)#prune left top  
            or (i==0 and j==n-1)):#prune right top
            print(" ",end=" ")
        #logic to printing A pattern by using *
        elif i==0 or j==0 or i==(n//2) or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")