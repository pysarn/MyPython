'''
Created on Feb 19, 2015

@author: Pysarn
'''

def FileRead(Filename):
    f = open(Filename, 'r')
    return f.read()
    
def FileWrite(Filename, Text):
    f = open(Filename, 'w')
    f.write(Text)

if __name__ == '__main__':
    # test FileWrite and FileRead functions  
    FileWrite("test.txt", "Hello World!")
    print FileRead("test.txt")
