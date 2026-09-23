import serial
import time

cmd = (
    'AUTH1 '
    '100000000000000000000000000000000000000000000000000000000000000000000000'
    '00000000000000000000000000000000000000000000000000000000000000000000'
)

checksum = sum(cmd.encode('ascii')) % 0x100
packet = f'{cmd}:{checksum:02X}\r\n'

print("Sending:")
print(packet)

s = serial.Serial(
    '/dev/ttyAMA0',
    57600,
    bytesize=8,
    parity='N',
    stopbits=1,
    timeout=0.2
)

s.reset_input_buffer()
s.write(packet.encode('ascii'))
s.flush()

print("Waiting for response...")

data = b''
deadline = time.time() + 3

while time.time() < deadline:
    x = s.read(256)
    if x:
        data += x
        print("RX:", x.hex(' '))
        print("   :", repr(x))

print("\nTotal:", len(data), "bytes")
print("HEX:")
print(data.hex(' '))

print("\nASCII:")
print(repr(data))

s.close()

