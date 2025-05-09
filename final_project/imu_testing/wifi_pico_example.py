# A simple example that:
# - Connects to a WiFi Network defined by "ssid" and "password"
# - Performs a GET request (loads a webpage)
# - Queries the current time from a server

import network   # handles connecting to WiFi
import urequests # handles making and servicing network requests

# Connect to network
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

# Fill in your network name (ssid) and password here:
ssid = 'Jojo'
password = 'Jojo12345'
wlan.connect(ssid, password)


# Example 1. Make a GET request for google.com and print HTML
# Print the html content from google.com
print("1. Querying google.com:")
r = urequests.get("http://www.google.com")
print(r.content)
r.close()

# Example 2. urequests can also handle basic json support! Let's get the current time from a server
print("\n\n2. Querying the current GMT+0 time:")
r = urequests.get("http://date.jsontest.com") # Server that returns the current GMT+0 time.
print(r.json())

import socket

try:
    addr_info = socket.getaddrinfo("httpbin.org", 80)
    ip_addr = addr_info[0][-1][0]
    s = socket.socket()
    s.connect((ip_addr, 80))
    print("Connected to httpbin.org!")
    s.send(b"GET / HTTP/1.0\r\nHost: httpbin.org\r\n\r\n")
    response = s.recv(4096)
    print("Received response:", response)
    s.close()
except OSError as e:
    print(f"Socket error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")