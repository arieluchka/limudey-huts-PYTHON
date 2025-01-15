# Loops Explained

In Python, loops are used to repeatedly execute a block of code until a certain condition is met. They are an essential part of programming and allow us to automate repetitive tasks.

## Types of Loops

Python provides two types of loops: `for` loops and `while` loops.

### For Loops

A `for` loop is used to iterate over a sequence (such as a list, tuple, or string) or other iterable objects. It allows us to perform a set of actions for each item in the sequence.

Here's the general syntax of a `for` loop:

```python
for item in sequence:
    # code to be executed
```

In each iteration, the `item` variable takes the value of the next item in the sequence. The code inside the loop is executed for each item.

Here are three examples of `for` loops:

1. Iterating over a list:
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

2. Iterating over a string:
```python
message = "Hello, world!"
for char in message:
    print(char)
```

3. Iterating over a range of numbers:
```python
for i in range(1, 5):
    print(i)
```

### While Loops

A `while` loop is used to repeatedly execute a block of code as long as a certain condition is true. It allows us to perform actions until the condition becomes false.

Here's the general syntax of a `while` loop:

```python
while condition:
    # code to be executed
```

The code inside the loop is executed as long as the `condition` remains true. It's important to ensure that the condition eventually becomes false, otherwise, the loop will continue indefinitely.

Here are three examples of `while` loops:

1. Counting down from 10:
```python
count = 10
while count > 0:
    print(count)
    count -= 1
```

2. Reading user input until a specific value is entered:
```python
user_input = ""
while user_input != "quit":
    user_input = input("Enter a value (or 'quit' to exit): ")
    print("You entered:", user_input)
```


## Loop Control Statements

### Break 

The `break` statement is used to exit the loop prematurely. When encountered, **it immediately terminates the loop** and transfers control to the next statement after the loop.

```python
for item in sequence:
    if condition:
        break
    # code to be executed
```

### Continue 

The `continue` statement is used to **skip** the rest of the code inside the loop for the current iteration **and move to the next iteration.**

```python
for item in sequence:
    if condition:
        continue
    # code to be executed
```

### Pass 

The `pass` statement is used as a placeholder when a statement is required syntactically but no action is needed.

```python
for item in sequence:
    if condition:
        pass
    # code to be executed
```

The `pass` statement allows us to write empty loops or placeholders for future code.
