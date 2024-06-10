from initializePopulation import initializePopulation
from fitnessEvaluation import Fitness
from roulette import RouletteSelection
class main:
    def __init__(self):

        #Test Parameters Definition
        self.initial_population=5
        self.maximum = 10
        self.minimum = 1
        self.minimize = True
        self.referenceResolution = 0.8
        self.mutationProbability = 0.5

        #Modules testing
        self.initialparams = initializePopulation(self.initial_population, self.maximum, self.minimum, self.minimize)
        self.starting_array = self.initialparams.output
        self.fitnessparams = Fitness(self.minimum, self.maximum, self.referenceResolution, self.starting_array)
        self.bits = self.fitnessparams.getBits
        self.systemResolution = self.fitnessparams.sysRes
        self.evaluatedIndividuals = self.fitnessparams.getEvaluatedIndividuals
        self.binaries = self.fitnessparams.getBinaries
        self.testconversion = self.fitnessparams.binariesConverted
        self.testRoulette = RouletteSelection(self.fitnessparams.getEvaluatedIndividuals)
        self.testPair = self.testRoulette.selectedIndividualTest

        print("\nGenerated Individuals",self.starting_array)
        print("\nObtained Bits:",self.bits)
        print("\nSystem Resolution: ",self.systemResolution)
        print("\nEvaluated Individuals:",self.evaluatedIndividuals)
        print("\nEvaluated individuals converted to binaries",self.binaries)
        print("\nBinaries Converted back to int",self.testconversion)
        print("\nRoulette Selection first test",self.testRoulette.selectTest)
        print("\nSelected Individuals Test",self.testRoulette.selectedIndividualTest)

        
main()