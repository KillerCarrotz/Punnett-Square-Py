#Program Name: main.py

#Programmer: Kacey Brukiewa
#Date: 5/19/2025

#Program description: This program takes user input for two parent objects. Then it 
# displays a punnett square in a text file depicting likely hood of an ofspring gene 
# result. It then prompts user to run a simulation which will give a possible distribution
# of genes given an amount of ofspring.

#TODO: Add functionality to simulateOffspring so that it generates offspring of a specified amount with random gene distribution.
#TODO: Call simulateOffspring in a loop so that user can run simulation repeatedly.
#TODO: In simulateOffspring; Use MatPlotLib to generate a graph of offspring results.
#TODO: Clean user input so only a 30 char maximum for gene names and y/n for dominance are accepted.
#TODO: Use loops in main so that new punnett squares can be generated back to back.

from parent_Class import *

def main():

    #Create two parent objects with the genes assigned from the get genes funtion.
    gene_1_parent_1, gene_1_parent_1_dominant, gene_2_parent_1, gene_2_parent_1_dominant = getGenes("1")
    parent1 = Parent(gene_1_parent_1, gene_1_parent_1_dominant, gene_2_parent_1, gene_2_parent_1_dominant)
    gene_1_parent_2, gene_1_parent_2_dominant, gene_2_parent_2, gene_2_parent_2_dominant = getGenes("2")
    parent2 = Parent(gene_1_parent_2, gene_1_parent_2_dominant, gene_2_parent_2, gene_2_parent_2_dominant)
    
    #createSquare will create the punnett square and write it to punnett_py.txt
    createSquare(parent1, parent2)

def getGenes(number_of_parent):#number_of_parrent is used to acurately prompt the user.
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

def createSquare(parent1, parent2):
    #createSquare function takes two parent objects, creates a punnet square using their genes, and prints it to the terminal and writes it to punnett_py.txt.
    punnet_square_lines = [
        " ____________________ \n",
        "|        Parent 1    |\n",
        "|P        ", parent1.gene_a_symbol, "      ", parent1.gene_b_symbol, "   |\n",
        "|a     ______ ______ |\n",
        "|r  ", parent2.gene_a_symbol, " |  ", parent1.gene_a_symbol, parent2.gene_a_symbol, "  |  ", parent1.gene_b_symbol, parent2.gene_a_symbol, "  ||\n",
        "|e    |______|______||\n",
        "|n  ", parent2.gene_b_symbol, " |  ", parent1.gene_a_symbol, parent2.gene_b_symbol, "  |  ", parent1.gene_b_symbol, parent2.gene_b_symbol, "  ||\n",
        "|t    |______|______||\n",
        "|2                   |\n",
        "|____________________|\n"
    ]

    #Print punnet square to terminal
    print(punnet_square_lines)

    #Create and output to a text file.
    punnett_file_path = "punnett_py.txt"
    with open(punnett_file_path, 'a') as file:
        file.writelines(punnet_square_lines)
    
    #Informs user of file write.
    print(f"This square has been written to {punnett_file_path} (the file is now closed automatically).") 

    return

def simulateOffspring(parent_object_1, parent_object_2, number_of_offspring):
    #simulateOffspring function takes two parent objects and determines based on the dominance of the genes passed how many offspring will have 
    #different genes.

    #todo: After determining how many offspring are in each category using random from math, it will display a graph using matplotlib.
    
    return

if __name__ == "__main__":
    main()
