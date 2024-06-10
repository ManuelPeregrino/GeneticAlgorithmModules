import random
import math
import numpy as np

class RouletteSelection:
    def __init__(self, evaluatedIndividuals):
        self.evaluatedIndividuals = evaluatedIndividuals   
        self.selectTest = rouletteStartup(self.evaluatedIndividuals)
        self.selectedIndividualTest = rouletteSelection(self.selectTest)
        

#Personal note here for selection. I have to generate a random float number between 0 and 1. The generated number should match the normalized value of each individual. To calculate this. I'll evaluate the percentage held by each individual. Depending on the algorithm behaviour (Maximize or minimize) should give each number a better chance to be selected.
#I used dictionaries for aranging individuals and their percentages. This will impact further in the ease of handling for crossover and mutation

def rouletteStartup(individuals):

    individuals.sort()
    individualDictionaries = {}
    for individual in individuals:
        normalizedIndividual =  math.ceil(individual/len(individuals)*100)/2
        if normalizedIndividual < 0:
            roundedNegative = int(normalizedIndividual)+abs(normalizedIndividual)
            print("pepe:",roundedNegative)
            individualDictionaries.update({individual:round(roundedNegative)})
        if normalizedIndividual > 0:
            individualDictionaries.update({individual:round(normalizedIndividual)})
            print("Pepedos:", normalizedIndividual)
    return individualDictionaries

def rouletteSelection(returnedIndividuals):
        selectedIndividuals=[]
        randomFloatsExample = random.sample(range(0,100), 2)
        if returnedIndividuals in randomFloatsExample:
            print("\nRandomnumbersforselection",randomFloatsExample)
        return returnedIndividuals