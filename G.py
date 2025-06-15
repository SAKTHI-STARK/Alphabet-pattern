#getting rows and columns from the user
n=int(input("Enter number of rows & columns:"))

#initialize for loop to print albhabet G
for i in range(0,n):
    print("")
    for j in range(0,n):
        if (i==2 and j==1) or (i==3 and j==1) or (i==3 and j==3) or (i==4 and j==3) or (i==1 and j!=0):
            print(" ",end=" ")
        elif(i==0 or j==0 or i==4 or j==2 or i==2 or j==4):
            print("*",end=" ")
        else:
            print("*",end=" ")