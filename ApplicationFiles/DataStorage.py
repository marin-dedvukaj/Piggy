import csv
import os
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
class DataStorageClass:
    def __init__(self, filename):
        self.pathOfFile = self.findFilePath(filename)
        self.Total = 0
        self.theGraph = None
        self.CreateFile()
    
    def findFilePath(self, filename):
        path = os.path.join(os.environ.get('ProgramFiles'), 'Piggy')
        if not os.path.exists(path):
            os.makedirs(path)
            print(f"Directory {path} created successfully.")
        else:
            print(f"Directory {path} already exists.")
        return os.path.join(path, filename)

    
    def CreateFile(self):
        if not os.path.exists(self.pathOfFile):
            with open(self.pathOfFile, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['DateTime','Value'])
                print(f"File {self.pathOfFile} created successfully.")
            self.WriteData(0)
            
        else:
            print(f"File {self.pathOfFile} already exists.")
        self.SumAllValues()    
        pass 

    def RebuildFile(self):
        if os.path.exists(self.pathOfFile):
            os.remove(self.pathOfFile)
            self.CreateFile()
            print(f"File {self.pathOfFile} rebuilt successfully.")
        else:
            print(f"File {self.pathOfFile} does not exist.")
            self.CreateFile()
        pass

    def WriteData(self, value):
        now = datetime.now()
        time = now.strftime("%Y-%m-%d %H:%M:%S")
        data = [time, value]
        with open(self.pathOfFile, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data)
            print(f"Data {data} written to {self.pathOfFile} successfully.")
    
    def SumAllValues(self):
        self.Total = 0
        with open(self.pathOfFile, mode='r') as file:
            reader = csv.reader(file)
            header = next(reader)
            value_index = header.index('Value')
            for row in reader:
                try:
                    self.Total += float(row[value_index])
                except (ValueError, IndexError):
                    continue
        return None
    
    def graphData(self):
        if not os.path.exists(self.pathOfFile):
            print(f"File {self.pathOfFile} does not exist. Please create a file first.")
            raise FileNotFoundError(f"File {self.pathOfFile} does not exist.")
        if not os.access(self.pathOfFile, os.R_OK):
            print(f"File {self.pathOfFile} is not readable. Please check the file permissions.")
            raise PermissionError(f"File {self.pathOfFile} is not readable.")
        
        df = pd.read_csv(self.pathOfFile)
        df['DateTime'] = pd.to_datetime(df['DateTime'])
        df = df.sort_values('DateTime')
        df['CumulativeSum'] = df['Value'].cumsum()

        self.theGraph, ax = plt.subplots()
        ax.plot(df['DateTime'], df['CumulativeSum'])
        ax.set_xlabel('DateTime')
        ax.set_ylabel('Cumulative Sum of Value')
        ax.set_title('Cumulative Data over Time')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.grid()

    def showGraph(self):
        if self.theGraph:
            plt.show()
        else:
            print("No graph to show. Please create a graph first.")
            try:
                self.graphData()
                self.showGraph()
            except Exception as e:
                print(f"Error showing graph: {e}")
        return
            