#pattern printing problem for Alphabet C

#getting iput from the user no.of rows and columns
n=int(input("Enter no.of rows and columns:"))

#initialize for loop for creating C pattern 
for i in range(0,n):
    print("")
    for j in range(0,n):
        if (i==0 and j==0) or (i==n-1 and j==0):
            print(" ",end=" ")
        elif((i==0 or j==0 or i==n-1)):
            print("*",end=" ")
        else:
            print(" ",end=" ")