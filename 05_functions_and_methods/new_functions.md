## Functions

Function are like python "blueprints", that let you create a re-usable piece of code, which you can execute from anywhere.

Functions are like individual "lego blocks", and combining those together helps us build readable, reusable and easy to work with code.

### Syntax
#### Basics
function are defined using `def <function_name>():`
```python
def print_hello():
    print("hello world!")
```

After defining a new function, we can call it by using its name:
```python
print_hello()

# OUTPUT
# hello world!
```

#### Input/Output
We can set input arguments/parameters that need to be passed to the function, in order for it to work.

**Example 1**
```python
def greet(user_name):
    print(f"hello {user_name}!")
```

```python
greet("Ariel")

greet("Yoram")


# OUTPUT
# hello Ariel!
# hello Yoram!
```

**Example 2**
```python
def odd_or_even(user_num):
    if (user_num % 2) == 0:
        print(f"The number {user_num} is even")
    else:
        print(f"The number {user_num} is odd")
```

```python
odd_or_even(9)
odd_or_even(20)
odd_or_even(user_num=31)  # We can specify the argument name


# OUTPUT
# The number 9 is odd
# The number 20 is even
# # The number 31 is odd
```

**Example 3**

We can define/pass multiple arguments
```python
def calculate_sum(num1, num2):
    sum_result = num1 + num2
    print(f"The sum of {num1} and {num2} is {sum_result}")
```

```python
calculate_sum(5, 10)
calculate_sum(num1=2, num2=8)  # We can specify the argument names
calculate_sum(num2=7, num1=3)  # When we specify the argument name explicitly, we don't need to keep the order.

# OUTPUT
# The sum of 5 and 10 is 15
# The sum of 2 and 8 is 10
# The sum of 3 and 7 is 10
```

**IMPORTANT** - We need to pass **ALL** arguments to the function, for it to work.

---

Functions can also return data to the caller.

`len()` is a function that returns the length of a `string`/`list`, that we can later use.

```python
password = "Aa123456!"
pass_len = len(password)  # returns the int 9
if pass_len >= 8:
    print("Your password matches the needed length")
```

To return something from the function, we can use `return`.

**IMPORTANT**: When we use `return`, the function exited immediately (nothing will execute after `return`)

<br>
<br>

**Example 1**

```python
def calculate_sum(num1, num2):
    sum_result = num1 + num2
    return sum_result

result = calculate_sum(5, 10)
print(result)

# OUTPUT
# 15
```

**Example 2**

In the "odd or even" func, instead of printing the result, we can return True/False.

This will let us use the function in the future in `if` conditions.
```python
def is_even(user_num):
    if (user_num % 2) == 0:
        return True
    else:
        return False
```

```python
my_num = 20

if is_even(20):  # "is_even" return True, so the print will execute
    print(f"half of {my_num} is {my_num / 2}") 
```

---

<br>

- default value

```python
def greet_user(name="User"):
    print(f"Hello, {name}!")

greet_user("John")  # Output: Hello, John!
greet_user()        # Output: Hello, User!
```

<br>


- expected argument type (can enable auto-complete inside the function)

(also helps with documentation and readability)

```python
def calculate_square(num: int):
    return num ** 2

result = calculate_square(5)
print(result)

# OUTPUT
# 25
```

<br>

- expected output (can enable auto-complete for the output/return of the function)

```python
def bigger_list(num1, num2, num3) -> list:
    list1 = [num1 + 1, num2 + 2, num3 + 3]

result = bigger_list(5, 7, 12)

result.append(20) # The append will be auto-completed, as python knows for sure the "result" is a list

print(result) #     [6, 9, 15]

```


- recursive functions

Recursive functions are functions that call themselves within their own definition. They are useful when solving problems that can be broken down into smaller, similar subproblems.

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

result = factorial(5)
print(result)

# OUTPUT
# 120 (= 5 * 4 * 3 * 2 * 1)
```
