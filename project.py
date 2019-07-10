import csvread

class project:

    def __init__(self):
        self.id = 0
        self.headers = []
        self.vectors = []
        self.framedata = []
        self.colRef = []
        self.expr = ""
        self.vars = []
        self.fileref = ""

        
    def createData(self, filepath, hdrs, col):
        self.headers = hdrs
        self.fileref = filepath
        csv = csvread.CsvRead(self.filepath)
        csv.read()
        for ref in col:
            newCol = csv.readCol(ref)
            print("Test--Vector Read", newCol)
            self.vectors.append(newCol)

    def info(self):
        print(self.id, "\n", self.headers, "\n")
        for i in vectors:
            print(i[0:9])
        print(self.framedata, "\n", self.fileref)


