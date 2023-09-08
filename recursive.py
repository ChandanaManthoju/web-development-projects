





def square_rec(n, lst):
    if n >= 0:
        lst.append(n ** 2)
        square_rec(n - 1, lst)

# Create an empty list to store the calculated squares
squared_list = []

# Call the recursive function
square_rec(5, squared_list)

# Print the contents of the squared_list
print(squared_list)