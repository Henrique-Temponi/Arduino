import serial as arduino
import time

print("Start")

y = "0 1 0\n".encode()
print(type(y))
print(y)

port = arduino.Serial('/dev/ttyUSB0')

# port.write(y)
# port.write(b'1 1 0\n')

time.sleep(2)

while True:
    port.write(b'0 0 0\n')
    time.sleep(2)
