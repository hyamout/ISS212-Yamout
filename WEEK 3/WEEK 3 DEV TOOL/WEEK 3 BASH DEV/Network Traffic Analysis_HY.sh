#ISS 212
#Week 3 Dev Tool - Network Traffic Analysis Example
 read -p "Enter the packet size in bytes: " packet_size
 if [ "$packet_size" -ge 100 ]; then
 	echo "True - Packet meets the threshold for analysis."
 else
 	echo "False - Packet is too small to analyze."
 fi
