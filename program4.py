# highest number in the list( remember you need to remove the duplicates and than print the list ). 
# And try to do this question using two lists(one original
#  list that contains the numbers and another empty list with it )

def highest_number(numbers):
    unique_numbers = list(set(numbers))  # Remove duplicates
    max_number = max(unique_numbers) if unique_numbers else None  # Find the highest number
    return max_number, unique_numbers


numbers = [5, 2, 9, 5, 7, 2, 1, 9, 8]
max_number, unique_numbers = highest_number(numbers)

print("List without duplicates:", unique_numbers)
print("Highest number:", max_number)
