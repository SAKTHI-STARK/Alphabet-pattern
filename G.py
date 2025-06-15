#getting input for no.of rows and columns from the user
n = int(input("Enter an odd number (>=5) for rows & columns: "))

if n < 5 or n % 2 == 0:
    print("Please enter an odd number >= 5.")
else:
    for i in range(n):
        for j in range(n):
            if (
                i == 0 or                        # Top bar
                i == n-1 or                      # Bottom bar
                j == 0 or                        # Left bar
                (i >= n//2 and j == n-1) or      # Lower-right vertical
                (i == n//2 and j >= n//2)        # Middle bar to right
            ):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
