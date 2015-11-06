def frequencyTable(countdict):
    
    print("ITEM", "\t", "FREQUENCY")
    
    ## print the dictionary sorted by the key


def mode(alist, countdict):

    ## iterate over alist and build a dictionary called countdict
    ## to store the frequency of each value in alist
    for i in alist:
        if countdict.get(i, None):
            countdict[i] = countdict[i] + 1
        else:
            countdict[i] = 1           

    maxcount = max(countdict, key=countdict.get)## find the highest value in a value componet of the dictionary
    
    modelist = [ ]      ## creates a list of modes since there may be more than one mode
    for item in countdict:
        if countdict[item] == maxcount:
            modelist.append(item)
    
    return modelist

def median(alist):
    # deep copy of a list and then sort the copy

    ## find the median value - middle value if the length odd
    ## average of 2 middle values otherwise
    
    return median

def makeMagnitudeList():
        quakefile = open("earthquakes.txt","r")
        headers = quakefile.readline()
        
        maglist = [ ]
        for aline in quakefile:
            vlist = aline.split()
            maglist.append(float(vlist[1]))
        return maglist


magList = makeMagnitudeList()
print(magList)
## print mean (use built in functions sum and len)
print("mean: ", sum(magList))
frequencyDict = {}
med = median(magList)
print("median: ", med)
mod = mode(magList, frequencyDict)
print("mode: ", mod)
frequencyTable(frequencyDict)


