#getting input from user for no.of rows & columns
n=int(input("enter no.of rows & columns:"))

#initialize for loop to print alphabet U
#here i represts row nd j represent columns
for i in range(n):
    for j in range(n):
        if(j==0 and i<=n-2 or i==n-1 and j>0 and j<n-1 or j==n-1 and i!=n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()