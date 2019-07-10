

class Vectors:

    def __init__(self):
        self.var = self
        self.vec = []
        
    def createVector(file, col, nl, delim, qchar):

        with open(self.file, newline=self.nl) as csvfile:
            reader = csv.reader(csvfile, delimiter=self.delim, quotechar=self.qchar)
        
        print(reader)
            
