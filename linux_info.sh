#!/bin/bash

# 1. Opret en ny bruger ved navn "testuser"
sudo useradd -m testuser
echo "User 'testuser' created."

# 2. Log ind som "testbruger" og opret en ny mappe kaldet Projekter
sudo -u testuser mkdir /home/testuser/Projects
echo "Folder 'Projects' created in /home/testuser."

# 3. Udskriv information om systemet og kerneversionen
echo "System and Kernel Information:"
uname -a

# 4. Udskriv information om den Linux-distribution, der er installeret
echo "Linux Distribution Information:"
cat /etc/os-release
