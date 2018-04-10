import serial
import io
import time
import datetime

# Connect to Serial Port
# Change according to connected device port
# To see port enter in terminal: dmesg
ser = serial.Serial('/dev/ttyUSB0', timeout=1)
# Parameters for Blocking or Non-Blocking communication
sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser, 1), newline = '\r', line_buffering = True)

# Get current date and time
now = datetime.datetime.now()

# Name for file
fileName = now.strftime("%Y-%m-%d %H-%M") + ".csv"

# Append mode
file = open(fileName, 'a')

# Read first line and ignore it
data = sio.readline()
#start_time = time.time() * 1000

#x = 0
#sample = 0

while 1:
    
    # File must be open and close each time because of writting to SD card, if not data is lost and not stored
    file = open(fileName, 'a')
    
    # Read a single measurement.
    data = sio.readline()
    
    # Convert data to extract real measurement value.
    i = int(data)
    total = i*(0.003384)
    #FOR TESTING
    #print(data) 
    print(str(total)) #Confirmando que sea el mismo que se escribe.
    file.write(str(datetime.datetime.now()) + "," + str(total) + "\n")
    file.close()
    

#end_time = time.time() * 1000
#print("--- %s seconds ---" % (end_time - start_time))
