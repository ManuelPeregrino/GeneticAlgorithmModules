import random

#Class for initializing the algorithm values. This class might change its structure in the future.
class initializePopulation:
    def __init__(self, initial_population, maximum, minimum, minimize):
        self.minimize = minimize
        self.initialPopulation = initial_population
        self.mini = minimum
        self.maxi = maximum
        self.output = generatePopulation(self.initialPopulation, self.mini, self.maxi)
        if self.minimize == True:
            self.output.sort(reverse = True)
        else:
            self.output.sort()
    
def generatePopulation(initialPopulation, mini, maxi):
    generatedIndividuals = random.sample(range(mini, maxi), initialPopulation)
    return generatedIndividuals