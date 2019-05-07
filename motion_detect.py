#import libs
import time
import RPi.GPIO as GPIO
import os
import sqlite3
import sys
from subprocess import call


#Assign gpio pin 13 to motion detection
motionPin = 13
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(motionPin, GPIO.IN)
GPIO.setwarnings(False)

#sqlite stuff
mydb = sqlite3.connect("./time.db")
cursor = mydb.cursor()


#initialize variables and wait for sensors to start up 
time.sleep(10)
timeOn = 0
endtime = 0
startTime = 0
screen = "empty"

#This is the main function to check if there was any motion detected by the sensor.
#If there was motion detected then turn the screen on. If there is no motion, turn it off.
print("Listening for changes!")
try:
    while True:
        
        timeStamp = time.strftime('%I:%M %p')
        if GPIO.input(motionPin) == 0: 
            screen = "Screen is Off"
            print("Screen is Off", motionPin)
            print(timeStamp)
            call(["/usr/bin/vcgencmd", "display_power", "0"])          
            time.sleep(1)
            # cursor.execute('''INSERT INTO time VALUES(?,?,?)''', (timeStamp, screen)
	    	# mydb.commit()
	    	# all_rows = cursor.execute('''SELECT * FROM time''')
	    	# os.system('clear')
	    	# for row in all_rows:
			#     print('{0} : {1}'.format(str(row[0]), row[1])
        elif GPIO.input(motionPin) == 1:
            screen = "Screen is On"
            print("Screen is On", motionPin)
            print(timeStamp)
            call(["/usr/bin/vcgencmd", "display_power", "1"])
            time.sleep(5)
            # cursor.execute('''INSERT INTO time VALUES(?,?,?)''', (timeStamp, screen)
	    	# mydb.commit()
	    	# all_rows = cursor.execute('''SELECT * FROM time''')
	    	# os.system('clear')
	    	# for row in all_rows:
			#     print('{0} : {1}'.format(str(row[0]), row[1])
        
except mydb.Error, e:
	print "Error %s:" %e.args[0]
	sys.exit(1)

except KeyboardInterrupt:
        GPIO.cleanup()
        mydb.close()
        print('Exited Cleanly')


