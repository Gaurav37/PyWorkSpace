from serial.tools import list_ports
port = list(list_ports.comports())
print(port)
for p in port:
    print(p.device)