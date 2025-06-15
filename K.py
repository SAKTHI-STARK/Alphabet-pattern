#getting input from user for no.of rows and columns
n=int(input("Enter no.of rows & columns:"))
mid=n//2

#initialize for loop to print alphabet K
for i in range(n):
    for j in range(n):
        if(j==1 and i==n//2):
            print("*",end=" ")
        elif(j==0 or i+j==mid+1 or i-j==mid-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()