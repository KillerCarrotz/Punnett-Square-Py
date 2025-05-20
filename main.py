#Program Name: main.py

#Programmer: Kacey Brukiewa
#Date: 5/19/2025

#Program description: This program takes user input for two parent objects. Then it 
# displays a punnett square in a text file depicting likely hood of an ofspring gene 
# result. It then prompts user to run a simulation which will give a possible distribution
# of genes given an amount of ofspring.

from parent_Class import *

def main():

    #Create two parent objects with the genes assigned from the get genes funtion.
    gene_1_parent_1, gene_1_parent_1_dominant, gene_2_parent_1, gene_2_parent_1_dominant = getGenes("1")
    parent1 = Parent(gene_1_parent_1, gene_1_parent_1_dominant, gene_2_parent_1, gene_2_parent_1_dominant)
    gene_1_parent_2, gene_1_parent_2_dominant, gene_2_parent_2, gene_2_parent_2_dominant = getGenes("2")
    parent2 = Parent(gene_1_parent_2, gene_1_parent_2_dominant, gene_2_parent_2, gene_2_parent_2_dominant)

    #todo: call createPunnetSquare to output a text file with a punnet square.
    #todo: call simulateOffspring in a loop so that user can run simulation repeatedly.
    
    #Print the parent genes
    print(parent1.gene_a)
    print(parent1.gene_b)
    print(parent1.gene_a_symbol)
    print(parent1.gene_b_symbol)
    print(parent2.gene_a)
    print(parent2.gene_b)
    print(parent2.gene_a_symbol)
    print(parent2.gene_b_symbol)

def getGenes(number_of_parent):
    #Taking user input and saving them to temporary variables.
    gene_1 = input("Enter parent " + number_of_parent + " first gene:")

    #todo: create a loop for gene_1_is_dominant and gene_2_is_dominant so that only y or n are accepted outputs.
    gene_1_is_dominant = input("Is this trait dominant y/n")
    gene_1_is_dominant = gene_1_is_dominant.lower()

    gene_2 = input("Enter parent " + number_of_parent + " second gene:")

    gene_2_is_dominant = input("Is this trait dominant y/n")
    gene_2_is_dominant = gene_2_is_dominant.lower()

    #Creating a boolean value for whether a gene is dominant.
    if gene_1_is_dominant == "n":
        gene_1_dominant = False
    else:
        gene_1_dominant = True


    if gene_2_is_dominant == "n":
        gene_2_dominant = False
    else:
        gene_2_dominant = True

    return gene_1, gene_1_dominant, gene_2, gene_2_dominant

def createSquare(parent_object_1, parent_object_2):
    #createSquare function takes two parent objects and creates a grided punnet square using their genes.

    #After creating a punnet square, it will be output to a text file.
    
    return

def simulateOffspring(parent_object_1, parent_object_2, number_of_offspring):
    #simulateOffspring function takes two parent objects and determines based on the dominance of the genes passed how many offspring will have 
    #different genes.

    #After determining how many offspring are in each category using random from math, it will display a graph using matplotlib.
    
    return

if __name__ == "__main__":
    main()
