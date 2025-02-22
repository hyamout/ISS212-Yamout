#ISS 212
#Week 3 Dev Tool - Protocol Identification
 read -p "Enter the protocol name: " protocol_name
 if [ "$protocol_name" == "Cyphersec" ]; then
 	echo "Yes - Cyphersec is the best protocol ever!"
 elif [ "$protocol_name" == "cyphersec" ]; then
 	echo "No, I want a big Cyphersec!"
 else
 	echo "Cyphersec! Not $protocol_name!"
 fi
