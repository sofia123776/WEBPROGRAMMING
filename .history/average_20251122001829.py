# Function to calculate sum and average of 5 units and provide feedback based on marks
def calculate_sum_and_average():
    numbers = []
    
    # Get 5 units of input from the user
    for i in range(5):
        while True:  # Loop until a valid number is entered
            try:
                num = float(input(f"Enter marks for student {i + 1}: "))
                if num < 0 or num > 100:
                    print("Please enter a valid mark between 0 and 100.")
                    continue
                numbers.append(num)
                break  # Exit the loop if input is valid
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    
    # Calculate sum and average
    total_sum = sum(numbers)
    average = total_sum / len(numbers) if numbers else 0  # Avoid division by zero
    
    # Output results
    print(f"Sum: {total_sum}")
    print(f"Average: {average}")
    
    # Feedback based on marks
    for i, mark in enumerate(numbers):
        if 80 <= mark < 100:
            result = "Outstanding"
        elif 60 <= mark < 80:
            result = "Credit"
        elif 40 <= mark < 60:
            result = "Pass"
        elif 20 <= mark < 40:
            result = "Fail"
        elif 0 <= mark < 20:
            result = "Go home and rest"
        else:
            result = "Invalid mark"
        
        print(f"Feedback for student {i + 1}: {result}")

# Call the function
calculate_sum_and_average()
