#!/usr/bin/env bash
echo "Please Enter the subnet"
read SUBNET

for IP in $(seq 1 255);
  do
    ping -c 1 $SUBNET.$IP

if  [[ "Packets Sent:" == "Packets Sent"]]; then
    echo "This IP is pinged"
  else
    echo "Did not connect to host"
fi

done
