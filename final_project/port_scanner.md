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

(all user ip input functions should return a list (even if it's only a single ip))

### Scanner
- a function that receives an ip address and a port
- checks (with a timeout of 1 sec) if it can create a connection to the socket
- returns tuple(port, bool)
	- (3000, True)
	- (80, True)
	- (443, False)

### Orchestrating the Scan (calling the scanner)
After user input is collected and parsed (we have a **list of ips** and a **list of ports**):
1) create an empty dictionary
2) for every IP address
3) add it as a key to the dictionary (with an empty list)
```python
open_ports_of_ips = {
	"192.168.1.1": [],
	"192.168.1.2": [],
	...
}
```
4) go over all chosen ports 
5) add every open port to the list

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
## Important notes!
- When raising errors, communicate clearly of what was the issue and what can be done to fix it.
	- "an error while validating the port range. Please ensure you use a valid port (between 0 and 65535)."
	- "an error with validating these IP: {ip}. Please ensure the is has 4 octets and each octet is in range of 0 to 255."
## Bonuses
- scan the ports using [multiple threads](https://www.youtube.com/watch?v=STEOavXqXkQ)
- at the start of the run, print the estimated time it will take to scan all the ports (num_of_ips * num_of_ports * timeout(1 second) / threads (if multi-threading))
	- "The scan will complete in around 3 minutes and 45 seconds. (will be ready at around 16:42)."


