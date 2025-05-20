import serial

class BluetoothCommunication:
    def __init__(self, bluetooth_port='COM5', baud_rate=9600):
        self.bluetooth_port = bluetooth_port
        self.baud_rate = baud_rate
        self.ser = None

    def connect(self):
        try:
            self.ser = serial.Serial(self.bluetooth_port, self.baud_rate)
            print(f"Connected to {self.bluetooth_port}")
        except serial.SerialException as e:
            print(f"Error connecting to Bluetooth device: {e}")

    def readData(self):
        print("Waiting for data...")
        while not self.ser.in_waiting:
            pass
        if self.ser.in_waiting:
            line = self.ser.readline().decode().strip()
            return line
        else:
            raise serial.SerialTimeoutException("No data available to read.")

    def writeData(self, data):  
        if self.ser and self.ser.is_open:
            try:
                self.ser.write(str(data).encode())
                print(f"Data sent: {data}")
            except serial.SerialTimeoutException as e:
                print(f"Write timeout: {e}")
            return None
        else:
            print("Bluetooth connection is not open.")
            return None

    def close(self):
        if self.ser and self.ser.is_open:
            self.ser.close()
            print("Bluetooth connection closed.")
    
    def __del__(self):
        if self.ser and self.ser.is_open:
            self.ser.close()
            print("Bluetooth connection closed.")