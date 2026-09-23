import serial
import time

s = serial.Serial(
    '/dev/ttyAMA0',
    57600,
    bytesize=8,
    parity='N',
    stopbits=1,
    timeout=1
)

print("Sending test...")
s.write(b'HELLO\r\n')
s.flush()

time.sleep(0.1)

data = s.read(100)
print("Received:", data.hex())
print("As text:", repr(data))

s.close()
