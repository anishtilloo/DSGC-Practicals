# Berkeley algorithm
# client script

import datetime, zmq, random, pickle
from time import sleep

def getRandomOffset(currTime : datetime.datetime):
	offset = datetime.timedelta(minutes=random.randint(-10,10), seconds=random.randint(-59, 59))
	newTime = currTime + offset
	return newTime

# script main function
def main():
	# client initialization
	context = zmq.Context()
	client = context.socket(zmq.REQ)
	client.connect("tcp://localhost:5555") # Port 5555 will be used

	# Get random ID for the process
	id = random.randint(0, 1024)

	# Select whether the system time will be used without variation or with a random variation
	mode = int(input("""Press 1 to Continue
	"""))
	# 1) Continue
	# 2) random time variance\n

	# starting client
	while True:
		print(f"process ID: {id}")
		# \nSending sync time

		# gets time
		firstTime = datetime.datetime.now()
		# If mode = 2, a random variation is added
		if mode == 2:
			firstTime = getRandomOffset(firstTime)
		
		print(f"Receiving time {firstTime}")
		client.send(pickle.dumps(firstTime))

		# wait for answer
		resp = client.recv().decode('utf-8')
		print(f"{resp}")

		# Wait to send new time request message
		sleep(0.01)
		client.send("time request".encode('utf-8'))
		# wait for answer
		reply = pickle.loads(client.recv())

		# Show received message on screen
		print(f"Synchronized time at slave :  {reply}")

		sleep(360000) # wait 10 seconds

if __name__ == '__main__':
	main()