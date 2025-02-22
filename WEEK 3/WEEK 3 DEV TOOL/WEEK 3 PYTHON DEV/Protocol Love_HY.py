#ISS 212
#Week 3 Dev Tool - Protocol Love Example
protocol_name = input("Enter the protocol name: ")
if protocol_name == "Cyphersec":
	print("Cyphersec is the only supported protocol!")
elif protocol_name == "cybersec":
	print("DENIED. Cyphersec protocol ONLY!")
else:
	print(f"Cyphersec! Not {protocol_name}!")
C