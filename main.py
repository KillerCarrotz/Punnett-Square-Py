#Program Name: main.py

#Programmer: Kacey Brukiewa
#Date: 5/19/2025

#Program description: This program takes user input for two parent objects. Then it 
# displays a punnett square in a text file depicting likely hood of an ofspring gene 
# result. It then prompts user to run a simulation which will give a possible distribution
# of genes given an amount of ofspring.

from parent_Class import *

def main():


    
    #Create a parent object with the genes assigned from the user input.
    gene_1_parent_1, gene_1_parent_1_dominant, gene_2_parent_1, gene_2_parent_1_dominant = getGenes("1")
    parent1 = Parent(gene_1_parent_1, gene_1_parent_1_dominant, gene_2_parent_1, gene_2_parent_1_dominant)
    gene_1_parent_2, gene_1_parent_2_dominant, gene_2_parent_2, gene_2_parent_2_dominant = getGenes("2")
    parent2 = Parent(gene_1_parent_2, gene_1_parent_2_dominant, gene_2_parent_2, gene_2_parent_2_dominant)

    #Print the parent1 genes
    print(parent1.gene_a)
    print(parent1.gene_b)
    print(parent2.gene_a)
    print(parent2.gene_b)

def getGenes(number_of_parent):
    #Taking user input and saving them to temporary variables.
    gene_1 = input("Enter parent " + number_of_parent + " first gene:")
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

if __name__ == "__main__":
    main()
