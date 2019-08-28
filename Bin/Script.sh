#!/usr/bin/env bash
echo "Please Enter the subnet"
read SUBNET

for IP in $(seq 1 255);
  do
    ping -c 1 $SUBNET.$IP

done
