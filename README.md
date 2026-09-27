# Algorithm for File Updates in Python

## Project Description
An automation system developed for a healthcare organization to inspect and update an access control allow list, ensuring that only verified users retain access to restricted patient data subnetworks.

## Open the file that contains the allow list
The algorithm assigns the target file name to a variable and opens it using the `with` statement to ensure proper resource management and automatic file closure:

```
import_file = "allow_list.txt"

with open(import_file, "r") as file:
```

## Read the file contents
Inside the `with` block, the `.read()` method converts the contents of the text file into a string format:

```
    ip_addresses = file.read()
```

## Convert the string into a list
To process and compare each IP address individually, the `.split()` method divides the text string into list elements:

```
ip_addresses = ip_addresses.split()
```

## Iterate through the remove list
A `for` loop iterates through each element in the revocation list (`remove_list`), checking whether that element is currently present in the allow list:

```
for element in remove_list:
    if element in ip_addresses:
```

## Remove IP addresses that are on the remove list
When a match is found, the `.remove()` method deletes that specific IP address from `ip_addresses`:

```
        ip_addresses.remove(element)
```

## Update the file with the revised list of IP addresses
The list is rejoined into a single string using newline characters (`"\n"`) as delimiters, and a second `with` statement writes the updated list back to the original file:

```
ip_addresses = "\n".join(ip_addresses)

with open(import_file, "w") as file:
    file.write(ip_addresses)
```

## How to Run

1. Clone this repository:
   ```
   git clone https://github.com/smormu31415/cybersecurity-allowlist-algorithm.git
   cd cybersecurity-allowlist-algorithm
   ```
2. Run the script:
   ```
   python3 main.py
   ```
