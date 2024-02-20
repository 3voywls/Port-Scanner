# Port Scanner

This is a simple Python script for scanning ports on a given host. It utilizes threading for concurrency and socket operations for establishing connections to ports.

## Prerequisites

- Python 3.x

## Usage

1. Clone the repository or download the `port_scanner.py` file.
2. Open a terminal or command prompt.
3. Navigate to the directory containing `port_scanner.py`.
4. Run the script using Python:

    ```bash
    python port_scanner.py
    ```

## Functionality

- The script provides two main functions:
  - `connectionScan(targetHost, targetPort)`: Scans a single port on a given host.
  - `portScan(targetHost, targetPorts)`: Scans multiple ports on a given host.
- It utilizes the `socket` module to create socket objects and establish TCP connections.
- Threading is used to perform port scans concurrently, improving efficiency.
- The script prints whether each scanned port is open or closed.

## Example

```python
# Perform a port scan on google.com with specified ports
portScan('google.com', [80, 22, 33, 44, 1, 2, 3, 4, 4, 5, 443])
```

## ScreenShots
![image](https://github.com/3voywls/Port-Scanner/assets/91720908/ad778f00-8124-4c25-8d03-2db29697b695)

This python script scan ports for open/closed state for given host and ports.
![image](https://github.com/3voywls/Port-Scanner/assets/91720908/5d6ce0ca-7f4f-4d92-ac25-729770babbe9)
Edit host and ports as per your requirement.

## Author
 - Suhail

