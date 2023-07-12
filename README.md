# TCP-network-monitor-py

# Python Network Connections Monitor

This script allows you to monitor the active TCP network connections on your machine. It lists the process name, local address, remote address, and the PID of the process that established each connection. It can be configured to exclude specific processes or to only show remote connections.

## Prerequisites

1. Python 3.6 or newer
2. Administrative privileges (required to list network connections)
3. `psutil` Python library

You can install `psutil` with pip:

```shell
pip install psutil
```
## Usage

Run the script in a terminal with Python 3:

```
python script.py
```

By default, this will list all TCP network connections established by any process.
Options
-e or --exclude

Use this option followed by one or more process names to exclude these processes from the list.

Example:
```
python script.py -e firefox.exe
```

This will exclude any connections established by firefox.exe.
Filtering Local Connections

The script is configured to exclude local (loopback) connections by default. It only lists connections with a remote address that doesn't start with 127.0.0..
Limitations

This script only lists TCP connections. It does not show UDP, ICMP, or other types of network activity. It also does not show the actual traffic going through the connections.

For a more detailed analysis of network traffic, consider using a dedicated network monitoring or packet sniffing tool.
