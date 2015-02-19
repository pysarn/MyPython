'''
Created on Feb 19, 2015
@author: Pysarn
test on Python 2.7
'''

def createDirectory(Path):
    import os
    import errno

    try:
        os.makedirs(Path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise
    
def readFile(Filename):
    f = open(Filename, 'r')
    return f.read()
    
def writeFile(Filename, Text):
    f = open(Filename, 'w')
    f.write(Text)

def openUrl(url):
    import urllib
    sock = urllib.urlopen(url)
    text = sock.read()
    sock.close()
    return text

if __name__ == '__main__':
    # test FileWrite and FileRead functions  
    createDirectory("new_dir")    
    
    writeFile("test.txt", "Hello World!")
    print readFile("test.txt")

    # test Download
    print openUrl("http://example.com")
    
