import serial
import time

s = serial.Serial(
    '/dev/ttyAMA0',
    57600,
    bytesize=8,
    parity='N',
    stopbits=1,
    timeout=0.05
)

print("Listening...")
print("Now power on the PS3.")

try:
    while True:
        data = s.read(256)
        if data:
            print(time.strftime("%H:%M:%S.%f")[:-3],
                  "RX:", data.hex(" "))
except KeyboardInterrupt:
    pass
finally:
    s.close()
