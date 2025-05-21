import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from DataStorage import DataStorageClass  
from Communication import BluetoothCommunication
import threading
import time

class PiggyApp:
    def __init__(self, filename):
        self.filename = filename
        self.root = tk.Tk()
        self.root.title("Piggy Bank")
        self.root.geometry("900x600")

        self.storage = DataStorageClass(filename)
        self.bluetooth = BluetoothCommunication()
        self.bluetooth.connect()
        self.canvas = None

        self.balance_var = tk.StringVar()
        self.balance_label = tk.Label(self.root, textvariable=self.balance_var, font=("Arial", 16))
        self.balance_label.pack(pady=10)

        self.graph_frame = tk.Frame(self.root)
        self.graph_frame.pack(fill=tk.BOTH, expand=True)

        self.update_display()

    def update_display(self):

        self.storage.SumAllValues()
        self.balance_var.set(f"Balance: {self.storage.Total}")

        try:
            self.storage.graphData()
            self.displayGraph()
        except Exception as e:
            self.balance_var.set(f"Error: {e}")
        self.root.after(1000, self.update_display)     


    def displayGraph(self):
        if self.canvas:
            self.canvas.get_tk_widget().destroy()

        self.canvas = FigureCanvasTkAgg(self.storage.theGraph, master=self.graph_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    
    def run(self):
        self.root.mainloop()



filename = "piggy_data.csv"
app = PiggyApp(filename)



def ComunicateWithBluetooth():
    while True:
        data = app.bluetooth.readData()
        print(f"Received: {data}")
        app.storage.WriteData(data)
        app.storage.SumAllValues()
        #app.bluetooth.writeData(app.storage.Total)


thread = threading.Thread(target=ComunicateWithBluetooth)

def main():
    thread.start()
    app.run()

if __name__ == "__main__":
    main()
