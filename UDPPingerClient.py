# This skeleton is valid for both Python 2.7 and Python 3.
# You should be aware of your additional code for compatibility of the Python version of your choice.

import time
from socket import *

# Get the server hostname and port as command line arguments                    
host = "192.168.1.3"	#Localhost for debugging purposes		# FILL IN END
port = 12000		#Stated in UDPPingServer_python3.py		# FILL IN END
timeout = 1 # in seconds
 
# Create UDP client socket
# FILL IN START		
clientsocket = socket(AF_INET, SOCK_DGRAM)
# Note the second parameter is NOT SOCK_STREAM
# but the corresponding to UDP

# Set socket timeout as 1 second
clientsocket.settimeout(timeout)

# FILL IN END

# Sequence number of the ping message
ptime = 0  

# Ping for 10 times
while ptime < 10: 
	ptime += 1
	# Format the message to be sent as in the Lab description

	try:
    	# FILL IN START
    	
	# Record the "sent time"
		sentTime = time.clock()
		string="ping"+"-"+str(ptime)+"-"+str(sentTime)
		data = string.encode()		# FILL IN END
	# Send the UDP packet with the ping message
		clientsocket.sendto(data,(host, port))
	# Receive the server response
		modifiedMessage, serverAddress = clientsocket.recvfrom(2048)
	# Record the "received time"
		receivedTime = time.clock()
	# Display the server response as an output
		print(modifiedMessage)
	# Round trip time is the difference between sent and received time
		rtt = receivedTime - sentTime
		print(rtt)
		print()
        
        # FILL IN END
	except:
        # Server does not response
	# Assume the packet is lost
		print("Request timed out.")
		print()
		continue

# Close the client socket
clientsocket.close()
 
