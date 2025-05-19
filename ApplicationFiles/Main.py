import tkinter as tk
from PIL import Image, ImageTk
from DataStorage import DataStorageClass
from Communication import BluetoothCommunication
import os
def main():
    # Connect to bluetooth
    bl = BluetoothCommunication()
    bl.connect()
    # Create data storage
    ds = DataStorageClass("Data.csv")
    print(ds.pathOfFile)
    print(ds.Total)

    return None

if __name__ == "__main__":
    main()