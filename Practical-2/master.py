# Berkeley algorithm
# master

import datetime, zmq, pickle
from time import sleep

# Structure to save customer data (time). Global
timeClients = []

# Receive time from all connected salves
def getTime(numClients : int, socket):
	for x in range(numClients):
		timeC = pickle.loads(socket.recv())
        
		# Receive time, print received time
		print(f"Time {x} sent: {timeC}")
        
		# Calculate time difference
		timeClients.append(datetime.datetime.now() - timeC)
		socket.send("Difference Calculated...\nDifference sent to master".encode('utf-8'))

# Calculate average
def calcAverageTimeDiff():
    
	# Sum times, includes difference with server time (difference from 0)
	sumTimes = sum(timeClients, datetime.timedelta(0,0))
    
	# divide to get average
	average = sumTimes/len(timeClients)
	print("Difference Received: ")
	print(f"Average time difference: {average}")
	return average 

# send new watch
def sendTime (numClients : int, socket, offset : datetime.timedelta):
    
	# Get new clock time
	newTime = datetime.datetime.now() + offset
	print(f"The new time in the system is {newTime}")
    
	# Get request for new time from clients
	for x in range(numClients):
        
		# Wait to receive message
		id = socket.recv().decode('utf-8')
		print (f"sending to client {id}")
		socket.send(pickle.dumps(newTime))

# script main function
def main():
	# Server socket initialization
	context = zmq.Context()
	socket = context.socket(zmq.REP)
	socket.bind("tcp://*:5555") # Port 5555 will be used

	# Number of clients specified at startup
	numClients = int(input("Enter the number of slave to used: "))

	# The server is waiting for responses
	while True:
		print("starting synchronization")
        
		# function to get time
		getTime(numClients, socket)
		# print("Difference sent to master")
		offset = calcAverageTimeDiff()
        
		# Send new time to all clients
		sendTime(numClients, socket, offset)
        
		# finished algorithm
		print("synchronization finished")
		sleep(10) # Start this process every 10 seconds

if __name__ == '__main__':
	main()