base functions:

### validation functions:
- check if a given ip is valid
	- a string
	- has 4 octets (seperated by dots)
	- every octet is between 0 and 255
	- the length of the ip is making sense (the shortest X.X.X.X=7 and longest XXX.XXX.XXX.XXX=15)

- check if a given port is valid
	- an integer
	- ranging from 1 to 65535

### parse user input functions:
לזקק את הקלט מהמשתמש
#### ports:
These functions will check the user input and turn it into a list of ports.
- single port
	- turn into int (catch errors/use .isdigit)
	- check if port is valid
	- return it as a list
- list of ports
	- separate the list
	- turn all items into ints (catch errors/use .isdigit)
	- check if all ports are valid
		- if they are, return the list of ports
		- if not, raise an exception 
- range of ports
	- separate the start and end of the ranges
	- check if both are valid
	- validate the start of the range is smaller than the end
	- return a list of ports in this range (you can use the `for port in range(start, end + 1)`)

#### IPs:
These functions will check the user input and turn it into a list of ips.
- single ip
	- check if ip is valid
	- return in a list
- list of ips
	- separate list
	- check every ip if it's valid
		- if all are valid, return list 
		- if not, raise exception
- range of ips **BONUS**
	- separate first ip and last ip
	- check if both IPs are valid
	- check that the first ip is before the last ip
		- 10.0.0.0 - 10.0.5.100 OK
		- 5.62.12.5 - 3.12.5.7 NOT OK
	- create a list of ips in that range 
		- 10.0.0.0 - 10.0.0.3 = \[10.0.0.0, 10.0.0.1, 10.0.0.2, 10.0.0.3]

main functions:
- check if a specific port of a specific ip address is open.
	- input: ip address, port
	- output: bool



user input functions (ip):
(all user ip input functions should return a list (even if it's only a single ip))
- 

## user interface:
The user will have multiple ways to use the port scannning tool.
IPs of choice:
1) input a single IP 
2) input a list of ips (192.168.1.1, 192.168.1.6, 192.168.1.10)
3) input a range of ips (192.168.1.1 - 192.168.5.4) **BONUS**
4) input a network to test (192.168.1.0/24 or 10.5.2.0/19) **BONUS**

ports of choice:
1) A single port (to check if that port is open)
2) A list of ports (to check what ports from the list are open)
3) A range of ports (to check the ports range)

### Scanner
- a function that receives an ip address and a port
- checks (with a timeout of 1 sec) if it can create a connection to the socket
- returns tuple(port, bool)
	- (3000, True)
	- (80, True)
	- (443, False)

### Orchestrating the Scan (calling the scanner)
After user input is collected and parsed (we have a **list of ips** and a **list of ports**):
4) create an empty dictionary
5) for every IP address
6) add it as a key to the dictionary (with an empty list)
	`open_ports_of_ips = {"192.168.1.1": []}`
7) go over all chosen ports
8) add every open port to the list

**Example of the output:**
```python
open_ports_of_ips = {
	"192.168.1.1": [80, 443, 3000],
	"192.168.1.2": [80],
	"192.168.1.3": [],
	"192.168.1.4": [80, 3000],
	}
```

### Displaying the Results
After scanning, present the results in a clear and organized format
- print what was the request of the user ("searched for open ports for these ips: ....")
- For each IP, list the open ports.
- Add the total time the whole process took **BONUS**

## Bonuses
- scan the ports using [multiple threads](https://www.youtube.com/watch?v=STEOavXqXkQ)
- at the start of the run, print the estimated time it will take to scan all the ports (num_of_ips * num_of_ports * timeout(1 second) / threads (if multi-threading))
	- "The scan will complete in around 3 minutes and 45 seconds. (will be ready at around 16:42)."
## Important notes and tips!
#### Raising errors
When raising errors, communicate clearly of what was the issue and what can be done to fix it.
	- "an error while validating the port range. Please ensure you use a valid port (between 0 and 65535)."
	- "an error with validating these IP: {ip}. Please ensure the is has 4 octets and each octet is in range of 0 to 255."

#### Isolate your work
When writing new functions, check them individually. You can do it in the "if name == main"
For example, If we write the function that checks if an IP is valid,
```python
# ./validation_functions.py

def check_if_ip_valid(ip: str):
	...


if __name__ == "__main__":
	print(check_if_ip_valid(ip="192.168.5.3"))   # should be valid
	print(check_if_ip_valid(ip="500.4.6.7"))     # is not valid
	print(check_if_ip_valid(ip="170.53.51.7.6")) # is not valid
```

This way, we can check if the function works correctly, **without running the whole application**


---

# Handing the work
You will be uploading a zip folder, with all of the project files in it.


## Part 1

**Decide on how to separate the functions into modules, and create those files.**
(Example: `input_parsing.py`, `data_validation.py`, `user_interface.py`)

In each file, start defining the functions (everything except the function itself)
Example:

`data_validation.py`
```python
"""
This file will hold functions that validate if an ip/port are valid.

It also has functions that check if a user input according to the option.
(for example: if user chose a port range, then the input is following "PORT-PORT")
"""

def check_if_ip_valid(ip: str) -> bool:
	pass

def check_if_port_valid(port: int) -> bool:
	pass

...
...

if __name__ == "__main__":
	pass
```

`input_parser_and_validator.py`
```python
import data_validation

...

def single_port_parser(user_input: str) -> []:
	"""This function checks that the user input is a valid single port, and
	returns it as a list"""
	pass


def port_range_parser(user_input: str) -> []:
	"""
	This function checks that the user input is a valid range of ports
	and returns all the ports in a list.
	Example:
		input:  "51-55"
		output: [51, 52, 53, 54, 55]
	"""
	pass

def port_list_parser(user_input: str) -> []:
	pass

...

if __name__ == "__main__":
	pass
```

**Its okay if you are not 100% sure with your plan**. You can always change it in the middle of the project :)

- adding documentation **is not a must**, but will help you understand your plan better.
- YOU **CAN** WRITE DOCUMENTATION IN HEBREW!
- If you find that you have time to also start writing the functions themselves, feel free to include some of them, to receive feedback.
---

## part 2 

Upload a zip folder with all the files, where most of the functions are already implemented and written.


leave the `if __name__ == "__main__":` in, so ill be able to easily test your code.


You can also leave a `README.txt` or a `README.md` file, if you have notes for me/want to write a basic explanation/overview of the project.

---
## part 3

