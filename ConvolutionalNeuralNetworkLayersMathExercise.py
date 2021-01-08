"""
The programs are meant to be tested with 1 starting size at a time, so in def main(),
please comment out 4 of the startingSizeXX() functions. Then run the script, and
the results as well as parameters will be printed in the command line.

No installs are needed.
"""

def main():
    startingSize36()
    startingSize64()
    startingSize69()
    startingSize227()
    startingSize250()
    
    run()

def run():
    startingVars = startingSize * startingSize * colorDepth
    print("starting image size: " + str(startingSize) + "x" + str(startingSize))
    print("starting variables: " + str(startingVars))
    print("")

    currentSize = startingSize
    currentLayers = colorDepth

    for i in range(loops):
        print("using frame size of " + str(frameSize))
        if (currentSize - frameSize) % strides[1] == 0:
            nextLayerSize = ((currentSize - frameSize)/strides[1]) + 1
            print("using stride size of " + str(strides[1]))
        elif (currentSize - frameSize) % strides[0] == 0:
            nextLayerSize = ((currentSize - frameSize)/strides[0]) + 1
            print("using stride size of " + str(strides[0]))
        else:
            nextLayerSize = ((currentSize - frameSize)/1) + 1
            print("using stride size of 1")
        if nextLayerSize <= 0:
            break
        print("sizeAfterConvolution: " + str(nextLayerSize))

        currentLayers = currentLayers * 2
        newVars = nextLayerSize*nextLayerSize*currentLayers

        if nextLayerSize % poolSizes[1] == 0:
            layerSizeAfterPool = nextLayerSize / poolSizes[1]
            print("using pool size of " + str(poolSizes[1]))
        elif nextLayerSize % poolSizes[0] == 0:
            layerSizeAfterPool = nextLayerSize / poolSizes[0]
            print("using pool size of " + str(poolSizes[0]))
        else:
            layerSizeAfterPool = nextLayerSize
            print("skipping pool")
        currentSize = layerSizeAfterPool
        newVars = layerSizeAfterPool*layerSizeAfterPool*currentLayers
        print("currentSize: " + str(currentSize))
        print("currentLayers: " + str(currentLayers))
        print("newVars: " + str(newVars))
        print("")

def startingSize36():
    global startingSize
    global currentSize
    global colorDepth
    global currentLayers
    global frameSize
    global strides
    global poolSizes
    global loops

    startingSize = 36
    colorDepth = 3
    frameSize = 3
    strides = [1, 1]
    poolSizes = [2, 3]
    loops = 3

def startingSize64():
    global startingSize
    global currentSize
    global colorDepth
    global currentLayers
    global frameSize
    global strides
    global poolSizes
    global loops

    startingSize = 64
    colorDepth = 3
    frameSize = 5
    strides = [1, 2]
    poolSizes = [2, 3]
    loops = 3

def startingSize69():
    global startingSize
    global currentSize
    global colorDepth
    global currentLayers
    global frameSize
    global strides
    global poolSizes
    global loops

    startingSize = 69
    colorDepth = 3
    frameSize = 5
    strides = [1, 2]
    poolSizes = [2, 3]
    loops = 3

def startingSize227():
    global startingSize
    global currentSize
    global colorDepth
    global currentLayers
    global frameSize
    global strides
    global poolSizes
    global loops

    startingSize = 227
    colorDepth = 3
    frameSize = 11
    strides = [1, 2]
    poolSizes = [2, 3]
    loops = 3

def startingSize250():
    global startingSize
    global currentSize
    global colorDepth
    global currentLayers
    global frameSize
    global strides
    global poolSizes
    global loops

    startingSize = 250
    colorDepth = 3
    frameSize = 13
    strides = [1, 2]
    poolSizes = [2, 3]
    loops = 3

if __name__ == "__main__":  #Run the main function
    main()
