import tkinter as tk
from PIL import Image, ImageTk
from DataStorage import DataStorageClass
from Communication import BluetoothCommunication
import os
def main():
    # Initialize Bluetooth communication
    bluetooth = BluetoothCommunication()
    bluetooth.connect()
    
    # Variables
    BalanceText = "Your Balance: $100"
    image_path = "path/to/your/image.png"  # Change this to your image path

    # Create main window
    root = tk.Tk()
    root.title("Balance Display")
    root.geometry("400x400")
    root.configure(bg="white")

    # Center the window on the screen
    root.eval('tk::PlaceWindow . center')

    # Create a frame to center content
    frame = tk.Frame(root, bg="white")
    frame.place(relx=0.5, rely=0.5, anchor="center")

    # Heading label
    heading = tk.Label(frame, text=BalanceText, font=("Arial", 20), bg="white")
    heading.pack(pady=20)

    # Load and display image
    img = Image.open(image_path)
    img = img.resize((150, 150), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(img)
    img_label = tk.Label(frame, image=photo, bg="white")
    img_label.pack(pady=10)

    root.mainloop()
    # Initialize data storage
    data_storage = DataStorageClass("data.csv")

    # Read data from Bluetooth device
    try:
        data = bluetooth.readData()
        print(f"Received data: {data}")
        # Write data to CSV file
        data_storage.WriteData(data)
    except Exception as e:
        print(f"Error reading data: {e}")

    # Close Bluetooth connection
    bluetooth.close()


if __name__ == "__main__":  
    main()