# You have a list of employees scheduled to work today and a list of employees who actually checked in.
# Write a function that returns the names of employees who didn’t check in.


def missing_employees(scheduled, checked_in):
    # Your code here
    pass

# Test the function
today_scheduled = {"Alice", "Bob", "Charlie", "David"}
today_checked_in = {"Alice", "Charlie"}
print(missing_employees(today_scheduled, today_checked_in)) # Expected output: {"Bob", "David"}
