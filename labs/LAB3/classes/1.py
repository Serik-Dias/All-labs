class String:
    def getstring(self):
        self.a = input("Enter: ")
    def printstring(self):
        print("With upper case: " + self.a.upper())


mystring = String()
mystring.getstring()
mystring.printstring()