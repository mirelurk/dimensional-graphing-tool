import csvread
import vectors
import project

class cmdInterface:
    
    def __init__(self):
        self.filepath = ""
        self.prevpaths = []

    def newProject(self):
        currproj = project.project() 
        self.writeFilepath
        currproj.expr = self.inputExpr()
        currproj.colRef = self.inputColRef()
        currproj.createData(self.filepath, self.vars, ) 

        print("CSV Info")
        csv.info()
        print("Project Info")
        currproj.info()

    def writeFilepath(self):
        print("Type filepath now:")
        path = input()
        if self.filepath=="":
            self.filepath = path
        else:
            self.prevpath.append(self.filepath)
            self.filepath = path

    def usePrevPath(self):
        tmpcnt = 0
        print("Previous paths listed below, choose a number or type new for new filepath.")
        for path in self.prevpaths:
            print(tmpcnt, "\t", path)
            tmpcnt+=1
        usrPathInp = input()
        if usrPathInp=="new":
            self.writeFilePath()

    def inputExpr(self):
        print("Enter function:")
        inputExpr = input()
        exprList = list(inputExpr)
        return(exprList)

    def inputColRef(self):
        newColRef = []
        print("Using the numbers in the reference chart below, associate variables with columns from the uploaded file.")
        #PROBLEM----->>>csv.csvread.info()
        for i in self.vars:
            print("Column to be used for ", i, ":")
            colInput = input()
            col = int(colInput)
            self.newColRef.append(colInput)

        return(newColRef)
                
    def help(self):
        print("When I write the help section, it will appear now!")

    def exit(self):
        pass
        #write to files to record the previous paths, projects, etc.
