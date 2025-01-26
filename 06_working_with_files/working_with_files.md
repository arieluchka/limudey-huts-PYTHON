Python has a basic built-in functionality for working with files
```python
f = open("file.txt")

print(f.read())  # reads the whole file
```


```python
f = open("file.txt")

print(f.read(4))  # reads the first 4 characters
```

When we read from a file, the position where we left in is saved.
If we will continue reading from the same opened file, it will continue from the last position.
```python
f = open("file.txt")

print(f.read(4))  # reads the first 4 characters
print(f.read(10)) # reads the next 10 characters (that comes after the first)
```

---
#### Read the whole line
```python
f = open("file.txt")

print(f.readline())  # reads first line (up to the \n character)
print(f.readline())  # reads the second line
```

you can also save the line into a varialble
```python
f = open("file.txt")
line1 = f.readline()

print(line1)
```

or you can get **all of the lines** in a list
```python
f = open("file.txt")
all_lines = f.readlines() # <------- readlines instead of readline

print(all_lines)
```

---

#### We can go over all lines with a loop
```python
f = open("file.txt")

for line in f:
	print(line)
```

---
#### It's important to close the file after we finish with it
```python
f = open("file.txt")

for line in f:
	print(line)

f.close()
```

#### There are different modes when opening files
here are some of them:
```python
f1 = open("file.txt", "r") # read only mode (the default)
f2 = open("file.txt", "w") # write to the file (deletes all previous data) (creates the file if it doesn't exists)
f3 = open("file.txt", "a") # appends to the end of the file
f4 = open("file.txt", "x") # creates new file and opens it for writing (raises an error if file already exists)
```

---
## Writing to file
overwrites whatever was in the file with "hello world"
```python
f = open("file.txt", "w")  # first we need to open the file in a writable mode

f.write("hello world")

f.close()  # we need to close the file for changes to take effect
```

This will add the "hello world" at the end of the file
```python
f = open("file.txt", "a")

f.write("hello world")

f.close()  
```
