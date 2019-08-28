#!/usr/bin/env bash
echo "Please Enter the subnet"
read SUBNET
touch adress.txt
echo $adress > adress.txt
c=0
touch replied.txt
echo "Ip's which replied: " > replied.txt
for IP in $(seq 1 255);
do
if ping -c 1 -w 1 $SUBNET.$IP &> /dev/null
then
	echo "Reply"
	echo "$SUBNET.$IP" >> replied.txt
	else
	echo "Miss"
	fi
done
cat replied.txt
