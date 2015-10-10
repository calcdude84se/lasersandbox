import numpy as np

a = np.fromfunction(lambda i, j: (i-10)**2 + (j-10)**2, (20, 20), dtype=float)

string = ''''''

string += 'tp quadmasterxlii '+str(a.shape[0]/2.)+' 256 '+str(a.shape[1]/2.)+'\n'

def normalize(numpyArray):
    m = np.amax(numpyArray)
    for x in np.arange(0, numpyArray.shape[0]):
        for y in np.arange(0, numpyArray.shape[1]):
            numpyArray[x][y] = 200*numpyArray[x][y]/m
    return numpyArray

a = normalize(a)

##for x in range(0, 5):
##    for y in range(0, 5):
##        string += 'fill '+str(10*x)+' '+str(0)+' '+str(10*y)+' '+str(10*x+10)+' '+str(200)+' '+str(10*y+10)+' minecraft:air \n'

def createString(numpyArray):
    global string
    string += 'fill '+str(0)+' '+str(0)+' '+str(0)+' '+str(numpyArray.shape[0]-1)+' '+str(200)+' '+str(numpyArray.shape[1]-1)+' minecraft:air \n'
    for x in np.arange(0, numpyArray.shape[0]):
        for y in np.arange(0, numpyArray.shape[1]):
            string += 'fill '+str(x)+' '+str(0)+' '+str(y)+' '+str(x)+' '+str(int(numpyArray[x][y]))+' '+str(y)+' minecraft:sandstone \n'
    string += '\n'
    return string

print(createString(a))1 

##string = ''''''
##
##string += 'tp quadmasterxlii 0 256 0 \n'
##
##x = 5
##y = 5
##z = 50
##
##string += 'fill '+str(x)+' '+str(0)+' '+str(y)+' '+str(x)+' '+str(z)+' '+str(y)+' minecraft:stone'
##
##print(string)
