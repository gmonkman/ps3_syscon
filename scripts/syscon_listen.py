import serial

s = serial.Serial(
    '/dev/ttyAMA0',
    57600,
    bytesize=8,
    parity='N',
    stopbits=1,
    timeout=1
)

print("Listening for 10 seconds...")
data = s.read(1000)

print("Received", len(data), "bytes:")
print(data.hex(" "))

s.close()
