'''
Created on Feb 19, 2015
@author: Pysarn
test on Python 2.7
'''

def createDirectory(path):
    # create directory if it doesn't exists
    import os
    import errno

    try:
        os.makedirs(path)
        print path, "was created"
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise
    
def readFile(filename):
    # read text file
    f = open(filename, 'r')
    return f.read() # String
    
def writeFile(filename, Text):
    # write String to text file
    f = open(filename, 'w')
    f.write(Text)

def openUrl(url):
    # open url and return content as String
    import urllib
    sock = urllib.urlopen(url)
    text = sock.read()
    sock.close()
    return text # String

def saveUrl(url, directory, filename):
    # open url and save content to textfile
    createDirectory(directory)
    print ("Downloading :"), url
    text = openUrl(url)
    writeFile(filename, text)


if __name__ == '__main__':
    # test FileWrite and FileRead functions  
    createDirectory("new/dir")    
    
    writeFile("test.txt", "Hello World!")
    print readFile("test.txt")

    # test Download
    print openUrl("http://example.com")
    
