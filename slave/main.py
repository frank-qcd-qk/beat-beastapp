from imutils.video import VideoStream
import imagezmq
import argparse
import socket
import time

#! Master IP: 10.0.0.1
#! Slave use port: 555{ID} 
DEBUG = True


sender = imagezmq.ImageSender(connect_to="tcp://10.0.0.1:5555")

rpiName = socket.gethostname()

if DEBUG:
	print("Got Hostname: ", rpiName)

vs = VideoStream(usePiCamera=True).start()
#stream = VideoStream(src=0).start
time.sleep(2.0)

while True:
	if DEBUG:
		print("Sending....")
	frame =vs.read()
	if frame is not None:
		sender.send_image(rpiName, frame)
	else:
    	print("No frame to send {}".format(time.time()))
	if DEBUG:
		print("Sent!")
