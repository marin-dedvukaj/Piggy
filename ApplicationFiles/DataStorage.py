import csv
import os
from datetime import datetime

class DataStorage:
    """
    This class handles the creation, writing, and reading of a CSV file.
    It creates a file if it does not exist, and allows for writing data to it.
    It also allows for rebuilding the file and summing all values in the file.
    Attributes:
        filename (str): The name of the CSV file.
        Total (float): The total sum of all values in the file.
    """
    def __init__(self, filename):
        self.filename = filename
        self.Total = 0
        self.CreateFile()
        self.Total = 0
    
    def CreateFile(self):
        if not os.path.exists(self.filename):
            with open(self.filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['DAteTime','Value'])
                print(f"File {self.filename} created successfully.")
        else:
            print(f"File {self.filename} already exists.")
            self.Total = self.SumAllValues()
        pass 

    def RebuildFile(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)
            self.CreateFile()
            print(f"File {self.filename} rebuilt successfully.")
        else:
            print(f"File {self.filename} does not exist.")
            self.CreateFile()
        pass

    def WriteData(self, value):
        now = datetime.now()
        time = now.strftime("%Y-%m-%d %H:%M:%S")
        data = [time, value]
        with open(self.filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data)
            print(f"Data {data} written to {self.filename} successfully.")
    
    def SumAllValues(self):
        self.total = 0
        with open(self.filename, mode='r') as file:
            reader = csv.reader(file)
            header = next(reader)
            value_index = header.index('Value')
            for row in reader:
                try:
                    total += float(row[value_index])
                except (ValueError, IndexError):
                    continue
        return total


            