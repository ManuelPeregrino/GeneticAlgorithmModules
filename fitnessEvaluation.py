import numpy as np
import math

#Definition of Fitness class. This might be refactorized for better handling.
class Fitness:
    def __init__(self, mini, maxi, referenceResolution, individuals):
        self.mini = mini
        self.maxi = maxi
        self.referenceResolution = referenceResolution
        self.evaluation = f(x=individuals[0])
        self.getBits = getBits(self.mini,self.maxi, self.referenceResolution)
        self.sysRes = getSystemResolution(self.mini, self.maxi, self.getBits)
        self.individuals = individuals
        self.getEvaluatedIndividuals = getEvaluatedIndividuals(self.individuals, self.sysRes, self.mini)
        self.getBinaries = getBinaries(self.individuals, self.getBits)
        self.binariesConverted = recursivetest(self.getBinaries)

#Reference Function for evaluate x values.
def f(x):
    return x*np.cos(x)

#Function for getting the max bits used in the algorithm.
def getBits(mini, maxi, referenceResolution):
    referenceResolution = referenceResolution
    bitRange = maxi-mini
    bitPoints = bitRange/referenceResolution + 1
    bitTotal = np.ceil(np.log2(bitPoints))
    bitEstimate = 2**bitTotal - 1
    return bitEstimate%16

#Function for estimate the System resolution. System resolution is the precision limit of estimation
#given by the system.
def getSystemResolution(mini, maxi, bitEstimate):
    bitRange = int(maxi)-int(mini)
    sistemResolution = bitRange/bitEstimate
    return sistemResolution

#Function for calculating the values of each individual.
#in binary
def getBinaries(individuals, bits):
    binaries = []
    characters = []
    for individual in individuals:
            individualBinary = bin(individual)[2:].zfill(int(bits))
            #for character in individualBinary:
            #   characters.append(character)
            binaries.append(individualBinary)
    return binaries

#Function for estimating the fitness of each individual.
def getEvaluatedIndividuals(individuals, systemResolution, mini):
    fitnessArray = []
    for individual in individuals:
            evaluatedIndividual = f(individual)
            fitnessArray.append(evaluatedIndividual)
    return fitnessArray

#Test function for converting back again the binaries to
#decimal values.
def binaryToDecimal(binary):
        int(binary)
        decimal, i = 0, 0
        while(binary != 0):
            dec = binary % 10
            decimal = decimal + dec * pow(2, i)
            binary = binary//10
            i += 1
        return(decimal)

#Test function for grouping the converted values
#in a data structure.
def recursivetest(binaries):
    convertedBinaries = []
    for binary in binaries:
        convertedBinaries.append(binaryToDecimal(int(binary)))
    return convertedBinaries
