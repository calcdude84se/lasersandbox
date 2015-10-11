import numpy as np

##a should be an np array
##a = np.ones((20, 10))
a = np.fromfunction(lambda x ,y: (x-10)**2+(y-5)**2, (20,10))

string = ''''''

##position person at viewpoint
string += 'tp quadmasterxlii '+str(a.shape[0]/2.)+' 256 '+str(a.shape[1]/2.)+'\n'

##normalize max height of array
def normalize(numpyArray):
    m = np.amax(numpyArray)
    for x in np.arange(0, numpyArray.shape[0]):
        for y in np.arange(0, numpyArray.shape[1]):
            numpyArray[x][y] = 200*numpyArray[x][y]/m
    return numpyArray

a = normalize(a)

##create string
def createString(numpyArray):
    global string
    ##erase drawing
    for x in range(0, int(numpyArray.shape[0]/10.)+1):
        for y in range(0, int(numpyArray.shape[1]/10.)+1):
            string += 'fill '+str(10*x)+' '+str(0)+' '+str(10*y)+' '+str(10*x+10)+' '+str(200)+' '+str(10*y+10)+' minecraft:air \n'
    ##fill drawing
    for x in np.arange(0, numpyArray.shape[0]):
        for y in np.arange(0, numpyArray.shape[1]):
            string += 'fill '+str(x)+' '+str(0)+' '+str(y)+' '+str(x)+' '+str(int(numpyArray[x][y]))+' '+str(y)+' minecraft:sandstone \n'
    string += '\n'
    return string

print(createString(a))
