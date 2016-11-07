#!/usr/bin/env python

ip_address = raw_input("What is your local IP address?")
ip_address = ip_address.split(".")

print
print "{:<25}{:<25}{:<25}{:<25}".format(*ip_address)
print
