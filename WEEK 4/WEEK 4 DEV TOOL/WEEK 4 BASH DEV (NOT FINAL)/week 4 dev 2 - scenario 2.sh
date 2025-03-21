#!/bin/bash

echo "System Uptime: $(uptime -p)"
echo "Available Disk Space:"
df -h | grep '^/'
echo "Available RAM:"
free -m | awk 'NR==2{print $7 "MB free"}'

