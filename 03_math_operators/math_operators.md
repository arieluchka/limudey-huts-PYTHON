We use mathematical operators to **perform calculations** or **manipulate data**. These operators are versatile and work with numbers, strings, and more.

#### Arithmetic Operators

- `+` **(Addition)**: Adds two numbers or concatenates strings.
    
- `-` **(Subtraction)**: Subtracts one number from another.
    
- `*` **(Multiplication)**: Multiplies two numbers or repeats a string by an integer.
    
- `/` **(Division)**: Divides one number by another and returns a float.
    
- `%` **(Modulus)**: Returns **only** the remainder of a division (שארית).
	- `5 % 3` == ${5 \over 3}$ == $1{2 \over 3}$ == 2 (השארית היא 2)
    
- `**` **(Exponentiation)**: Raises one number to the power of another.
    
- `//` **(Floor Division)**: Divides one number by another and returns the largest integer smaller than or equal to the result (חילוק ללא שארית).

### Examples with Numbers/Integers
#### Addition `a + b`

```python
x = 5
y = 3
print(x + y)  # Output: 8
```

#### Subtraction `a - b`

```python
x = 10
y = 4
print(x - y)  # Output: 6
```

#### Multiplication `a * b`

```python
x = 7
y = 6
print(x * y)  # Output: 42
```

#### Division `a / b`

```python
x = 10
y = 4
print(x / y)  # Output: 2.5
```

#### Modulus `a % b`

```python
x = 9
y = 4
print(x % y)  # Output: 1
```

#### Exponentiation `a ** b`

```python
x = 2
y = 3
print(x ** y)  # Output: 8
```

#### Floor Division `a // b`

```python
x = 9
y = 4
print(x // y)  # Output: 2
```

### Examples with Strings
#### String Concatenation `str + str`

```python
first_name = "John"
last_name = "Doe"
print(first_name + " " + last_name)  # Output: John Doe
```

```python
first_name = "Yoram"
last_name = "Cohen"
full_name = first_name + " " + last_name
print(full_name)  # Output: Yoram Cohen
```

```python
first_name = "Ariel"
last_name = "Agranovich"
full_name = f"{first_name} {last_name}"
print(full_name)  # Output: Ariel Agranovich
```

#### String Repetition `str * int`

```python
word = "Hi! "
print(word * 3)  # Output: Hi! Hi! Hi!
```
