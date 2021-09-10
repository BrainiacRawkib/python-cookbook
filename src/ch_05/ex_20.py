# communicating with serial ports
import serial
from serial.tools import list_ports as port_lists

ser = serial.Serial('COM10', baudrate=9600,
                    bytesize=8, parity='N', stopbits=1, rtscts=True)

ser.write(b'G1 X50 Y50\r\n')
resp = ser.read()

# list all com ports currently active
ports = list(port_lists.comports())

for port in ports:
    print(port)

# Hint: the struct module can be used to create binary-coded commands or packets

if __name__ == '__main__':
    pass
