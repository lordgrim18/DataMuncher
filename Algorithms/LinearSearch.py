def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index of the target if found
    return -1  # Return -1 if the target is not in the array

# Get user input for the list of numbers
user_input = input("Enter a list of numbers separated by spaces: ")
my_list = [int(x) for x in user_input.split()]

# Get user input for the target value
target_value = int(input("Enter the target value to search for: "))
result = linear_search(my_list, target_value)

if result != -1:
    print(f"Target {target_value} found at index {result}")
else:
    print(f"Target {target_value} not found in the list")
