# Function to get array input from the user
def get_array_input(prompt):
    return list(map(int, input(prompt).split()))

# Get input for the two arrays
array1 = get_array_input("Enter the elements of the first array separated by spaces: ")
array2 = get_array_input("Enter the elements of the second array separated by spaces: ")

# Merge using the '+' operator
merged_array = array1 + array2
print("Merged Array:", merged_array)