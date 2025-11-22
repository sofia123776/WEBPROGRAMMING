# Define a class for the stack
class Stack:
    def __init__(self):
        self.stack = []  # Initialize an empty list to represent the stack

    # Push operation: Add an element to the top of the stack
    def push(self, element):
        self.stack.append(element)
        print(f"{element} pushed to the stack.")

    # Pop operation: Remove the top element from the stack
    def pop(self):
        if not self.is_empty():
            element = self.stack.pop()
            print(f"{element} popped from the stack.")
            return element
        else:
            print("Stack is empty. Cannot pop an element.")
            return None

    # Peek operation: View the top element of the stack
    def peek(self):
        if not self.is_empty():
            print(f"The top element is: {self.stack[-1]}")
            return self.stack[-1]
        else:
            print("Stack is empty. No top element.")
            return None

    # Check if the stack is empty
    def is_empty(self):
        return len(self.stack) == 0

    # Display all elements in the stack
    def display(self):
        if not self.is_empty():
            print("Stack elements:", self.stack)
        else:
            print("Stack is empty.")

# Main program to demonstrate stack operations
if __name__ == "__main__":
    my_stack = Stack()

    # Perform stack operations
    my_stack.push(10)
    my_stack.push(20)
    my_stack.push(30)
    my_stack.display()
    my_stack.peek()
    my_stack.pop()
    my_stack.display()
    my_stack.pop()
    my_stack.pop()
    my_stack.pop()  # Attempt to pop from an empty stack


# Initialize an empty stack
stack = []

# Push operation
stack.append(10)
stack.append(20)
stack.append(30)

print("Stack after pushes:", stack)

# Peek operation
if stack:
    print("Top element:", stack[-1])

# Pop operation
if stack:
    popped = stack.pop()
    print("Popped element:", popped)
    print("Stack after pop:", stack)

# Is empty
print("Is stack empty?", len(stack) == 0)

# Size of the stack
print("Stack size:", len(stack))
