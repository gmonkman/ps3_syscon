import serial
import time

port = "/dev/ttyAMA0"

s = serial.Serial(
    port=port,
    baudrate=57600,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    timeout=0.1,
)

print(f"Listening on {port} at 57600 8N1...")
print("Power on the PS3 now.")
print("Press Ctrl-C to stop.\n")

try:
    while True:
        data = s.read(256)
        if data:
            print(
                time.strftime("%H:%M:%S"),
                "RX:",
                data.hex(" ")
            )
except KeyboardInterrupt:
    print("\nStopped.")
finally:
    s.close()
