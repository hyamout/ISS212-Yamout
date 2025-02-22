#ISS 212
#Week 3 Dev Tool - Network Traffic Analysis Example
 read -p "Enter the year to check the patch cycle: " year
 if [ "$year" -lt 2000 ]; then
 	echo "Not within the managed patch period."
 else
 	if (( year % 4 != 0 )); then
     	echo "Standard Year"
 	elif (( year % 100 != 0 )); then
     	echo "Patch Year"
 	elif (( year % 400 != 0 )); then
     	echo "Standard Year"
 	else
     	echo "Patch Year"
 	fi
 fi
