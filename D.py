#write a program to Print the Albhabet D
#i love to do this program more than others

#getting input for the user for number of rows and columns
n=int(input("enter no.of rows & columns:"))


#initialize for loop to print the pattern D
for i in range(0,n):
    print("")
    for j in range(0,n):
        if ((i==0 and j==n-1) or (i==n-1 and j==n-1)):
            print(" ",end=" ")
        elif(i==0 or j==0 or i==n-1 or j==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        
