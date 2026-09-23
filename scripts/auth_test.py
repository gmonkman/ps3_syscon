import serial
import time

s = serial.Serial(
    '/dev/ttyAMA0',
    57600,
    bytesize=8,
    parity='N',
    stopbits=1,
    timeout=0.2
)

# Clear anything already in the receive buffer
s.reset_input_buffer()

cmd = b'AUTH1 ' + b'10' + b'00' * 63 + b'\n'

print("Sending:")
print(cmd.hex(" "))

s.write(cmd)
s.flush()

print("\nWaiting for response...")

data = b''

deadline = time.time() + 3
while time.time() < deadline:
    chunk = s.read(256)
    if chunk:
        data += chunk
        print("RX:", chunk.hex(" "), repr(chunk))

print("\nTotal bytes:", len(data))
print("Complete response:")
print(data.hex(" "))
print(repr(data))

s.close()
