#ISS 212
#Week 3 Dev Tool - Network Traffic Analysis Example
 read -p "Enter your annual data usage in MB: " data_usage
 if [ "$data_usage" -le 85528 ]; then
 	tax=$((data_usage * 18 / 100 - 556))
 else
 	surplus=$((data_usage - 85528))
 	tax=$((14839 + surplus * 32 / 100))
 fi
 if [ "$tax" -lt 0 ]; then
 	tax=0
 fi
 echo "Your Data Security Tax is: $tax MB"
