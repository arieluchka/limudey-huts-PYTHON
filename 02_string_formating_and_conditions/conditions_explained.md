# Conditions

We use conditions to **add logic** and to execute code **only when a condition is met**.
- if user input the correct password, then let him login
- if the list is empty, then don't print it.
- if you are under 18, then you are a minor
- if you received over 40 in the exam, then you passed

**To check for a condition:**
```python
if <True/False>:
	<rest of the code>
```

```python
if True:
	print("hello world")
```

```python
if True:
	stuff will happen
if False:
	stuff wont happen
```

**We can also use condition/function/method that return `True` / `False`** 

<br>
<br>

### Mathematical logical conditions


##### Equal `a == b`
```python
a = 5
b = 5

if a == b:
	print("a is equal to b!")
```

```python
user_password = input("please input your password: ")

if user_password == "qwerty123":
	print("welcome back User!")
```

##### Not equal `a != b`
```python
x = 10
y = 20

if x != y:
    print("x is not equal to y!")
```

```python
number = "24"

if type(number) != int:
    print("Sorry! thats not an integer")
```

##### Less than `a < b`
```python
age = 16

if age < 18:
    print("You are a minor!")
```

```python
names = ["ariel", "yoad", "andrey", "adam"]

if len(names) < 6:
    print("The list of names is shorter than 6!")
```

```python
password = "abc123"

if len(password) < 8:
    print("Your password is not long enought! it should be at least 8 chars!")
```
##### Less than/Equal to `a <= b`
```python
max_limit = 100
current_usage = 85

if current_usage <= max_limit:
    print("Within usage limit!")

```

```python
exam_score = 70
if exam_score <= 75:
    print("You passed, but there's room for improvement!")
```

##### Greater than `a > b`
```python
height = 180

if height > 170:
    print("You are taller than average!")
```

```python
speed = 90
if speed > 80:
    print("You're over the speed limit!")
```

##### Greater than/Equal to `a >= b`
```python
score = 85
passing_score = 80

if score >= passing_score:
    print("Congratulations, you passed the exam!")
```

```python
bank_balance = 1000
withdrawal_amount = 500

if bank_balance >= withdrawal_amount:
    print("You have sufficient balance to withdraw.")
```

### Using "in"
The `in` operator checks for membership. It’s used to **verify if an element exists** within a collection like a list, set, or dictionary.

*Check if an item is in a list*
```python
allowed_users = ["admin", "manager", "staff"]
user = "manager"

if user in allowed_users:
    print("Welcome to the system!")
```

*Check if a key is in a dictionary*
```python
user_roles = {"admin": 1, "manager": 2, "staff": 3}
role = "manager"

if role in user_roles:
    print("Role found in the system!")
```

*Check if a character exists in a string*
```python
message = "Hello, world!"
if "H" in message:
    print("The message starts with 'H'!")
```

### Using "is"
The `is` operator checks for object identity. It verifies if two variables refer to **the same object in memory.**

```python
a = [1, 2, 3]
b = a

if a is b:
    print("Both variables point to the same object!")
```

```python
result = None

if result is None:
    print("No result available!")
```

```python
status = True

if status is True:
    print("Operation was successful!")
```

#### `==` VS `is`
The `==` operator checks for value equality, while `is` checks if two variables refer to the same object.


```python
x = [1, 2, 3]
y = [1, 2, 3]
z = x

# Value equality
if x == y:
    print("x and y have the same value!")

# Identity equality
if x is z:
    print("x and z point to the same object!")
```
