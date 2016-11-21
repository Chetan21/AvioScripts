import csv
import os


class Avio:
    def readInReference(self, refFile, refFilePath, filePrefix):
        result = dict()
        processFlag = False
        for row in refFile:
            tokens = row.split(",")
            token = tokens[0]
            chartNumber = tokens[1]
            fileName = filePrefix + chartNumber
            file = csv.reader(os.path.abspath(os.path.join(refFilePath, os.pardir))+"/"+fileName+".csv")
            if(file!=None):
                print "ERROR: readInReference no file"
            else:
                result[token] = fileName;
        return result

    def getParameterCore(self, parameter):
        return parameter.split(':')[0]

    def extractParamFromFile(self, inputFile, outputFile, parameter, flightId):
        print "Extracting Parameter from file..."
        headerParameter = self.getParameterCore(parameter)
        row=0
        columnMatch = -1
        processHeader = False
        headers = list()
        oFile = open(outputFile)
        with open(inputFile) as iFile:
            for line in iFile:
                row += 1
                parts = line.split(",")
                nparts = parts.__len__()
                if columnMatch == -1:
                    if row>100:
                        print "No headers found in first 100 rows"
                        return
                    if line.startswith("FLIGHT ID:"):
                        #find column
                        for i in nparts:
                            value = parts[i]
                            if value.startswith("FLIGHT ID:"):
                                value = parts[i+1]
                                if value.endswith(headerParameter):
                                    print "Found parameter match"
                                    columnMatch = i
                                    break
                elif processHeader:
                    print "Extract parameter from file processHeader "
                    if nparts > columnMatch + 2:
                        size = headers.__len__()-1
                        for i in range(0, size):
                            oFile.write(parts[columnMatch+i])
                            oFile.write(',')
                        oFile.write(parts[columnMatch+size])
                        oFile.write('\n')
                else:
                    processHeader = True
                    i = 0





    def main(self):
        #Fetch this data from avio.properties file or set a config file
        flightsIds = {}
        filePrefix = "Chart_"
        dir = ""
        refFilePath = ""

        app = Avio()
        refFile = csv.reader(refFilePath)
        refList = app.readInReference(refFile, refFilePath, filePrefix)
        parameterList = list()
        for key in refList:
            parameter = app.getParameterCore(key)
            parameterList.append(parameter)
            print "Key = "+key+" Value = "+refList[key]
            inputFile = csv.reader(dir+refList[key]+".csv")
            if inputFile != None:
                for flightId in flightsIds:
                    path = os.path.dirname(os.path.abspath(dir+"/"+flightId))
                    if not os.path.exists(path):
                        os.makedirs(path)
                    outputFile = path+flightId+"_"+refList[key]+"_"+parameter+".csv"
                    app.extractParamFromFile(inputFile, outputFile, key, flightId)


