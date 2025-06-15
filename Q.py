#getting input from user for no.of rows and columns
n=int(input("enter no.of rows and columns:"))

#initialize for loop for print Q pattern
#here i represents row and j represents column
for i in range(n):
    for j in range(n):
       if (i == 0 and j > 0 and j < n-1) or \
           (i == n-2 and j > 0 and j < n-1) or \
           (j == 0 and i > 0 and i < n-2) or \
           (j == n-1 and i > 0 and i < n-2) or \
           (i == j and i > n//2):
            print("*",end=" ")
       else:
           print(" ",end=" ")
    print()