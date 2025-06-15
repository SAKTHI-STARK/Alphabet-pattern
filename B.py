#develope a program to display Alphabet B

#getting the no.of rows and columns from the user
n=int(input("Enter no.of rows & columns:"))


#creating for loop to print pattern B
for i in range(0,n):
    print("")
    for j in range(0,n):
        #logic to print B using *
        """
        we only print * when row and column is 0 and row equal to middle 
        value and column equal to end value and then we need to prune when i==n-1 and j=n-1 and i==0 and i==middle value
        """
        if (i==0 or j==0 or i==n-1 or i==n//2) and j!=n-1:
            print("*",end=" ")
        elif(j==n-1 and i!=0 and i!=n-1 and i!=n//2):
            print("*",end=" ")
        else:
            print(" ",end=" ") 
