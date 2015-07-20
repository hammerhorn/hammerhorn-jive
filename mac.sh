#!/bin/sh

printf "\nwlan0: "
macchanger -s wlan0 |grep "^C"|awk '{print $3" "$4" "$5" "$6" "$7" "$8}'

printf " eth0: "
macchanger -s eth0|grep "^C"| awk '{print $3" "$4" "$5" "$6" "$7" "$8}'

echo
