def seven_checker(numbers):
  print("The list:", numbers)  # Print the list
  count = 0  # the counter for 7s
  for num in numbers:  # checks the list
      if num == 7:  # Check if the number is 7
          count += 1  
  print(f"The number 7 appears {count} times in the list.")

# Create a list with 10 numbers, including some 7s
my_list = [3, 7, 1, 9, 7, 4, 6, 7, 2, 8]

# Call the function with the list as an argument
seven_checker(my_list)
