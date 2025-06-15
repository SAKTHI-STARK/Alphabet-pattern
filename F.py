#geeting input from the user for rows and columns
n=int(input("Enter no.of Rows & columns:"))

#create a for loop for print alphabet F
for i in range(0,n):
    print("")
    for j in range(0,n):
        if(i==0 or j==0 or i==n//2):
            print("*", end=" ")
        else:
            print(" ",end=" ")