#getting input for rows & columns from user
n=int(input("Enter no.of rows & columns:"))

#initialize for loop for printing Alphabet L
#here i represents for rows & j represents columns
for i in range(n):
    for j in range(n):
        if(j==0 or i==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
