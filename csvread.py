import csv
import numpy as np

class CsvRead:

    cnt = True

    def __init__(self, file):
        self.file = file
        self.nl = ''
        self.delim = ','
        self.qchar = '\"'

        self.headers = []
        self.npdata = []

    def read(self):
        hdrs = [self.headers.append(i) for i in np.genfromtxt(self.file, dtype=str, delimiter=self.delim, max_rows=1)]
        self.npdata = np.genfromtxt(self.file, delimiter=self.delim, skip_header=1)
        
    def info(self):
        temp = 0
        print("Col#\tHeader\tLength")
        for i in self.headers:
            print(temp, "\t", i, "\t", len(self.readCol(temp)))
            temp+=1

    def readCol(self, col):
        return(self.npdata[:,col])

    def specialNl(self, newl):
        self.nl = newl

    def specialDelim(self, dl):
        self.delim = dl

    def specialQchar(self, qc):
        self.qchar = qc
        
