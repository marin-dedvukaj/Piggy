import serial
import time

class ReciverAnalyser:
    def __init__(self, port, baudrate=9600):
        self.port = port
        self.baudrate = baudrate
        self.serial = None
        pass

    def open_serial(self):
        try:
            self.serial = serial.Serial(self.port, self.baudrate)
            print(f"Serial port {self.port} opened successfully.")
        except serial.SerialException as e:
            print(f"Error opening serial port: {e}")
    
    def close_serial(self):
        if self.serial and self.serial.is_open:
            self.serial.close()
            print(f"Serial port {self.port} closed.")
        pass
